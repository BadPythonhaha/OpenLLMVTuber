以下是Markdown文件的核心内容翻译成中文：

# Open-LLM-VTuber Modified
![GitHub License](https://img.shields.io/github/license/BadPythonhaha/OpenLLMVTuber)

[EN](README.md)
[原项目的README](./doc/README_Original.md)

## 这是什么？

这是一个修改版的[Open-LLM-VTuber](https://github.com/t41372/Open-LLM-VTuber)，仅使用Ollama、FunASR和MeloTTS作为主要组件。旨在为在本地机器上创建和运行VTuber提供一个更轻量级、更易于使用的解决方案，并尝试使Windows用户更容易使用。

此外，我现在正在尝试为Windows用户制作一个“一键”安装包，以便他们可以轻松安装并运行程序，而不会遇到任何麻烦。

## 安装

更多详情请参阅[安装教程英文版](./doc/install.md)或[中文版](./doc/install_CN.md)。

## 使用方法

1. 确保你已经进入了安装步骤中创建的视觉环境。
2. 通过以下命令启动服务器：
```batch
python server.py
```
3. 当你在控制台看到消息“INFO: Uvicorn running on http://localhost:12393 (Press CTRL+C to quit)”时，你需要打开浏览器并访问http://localhost:12393。
（注意：你可以按住Ctrl并点击链接在新标签页中打开它）
4. 当你看到浏览器中的live2d模型时，尽情聊天吧。

## 致谢

- [Open-LLM-VTuber](https://github.com/t41372/Open-LLM-VTuber)
- [Ollama](https://github.com/ollama/ollama)
- [FunASR](https://github.com/modelscope/FunASR)
- [MeloTTS](https://github.com/myshell-ai/MeloTTS)
