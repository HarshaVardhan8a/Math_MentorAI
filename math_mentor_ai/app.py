import streamlit as st

from agents.parser_agent import parser_agent
from agents.intent_router import intent_router
from agents.solver_agent import solver_agent
from agents.verifier_agent import verifier_agent
from agents.explainer_agent import explainer_agent
from agents.memory_agent import memory_manager

from multimodal.text_input import get_text_input
from multimodal.image_ocr import extract_text_from_image
from multimodal.audio_asr import transcribe_audio

from rag.retriever import retrieve_context


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Math Mentor", layout="wide")

st.title("📘 AI Math Mentor")
st.subheader("Multimodal | RAG | Agents | HITL")


# ---------------- SESSION STATE INIT ----------------
if "extracted_data" not in st.session_state:
    st.session_state.extracted_data = None

if "parsed_output" not in st.session_state:
    st.session_state.parsed_output = None


# ---------------- INPUT MODE ----------------
input_mode = st.selectbox(
    "Choose input mode",
    ["Text", "Image", "Audio"]
)


# ---------------- TEXT ----------------
if input_mode == "Text":
    user_text = st.text_area("Enter math problem")

    if st.button("Process Text"):
        st.session_state.extracted_data = get_text_input(user_text)
        st.session_state.parsed_output = None


# ---------------- IMAGE ----------------
elif input_mode == "Image":
    image_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    if image_file:
        st.image(image_file, caption="Uploaded Image", width=700)

        if st.button("Extract Text"):
            st.session_state.extracted_data = extract_text_from_image(image_file)
            st.session_state.parsed_output = None


# ---------------- AUDIO ----------------
elif input_mode == "Audio":
    
    st.markdown("### 🎙️ Audio Input (Generic)")
    st.info("Upload an audio file containing a spoken math problem.")

    # Extended file types support
    audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a", "ogg", "aac", "wma"])

    if audio_file:
        st.audio(audio_file)

        if st.button("Transcribe Audio"):
            st.session_state.extracted_data = transcribe_audio(audio_file)
            st.session_state.parsed_output = None


# ---------------- PREVIEW & EDIT ----------------
if st.session_state.extracted_data:
    st.markdown("### 🔍 Extracted Text (Editable)")

    edited_text = st.text_area(
        "Review / Edit",
        value=st.session_state.extracted_data["text"] or ""
    )

    st.markdown("### 📊 Confidence Score")
    st.progress(min(st.session_state.extracted_data["confidence"], 1.0))

    if st.session_state.extracted_data["confidence"] < 0.6:
        st.warning("⚠️ Low confidence — Human verification required (HITL)")

    if st.button("Run Parser Agent"):
        st.session_state.parsed_output = parser_agent(edited_text)


# ---------------- PARSER → RAG → SOLVER → VERIFIER ----------------
if st.session_state.parsed_output:
    parsed_output = st.session_state.parsed_output

    st.markdown("## 🧠 Parser Agent Output")
    st.json(parsed_output)

    # -------- GUARDRAIL: PARSER AMBIGUITY --------
    if parsed_output["needs_clarification"]:
        st.warning("❗ Clarification Needed")
        st.info(parsed_output["clarification_question"])

    else:
        # ---------------- INTENT DISPATCH ----------------
        intent = intent_router(parsed_output)
        
        # UI: Agent Workflow Trace
        with st.expander("🕵️ Agent Workflow Trace", expanded=False):
            st.markdown(f"""
            1. **Parser Agent**: Extracted topic `{parsed_output['topic']}`
            2. **Intent Router**: Determined Intent `{intent}`
            3. **Solver/RAG**: {'Active' if intent == 'solve_math' else 'Related Concepts Only'}
            """)

        if intent == "chitchat":
            st.warning("⚠️ Input ambiguous or off-topic.")
            st.stop()
            
        elif intent == "explain_only":
             st.info("ℹ️ Explanation Mode: Showing related concepts.")

        # ---------------- RAG RETRIEVAL ----------------
        with st.expander("📚 View Related Math Concepts"):
             try:
                 retrieved_chunks = retrieve_context(parsed_output["problem_text"])
                 
                 if not retrieved_chunks:
                     st.info("No specific knowledge found in RAG knowledge base.")

                 for i, chunk in enumerate(retrieved_chunks):
                     st.markdown(f"**Source {i+1}**")
                     st.info(chunk)
             except Exception as e:
                 st.error(f"RAG Retrieval failed: {e}")
                 retrieved_chunks = []

        # ---------------- SOLVER AGENT ----------------
        if intent == "solve_math":
            st.markdown("## 🧮 Step-by-Step Solution")
            
            # --- MEMORY CHECK ---
            similar_entry = memory_manager.find_similar(parsed_output["problem_text"])
            if similar_entry:
                st.success("💡 Found a similar solved problem in memory!")
                with st.expander("View Past Solution"):
                    st.markdown(f"**Problem:** {similar_entry['problem_text']}")
                    st.markdown(f"**Solution:** {similar_entry['solution']}")
                    st.caption(f"Retrieved at: {similar_entry.get('timestamp', 'Unknown')}")

            # --- SOLVE ---
            solver_output = solver_agent(
                parsed_output["problem_text"],
                retrieved_chunks if 'retrieved_chunks' in locals() else []
            )

            if solver_output["error"]:
                st.error("❌ Could not solve")
                st.info(solver_output["error"])
                st.warning("Please try rephrasing the problem.")

            else:
                # ---------------- VERIFIER AGENT ----------------
                verifier_output = verifier_agent(
                    parsed_output["problem_text"],
                    solver_output["solution"]
                )

                if verifier_output["verified"]:
                    st.markdown("### ✅ Result Verified")
                else:
                    st.warning(f"⚠️ Verification: {verifier_output['reason']}")

                # Display steps
                for step in solver_output["steps"]:
                    st.write(f"• {step}")

                # ---------------- EXPLAINER AGENT ----------------
                with st.expander("🗣️ Explanation (AI)"):
                    explanation = explainer_agent(
                        parsed_output["problem_text"], 
                        solver_output["steps"], 
                        solver_output["solution"]
                    )
                    st.write(explanation)

                st.success(f"**Final Answer:** {solver_output['solution']}")
                
                # ---------------- FEEDBACK LOOP (HITL) ----------------
                st.markdown("---")
                st.write("### 📝 Feedback (Learning Signal)")
                col1, col2 = st.columns([1, 8])
                
                if col1.button("✅ Correct"):
                    memory_manager.add_entry({
                        "problem_text": parsed_output["problem_text"],
                        "solution": solver_output["solution"],
                        "steps": solver_output["steps"],
                        "feedback": "positive"
                    })
                    st.toast("Saved to memory! The system has learned from this.")
                    
                if col2.button("❌ Incorrect"):
                    # In a real app, this would trigger a re-route or manual edit
                    memory_manager.add_entry({
                        "problem_text": parsed_output["problem_text"],
                        "solution": solver_output["solution"],
                        "steps": solver_output["steps"],
                        "feedback": "negative"
                    })
                    st.toast("Feedback recorded. Will improve next time.")
