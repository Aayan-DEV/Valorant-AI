# Valorant-AI
This is a personal project for my school about a Valorant AI helper. 
Read the about and instructions for more details.
Those places are in the Program.

The hardware Requirements are: 
 - Good Nvidea Graphics card.
 - 16Gb Ram
 - Windows (As valorant isn't on Linux or MacOS)
 - Screen Resolution 1920x1080

To run the program the requirements are:
- The folders and files in the Github repository.
- Python version 3.9 (Newer versions will not work) > You can find it [Here](https://www.python.org/downloads/release/python-390/)
- Cuda 11.7 > You can find it [Here](https://developer.nvidia.com/cuda-11-7-0-download-archive)
- Git > You can find it [Here](https://git-scm.com/downloads)
- Pytorch 
  - First, go [Here](https://pytorch.org/)
  - Then select **Windows**
  - Select **Pip**
  - Select **Python**
  - Select **Cuda 11.7** 
  - Then copy the command and paste it into the terminal/CMD, which is being directed to your folder. 
  - Or just use this command and skip the steps: <br /> `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117`
- Yolov5 folder 
    - After making sure the above requirements, go to --> https://github.com/ultralytics/yolov5
    - Then clone this to your python main directory (where all the folders are located)
    - Use this code: <br />
    `git clone https://github.com/ultralytics/yolov5`
 - Tesseract-OCR folder
    - Now go [Here](https://github.com/UB-Mannheim/tesseract/wiki) 
    - Select and install 64 bit version. 
    - Put the install destination to your Valorant-AI-master folder > Valorant-AI-master\Tesseract-OCR

How to run the program:
- After installing everything, just locate your Valorant-AI-master folder in cmd.
- Then type in `python main.py`
- And then it will run, and you can go and choose any option and run the program.
