import google.generativeai as genai

from src import config

class Gemini:
    def __init__(self):
        api_key = config.get_gemini_api_key()
        genai.configure(api_key=api_key)

    def inference(self, model_id: str, prompt: str) -> str:
        model = genai.GenerativeModel(model_id)
        response = model.generate_content(prompt)
        return response.text
