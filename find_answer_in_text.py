# Question Matcher

import re

def find_answer_in_text(question, text):
    # Word-to-word matching
    match = re.search(re.escape(question), text, re.IGNORECASE)
    if match:
        start_idx = match.start()
        end_idx = start_idx + len(question)
        # Extract sentence where the question is found
        answer = text[start_idx:end_idx]
        return answer
    else:
        return "Answer not found"
