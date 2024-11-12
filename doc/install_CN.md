# 安装指南
[EN](./install.md)

如果你打算手动安装，建议使用Anaconda或Miniconda来创建虚拟环境。
**本教程假设你已经安装了 Git 和 Anaconda或Miniconda**


1. 克隆仓库：
```batch
git clone https://github.com/BadPythonhaha/OpenLLMVTuber.git
```
2. 创建一个基于Python 3.11.10的虚拟环境：
```batch
conda create -n <环境名称> python=3.11.10
```
你可以将`<环境名称>`替换为你想要的任何名称。
对于Anaconda，你也可以在Anaconda Navigator中操作。

3. 激活虚拟环境：
```batch
conda activate <环境名称>
```
4. 切换到仓库目录：
```batch
cd OpenLLMVTuber
```
5. 安装所需的包：
```batch
pip install -r requirements.txt
```
6. 安装MeloTTS模块：
由于某些原因，MeloTTS模块不在PyPI上，因此需要手动安装。我已经将MeloTTS模块放在`external`文件夹中，你可以通过运行以下命令来安装它：
```batch
cd external\MeloTTS
pip install -e .
python -m unidic download
```
如果你在下载unidic词典时遇到网络问题，你可能需要为控制台设置代理并再次尝试，运行：
```batch
set http_proxy=<代理>:<端口>
set https_proxy=<代理>:<端口>
python -m unidic download
```
通常，`<代理>:<端口>`是`127.0.0.1:7890`，但你最好在设置中检查一下。

7. 使用Ollama下载语言模型：
```batch
ollama pull <模型名称>
```
你可以用任何在[Ollama模型库](https://ollama.com/library)中的模型名称替换`<模型名称>`，在这个修改过的项目中，以`llama3.2:latest`为默认模型，你仍然可以用其他模型替换它，但不要忘记修改`config.yaml`中的模型名称。所以如果你不想更改，使用以下命令下载:
```batch
ollama pull llama3.2:latest
```
## 注意事项
这是一个正在进行中的工作，可能存在一些错误或问题。你可以在仓库的Issues部分报告它们，但在寻求帮助之前，建议在互联网上搜索解决方案。
或者，等待正在开发中的一键包。