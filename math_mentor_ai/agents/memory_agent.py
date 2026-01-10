import json
import os
import difflib
from datetime import datetime

MEMORY_FILE = "data/memory.jsonl"

class MemoryManager:
    def __init__(self, filepath=MEMORY_FILE):
        self.filepath = filepath
        self.ensure_memory_file()

    def ensure_memory_file(self):
        """Creates the memory file if it doesn't exist."""
        if not os.path.isabs(self.filepath):
             # Make it relative to this file? No, relative to CWD (project root) is fine.
             pass
        
        directory = os.path.dirname(self.filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
            
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                pass

    def add_entry(self, entry: dict):
        """
        Saves an interaction.
        Expected keys: "problem_text", "solution", "steps", "feedback" (optional)
        """
        entry["timestamp"] = datetime.now().isoformat()
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry) + "\n")

    def find_similar(self, current_problem: str, threshold=0.8):
        """
        Finds a similar solved problem from history.
        """
        if not os.path.exists(self.filepath):
            return None

        best_match = None
        highest_ratio = 0.0

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        past_problem = data.get("problem_text", "")
                        
                        # Simple similarity (perfect for "reuse solution patterns")
                        ratio = difflib.SequenceMatcher(None, current_problem.lower(), past_problem.lower()).ratio()
                        
                        if ratio > highest_ratio:
                            highest_ratio = ratio
                            best_match = data
                    except json.JSONDecodeError:
                        continue
        except Exception:
            return None

        if highest_ratio >= threshold:
            return best_match
        
        return None

# Singleton instance
memory_manager = MemoryManager()
