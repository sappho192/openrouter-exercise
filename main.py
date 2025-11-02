import os
from dotenv import load_dotenv
import httpx

load_dotenv()


def main():
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    response = httpx.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "google/gemma-3-27b-it",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a language translator. You MUST reply with translated text ONLY."
                },
                {
                    "role": "user",
                    "content": "Translate the following text to Japanese: 안녕하세요! 혹시 어제 보내주셨던 보고서에 대해 설명해 주실 수 있을까요? 필요하다면 회의를 가져도 됩니다."
                }
            ]
        },
    )

    result = response.json()
    print(result["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()
