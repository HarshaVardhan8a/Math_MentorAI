Math Mentor AI is an advanced educational assistant designed to help students understand mathematics—not just get answers.

It combines deterministic symbolic computation (SymPy) with Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to solve, verify, and explain math problems step-by-step, while continuously learning from user feedback.

🏗️ Architecture

Math Mentor AI is built on a Multi-Agent Architecture, where specialized agents collaborate to process inputs, reason about intent, solve problems, and explain results.

graph TD
    User[User Input] --> Input{Input Mode}

    Input -->|Text| TextProcessed
    Input -->|Image| OCR[OCR Extractor]
    Input -->|Audio| ASR[Whisper Transcription]

    OCR --> TextProcessed[Cleaned Text]
    ASR --> TextProcessed

    TextProcessed --> MemoryCheck{Memory Check}

    MemoryCheck -->|Found Similar| MemoryResult[Show Past Solution]
    MemoryCheck -->|New Problem| Parser[Parser Agent]

    Parser --> Router{Intent Router}

    Router -->|Explain| RAG[RAG Retrieval] --> Explainer[Explainer Agent]
    Router -->|Solve| SolverFlow

    subgraph Solving Pipeline
        SolverFlow --> RAGSolver[RAG Context]
        RAGSolver --> Solver[Solver Agent]
        Solver --> Verifier[Verifier Agent]
        Verifier --> Final[Final Answer]
    end

    Final --> Feedback[User Feedback]
    Feedback --> MemoryStore[(Memory / Self-Learning)]

🌟 Key Features
1. 🧠 Multi-Agent Framework

Each agent has a focused responsibility:

Parser Agent
Cleans and normalizes user input
(e.g., “three x squared” → 3x²)

Intent Router
Determines whether the user wants to:

Solve a problem

Get an explanation

Ask a general question

Solver Agent
A deterministic symbolic math engine powered by SymPy

No guessing. No hallucinations. Just math.

Verifier Agent
Cross-checks results against constraints and edge cases.

Explainer Agent
Converts symbolic steps into plain-English explanations.

Memory Agent
Stores solved problems and retrieves them instantly if asked again.

2. 👁️🎙️ Multimodal Inputs

Solve math problems using multiple input modalities:

✍️ Text
Type equations directly (LaTeX supported).

📸 Image
Upload photos or screenshots of homework.
Math Mentor AI uses OCR to extract equations.

🎙️ Audio
Speak your problem naturally.
Powered by OpenAI Whisper for transcription.

3. 📚 Retrieval-Augmented Generation (RAG)

Maintains a FAISS vector database of:

Math definitions

Theorems

Formulas

Retrieves relevant context before solving to ground reasoning
(e.g., quadratic formula, derivative rules, identities)

4. 🔄 Human-in-the-Loop (HITL) & Self-Learning

✏️ Correction Loop
Edit OCR / transcription results before solving.

👍👎 Feedback System
Mark solutions as:

✅ Correct

❌ Incorrect

🧠 Continuous Learning
Verified solutions are saved to memory—no retraining required.

🛠️ Technology Stack

Frontend: Streamlit

Agent Orchestration: Custom Agent Loop (inspired by LangGraph)

Math Engine: SymPy

Vector Search: FAISS
, SentenceTransformers

OCR: EasyOCR

Speech-to-Text: OpenAI Whisper

🚀 Getting Started
Prerequisites

Python 3.10+

FFmpeg (required for audio input)

Install FFmpeg (Windows):

winget install ffmpeg


Or download from ffmpeg.org
 and add it to your PATH.

Installation

Clone the repository

git clone https://github.com/your-username/math-mentor-ai.git
cd math-mentor-ai


Create a virtual environment (recommended)

python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


⏳ This may take a few minutes due to Torch and transformer models.

Environment configuration

copy .env.example .env


No API keys are required for the core solver.
Add keys only if extending with OpenAI or other LLM providers.

▶️ Running the App
streamlit run app.py


Open your browser at:
👉 http://localhost:8501

📂 Directory Structure
math_mentor_ai/
├── agents/              # The "Brains"
│   ├── parser_agent.py
│   ├── intent_router.py
│   ├── solver_agent.py
│   ├── verifier_agent.py
│   ├── explainer_agent.py
│   └── memory_agent.py
├── multimodal/          # The "Senses"
│   ├── image_ocr.py
│   ├── audio_asr.py
│   └── text_input.py
├── rag/                 # The "Knowledge"
│   ├── index/
│   ├── knowledge_base/
│   └── retriever.py
├── data/                # The "Memory"
│   └── memory.jsonl
├── app.py               # Streamlit entry point
├── requirements.txt
└── README.md

📖 Usage Guide
➗ Solving a Math Problem

Select Input Mode → Text

Enter:

Solve x^2 - 5x + 6 = 0


Click Process

Review:

Step-by-step solution

Natural language explanation

Click ✅ Correct to store the solution in memory

📸 Using Image Input

Select Input Mode → Image

Upload a clear PNG or JPG

Click Extract Text

Correct OCR errors if needed

Click Run Parser Agent

🧠 Memory Feature

Solve a problem correctly

Refresh the page

Ask the same question again

See:

💡 Found a similar solved problem in memory!

Instant retrieval = faster answers 🚀
