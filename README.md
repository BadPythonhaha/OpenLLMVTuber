# Open-LLM-VTuber Modified
![GitHub License](https://img.shields.io/github/license/BadPythonhaha/OpenLLMVTuber)

[CN](README_CN.md)
[Original](./doc/README_Original.md)

## What is this?

This is a modified version of the [Open-LLM-VTuber](https://github.com/t41372/Open-LLM-VTuber), only using Ollama, FunASR and MeloTTS as the main components. Aiming to provide a more lightweight and easy-to-use solution for creating and running VTubers on your local machine, and trying to make it easier for Windows users to use. 

Plus, now I'm trying to make a "one-click" installation package for Windows users, so they can easily install and run the program without any trouble.

## Installation

See [Installation](./doc/install.md) or [Installation_CN](./doc/install_CN.md) for more details.

## Usage

1. Make sure you have entered the visual environment created in the installation step.
2. Start the server by this command:
```batch
python server.py
```
3. Once you see the message "INFO: Uvicorn running on http://localhost:12393 (Press CTRL+C to quit)" in the console, you need to open browser and go to http://localhost:12393.(Note: you can hold Ctrl and click the link to open it in a new tab)