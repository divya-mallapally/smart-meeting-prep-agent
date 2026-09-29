import os

try:
    import google.generativeai as genai  # type: ignore # pylint: disable=import-error
except ImportError:
    genai = None  # type: ignore


def has_valid_api_key(api_key: str = None) -> bool:
    key = api_key or os.getenv("GEMINI_API_KEY")
    return bool(key and str(key).strip())


def configure_agent(api_key: str = None):
    if genai is None:
        return
    key = api_key or os.getenv("GEMINI_API_KEY")
    if key and str(key).strip():
        genai.configure(api_key=str(key).strip())


def generate_response(prompt: str, api_key: str = None) -> str:
    if genai is None:
        return "google-generativeai is not installed in the current interpreter."
    configure_agent(api_key)
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"