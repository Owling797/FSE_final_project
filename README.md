# Smoker Classifier

Smoking persons classification using pretrained ResNet50

By team 8:
* Svetlana Lukina
* Lyudmila Zavadskaya
* Pavel Gurevich
* Nikita Vybornov
## Overview
This project uses a pretrained ResNet model to classify images of smokers. 

From images to probabilities of smoking persons:

* prob: 0.02

  <img width="252" alt="image" src="https://github.com/user-attachments/assets/aa629c36-15bf-42b2-94c2-10b7ff25bff3">

* prob: 0.78

  <img width="247" alt="image" src="https://github.com/user-attachments/assets/13b5c12e-bed4-4863-a5f0-1a143e290f17">
  

## Requirements
- Python 3.9
- torch
- torchvision
- Pillow

## Setup Instruction

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Owling797/FSE_final_project.git
   git checkout main
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd FSE_final_project
   ```

3. **Place your images into 'images' directory:**

4. **Build the Docker Image:**
   ```bash
   docker build -t clasdss .
   ```
   <img width="862" alt="image" src="https://github.com/user-attachments/assets/ec5d2bd2-0af7-4e66-a9fe-e3ce96ba4398">


5. **Run the Docker Container:**
   Check where the FSE_final_project is located
   ```bash
   docker run -it -v <Your full path to FSE_final_project>/FSE_final_project/out/:/app/out/  clasdss
   ```
   <img width="993" alt="image" src="https://github.com/user-attachments/assets/668a42b8-2aae-4c02-a547-92356a3677eb">


6. **Check the result in the 'out' directory**
   ```bash
   cat out/out.txt
   ```
   <img width="482" alt="image" src="https://github.com/user-attachments/assets/aab77d1b-88ff-4902-b002-c0725b24bcfb">



## Auxilary options

1. **To Prerocess data:**

All paths must be relative to directory entrypoint
   ```bash
   make preprocessing input=<path to your image> output=<path to the result>
   ```
   or outside the container:
   ```bash
   docker run -it clasdss preprocessing input=<path to your image> output=<path to the result>
   ``` 
   ![alt text](screenshots/image-2.png)


2. **To Process data:**
   ```bash
   make processing
   ```
   or outside the container:
   ```bash
   docker run -it clasdss processing 
   ``` 
   ![alt text](screenshots/image-3.png)
   Runs the neural network model on the images.

3. **To Postprocess data:**
   ```bash
   make postprocessing input=<path to the model output (.pkl)> output=<path to the result (.json)>
   ```
   or outside the container:
   ```bash
   docker run -it clasdss postprocessing input=<path to the model output (.pkl)> output=<path to the result (.json)>
   ```
   ![alt text](screenshots/image-4.png)
  Analyzes the output from the neural network 

4. **Run tests**:
   ```bash
   python -m unittest test_main_model.py
   ```
   ![alt text](screenshots/image-1.png)