# Slack Posting

from slack_sdk import WebClient

def post_to_slack(answers, slack_token, slack_channel):
    client = WebClient(token=slack_token)
    response = client.chat_postMessage(channel=slack_channel, text=json.dumps(answers, indent=4))
    return response
