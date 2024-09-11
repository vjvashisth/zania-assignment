# Answer Extraction

def extract_answers(questions, text):
    answers = {}
    for question in questions:
        answer = find_answer_in_text(question, text)
        answers[question] = answer
    return answers
