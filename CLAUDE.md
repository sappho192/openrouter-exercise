# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an OpenRouter API exercise project that demonstrates language translation using the OpenRouter API with Google's Gemma model. The project is a simple Python application using `httpx` for API requests.

## Development Setup

This project uses `uv` for dependency management and Python 3.11.

**Install dependencies:**
```bash
uv sync
```

**Run the application:**
```bash
uv run python main.py
```

## Environment Configuration

The application requires an `OPENROUTER_API_KEY` environment variable. This should be set in a `.env` file:
```
OPENROUTER_API_KEY=your_api_key_here
```

## Architecture

The codebase is minimal and consists of a single entry point:

- **main.py**: Contains the main application logic that:
  - Loads environment variables using `python-dotenv`
  - Makes POST requests to the OpenRouter API (`https://openrouter.ai/api/v1/chat/completions`)
  - Uses the `google/gemma-3-27b-it` model for language translation
  - Expects responses in the OpenRouter chat completions format with `choices[0].message.content`

## API Integration

The application uses OpenRouter's chat completions API with:
- Model: `google/gemma-3-27b-it`
- Authorization via Bearer token
- System message to instruct the model as a language translator
- Response parsing expects the standard OpenRouter response structure
