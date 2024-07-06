import re
import json

def read_questions(file_path):
    # Load the JavaScript file
    with open(file_path, 'r') as file:
        js_content = file.read()

    # Use a regular expression to extract the JSON array
    match = re.search(r'const questions = (\[.*?\]);', js_content, re.DOTALL)
    if match:
        questions_json = match.group(1)
        questions = json.loads(questions_json)
    else:
        raise ValueError("Couldn't find the questions array in the JavaScript file.")

    return questions
