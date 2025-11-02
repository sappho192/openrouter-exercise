# OpenRouter Exercise

A simple Python application demonstrating language translation using the OpenRouter API with Google's Gemma model.

## Features

- Language translation via OpenRouter API
- Uses Google's Gemma 3 27B model
- Simple command-line interface
- Environment-based configuration

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- OpenRouter API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd genai-exercise
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Create a `.env` file in the project root:
```bash
OPENROUTER_API_KEY=your_api_key_here
```

You can obtain an API key from [OpenRouter](https://openrouter.ai/).

## Usage

Run the application:
```bash
uv run python main.py
```

The application will translate the configured text (currently Korean to Japanese) and display the result.

## Configuration

The application can be configured by modifying `main.py`:

- **Model**: Change the `model` field in the API request (default: `google/gemma-3-27b-it`)
- **Translation prompt**: Modify the user message content
- **System instructions**: Adjust the system message to change behavior

## Project Structure

```
genai-exercise/
    main.py           # Main application entry point
    pyproject.toml    # Project dependencies and metadata
    uv.lock          # Locked dependency versions
    .env             # Environment variables (not in git)
    README.md        # This file
```

## Dependencies

- `httpx` - Modern HTTP client for Python
- `python-dotenv` - Environment variable management

## License

See [LICENSE](LICENSE) file for details.
