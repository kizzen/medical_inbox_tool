# Automated Clinical Inboxes for Physicians

## Overview

This Flask application demonstrates the potential of Large Language Models (LLMs) in automatically generating replies for physician inboxes. Utilizing clinical notes, it produces synthetic questions linked semantically through GPT4. The system then offers answers with and without context, also using GPT4. The primary objective is to create an MVP that explores the viability of assisting doctors in managing their email workload.

## Features

1. **Automated Replies**: Generates automated replies for overflowing physician inboxes.
2. **Context-aware Responses**: Answers questions using both context from the clinical notes and without, showcasing the difference in response quality.
3. **Interactive UI**: Encapsulated within a Flask application for easy user interaction.

### Requirements

- Python 3.x
- Flask
- OpenAI's Python SDK

## Getting Started

### How to Run the Flask App

1. Clone the repository
- `git clone https://github.com/kizzen/medical_inbox_tool.git`
2. In the directory you just cloned, create and activate a new virtual environment
- `cd medical_inbox_tool`
- `conda create -n medical_inbox_env`
- `conda activate medical_inbox_env`
3. Install the necessary packages from requirements.txt into the newly create environment
- `pip install -r requirements.txt`
4. Replace config.template.json with config.json and edit config.json with your API key
5. Launch the Flask app from the Terminal
- `python app.py`
6. Click the given URL to access the app.: http://127.0.0.1:5000.

### Usage

- Interact with the app's GUI to view clinical notes, patient questions, and GPT4-generated responses.
- Compare the context-aware and non-contextual responses to assess the potential benefits of using LLMs in this context.

### Contributing
All contributions are welcome! 

While this MVP showcases an exciting application of LLMs in the medical field, there's immense potential for refinement and expansion. It presents a promising vision of how technology could assist in the healthcare sector, sparing doctors from administrative hassles and letting them focus more on patient care.

Note: Before deploying or extending the application, ensure thorough testing, especially given the critical nature of the domain. Always consider the ethical and practical implications of automating processes in healthcare.

## License

[MIT License](https://github.com/kizzen/pdf-chatbot/blob/main/LICENSE)

## Acknowledgments

Inspired by [this article](https://medium.com/@swanson.eric.karl/clinical-inbox-managers-will-need-more-than-llms-to-work-f144929d7057)

## Contact
For any queries or feedback, reach out to me at ezzine.khalil@gmail.com or via my [LinkedIn Profile](https://www.linkedin.com/in/kezzine)


