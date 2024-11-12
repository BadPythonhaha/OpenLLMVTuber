# Installation
[CN](./install_CN.md)

If you are planning to install manually, it is recommended to use Anaconda or Miniconda to create a virtual environment.
**This tutorial assumes that you have Anaconda or Miniconda installed.**
**Before you start, make sure that you have Git installed on your system.**

1. Clone the repository:
```batch
git clone https://github.com/BadPythonhaha/OpenLLMVTuber.git
```
2. Create a new virtual environment based on Python 3.11.10:
```batch
conda create -n <Environment Name> python=3.11.10
```
You can replace `<Environment Name>` with any name you want.
For Anaconda, you can opreate it in the Anaconda Navigator too.

3. Activate the virtual environment:
```batch
conda activate <Environment Name>
```
4. Switch to the repository directory:
```batch
cd OpenLLMVTuber
```
5. Install the required packages:
```batch
pip install -r requirements.txt
```
6. Install the MeloTTS module:
For some reason, the MeloTTS module is not available on PyPI, so you need to install it manually. I've put the MeloTTS module in the `external` folder, so you can install it by running:
```batch
cd external\MeloTTS
pip install -e .
python -m unidic download
```
If you have network troubles on downloading the unidic dictionary, you may need to set proxy for console and try again, by running:
```batch
set http_proxy=<proxy>:<port>
set https_proxy=<proxy>:<port>
python -m unidic download
```
Normally, the `<proxy>:<port>` is `127.0.0.1:7890`, but you better check it in settings.

## Notice
This is a work in progress, so there may be some bugs or issues. You can report them in the Issues section of the repository, but it is still recommended to serach for solutions on the internet before asking for help.