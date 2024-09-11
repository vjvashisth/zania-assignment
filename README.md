# Zania | Challenge for AI Engineers

## Problem Statement - 
## Create an AI Agent that leverages the capabilities of a Large Language Model. 

**Description** - This agent should be able to extract answers based on the content of a large PDF document and post the results on Slack, ideally using OpenAI LLMs. 

**Instructions** - If using Langchain or LLama Index framework to implement this agent's functionality, don’t use pre-built chains for the task. Implement the logic yourself. Please write production grade code as opposed to scripts as we will be evaluating your code quality.

**Inputs-**
1. A list of questions.
2. A PDF file containing the document over which the questions will be answered.
**Output-**
1. structured JSON blob that pairs each question with its corresponding answer
2. Answers should be word to word match if the question is a word to word match

## Design Concept
The AI agent will consist of the following components:
1. **PDF Extractor:** To extract the text content from the PDF.
2. **Question Matcher:** To match the input questions against the extracted PDF content using various search strategies.
3. **Answer Extraction:** To extract the specific answers and format them in a structured JSON blob.
4. **Slack Integration:** To post the resulting answers in a Slack channel.

## Workflow
**Input:**
1. Questions List: A list of questions provided by the user.
2. PDF File: The PDF document in which the answers to the questions need to be found.

**Processing:**
1. Text Extraction: Parse the PDF file and extract the text using a library like PyPDF2, pdfplumber, or pdfminer.
2. Question Matching: For each question, search for the answer in the extracted text. This will be done using word-to-word matching or other matching techniques.
3. Answer Extraction: Once a match is found, the relevant portion of text will be returned as the answer.
4. Generate JSON: For each question, pair the question with the answer and structure the result into a JSON object.

**Output:**
1. A structured JSON blob that pairs each question with its corresponding answer.
2. If a word-to-word match is found, the exact match will be returned.

## Ways to Improve Accuracy
1. **Preprocessing:**
   1. Clean the extracted text: Remove headers, footers, page numbers, and other irrelevant content.
   2. Segment text: Split text into sentences or paragraphs to improve contextual matching.
2. **Advanced Matching:**
   1. Semantic Search: Instead of exact word matching, use semantic similarity models like BERT or Sentence Transformers to match questions to semantically similar content.
   2. Fuzzy Matching: Use libraries like fuzzywuzzy or difflib for finding similar matches when exact word matching fails.
   3. Contextualized Search: Find paragraphs or sections related to the question context, rather than single sentences.
3. **Answer Extraction:**
   1. Contextual Answer Extraction: If the answer appears in a longer paragraph, extract the surrounding context rather than a direct word-to-word match.
   2. Structured PDF Parsing: If the document has well-structured data (e.g., headers, sections), use this to limit the search scope to relevant sections of the document.
4. **Natural Language Processing (NLP):**
   1. Use Named Entity Recognition (NER) to find specific entities like policies, dates, and names relevant to the questions.
   2. Keyword Highlighting: Use TF-IDF or word vectors to identify the most important keywords and match them to the questions.
  
## Making the Code Modular, Scalable, and Production-Grade
1. **Modular Design:**
   1. Separate the Components: Break down the code into distinct modules for:
      1. PDF Extraction (pdf_extractor.py)
      2. Question Matching (question_matcher.py)
      3. Slack Integration (slack_poster.py)
      4. Main Logic (main.py)
   2. Each module should be individually testable and reusable in different contexts.
2. **Scalability:**
   1. Asynchronous Processing: Use asynchronous processing (asyncio) or job queues like Celery for handling large PDFs or multiple requests simultaneously.
   2. Batch Processing: If many PDFs or large documents need to be processed, consider batch jobs and scalable services like AWS Lambda or Google Cloud Functions.
   3. Distributed Processing: For very large documents or multiple users, use distributed systems such as Apache Spark or Dask.
3. **Error Handling and Logging:**
   1. Implement robust error handling for edge cases such as corrupted PDF files, or missing sections.
   2. Use centralized logging (with logging module or services like ElasticSearch and Kibana) for better debugging and production monitoring.
4. **Production-Grade Deployment:**
   1.CI/CD Pipeline: Automate testing, deployment, and updates with a CI/CD pipeline using tools like GitHub Actions, Jenkins, or CircleCI.
   2. Containerization: Use Docker to package the solution into containers, making it easier to deploy on cloud platforms or as part of a larger microservices architecture.
   3. API-based Design: Make the solution accessible via APIs (using frameworks like Flask or FastAPI) for easier integration into various systems.
5. **Security:**
   1. Secure sensitive information like the Slack token by storing them in environment variables or a secret management service like AWS Secrets Manager.
   2. Implement authentication and authorization if this service is public-facing.
6. **Testing:**
   1. Write unit tests for each module, especially text extraction and question matching.
   2. Add integration tests to simulate the full workflow (e.g., extracting text, finding answers, and posting to Slack).
