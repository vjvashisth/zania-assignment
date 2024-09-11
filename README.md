# zania-assignment
## Zania | Challenge for AI Engineers

Problem Statement - Create an AI Agent that leverages the capabilities of a Large Language Model. 

Description - This agent should be able to extract answers based on the content of a large PDF document and post the results on Slack, ideally using OpenAI LLMs. 

Instructions - If using Langchain or LLama Index framework to implement this agent's functionality, don’t use pre-built chains for the task. Implement the logic yourself. Please write production grade code as opposed to scripts as we will be evaluating your code quality.

Inputs- 
1. A list of questions.
2. A PDF file containing the document over which the questions will be answered.
Output-
1. structured JSON blob that pairs each question with its corresponding answer
2. Answers should be word to word match if the question is a word to word match
