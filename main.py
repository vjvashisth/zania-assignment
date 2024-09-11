# Main Logic

def main(pdf_file, questions, slack_token, slack_channel):
    text = extract_text_from_pdf(pdf_file)
    answers = extract_answers(questions, text)
    post_to_slack(answers, slack_token, slack_channel)
