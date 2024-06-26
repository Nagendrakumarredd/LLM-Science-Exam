# LLM-Science-Exam
LLM Science Exam is a comprehensive tool designed to test and evaluate the knowledge and problem-solving skills in the field of science.
This project leverages large language models (LLMs) to create, administer, and grade science exams. The goal is to provide an intelligent, automated solution for educational institutions, educators, and learners to assess understanding and proficiency in various scientific disciplines.
# Features
Question Generation: Automatically generate diverse and challenging science exam questions using LLMs.
Automated Grading: Provide instant, unbiased grading of exam responses.
Analytics and Reporting: Detailed performance analytics and reporting to track progress and identify areas of improvement.
Multi-Disciplinary: Supports a wide range of scientific subjects including Physics, Chemistry, Biology, Earth Science, and more.
Customizable Exams: Create customized exams tailored to specific curricula and difficulty levels.



# Installation
To get started with LLM Science Exam, follow these steps:

# Clone the repository:

bash
Copy code
git clone https://github.com/nagendrakumarredd/llm-science-exam.git
cd llm-science-exam
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add the necessary environment variables. For example:

env
# Copy code
OPENAI_API_KEY=your_openai_api_key
Run the application:

bash
Copy code
python main.py
Usage
# Generating Questions
To generate exam questions, run the generate_questions.py script:

bash
Copy code
python generate_questions.py --subject physics --level highschool
# Options:
1) subject: Specify the subject (e.g., physics, chemistry, biology).
2) level: Specify the difficulty level (e.g., elementary, middle, highschool, college).
Administering Exams
To administer an exam, use the administer_exam.py script:

bash
Copy code
python grade_exam.py --exam_id 12345 --responses responses.json
Options:
1) exam_id: Specify the exam ID to grade.
2) responses: Path to the JSON file containing student responses.
# Contributing
We welcome contributions from the community! If you would like to contribute to LLM Science Exam, please follow these steps:

# Fork the repository.
Create a new branch for your feature or bugfix.
bash
Copy code
git checkout -b feature-name
Make your changes and commit them with a descriptive message.
bash
Copy code
git commit -m "Add feature: description"
Push your changes to your fork.
bash
Copy code
git push origin feature-name
Create a pull request with a detailed description of your changes.
