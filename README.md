# Smoker Classifier

Smoking persons classification using pretrained ResNet50

## Overview
This project uses a pretrained ResNet model to classify images of smokers. 

From images to probabilities of smoking persons in them:

* prob: 0.02

  <img width="252" alt="image" src="https://github.com/user-attachments/assets/aa629c36-15bf-42b2-94c2-10b7ff25bff3">

* prob: 0.78

  <img width="247" alt="image" src="https://github.com/user-attachments/assets/13b5c12e-bed4-4863-a5f0-1a143e290f17">


Team 8:
* Svetlana Lukina
* Lyudmila Zavadskaya
* Pavel Gurevich
* Nikita Vybornov
  

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
1. Run tests:
   ```bash
   python -m unittest test_main_model.py
   ```

2. **To Prerocess data:**
   ```bash
   make Preprocessing
   ```

3. **To Process data:**
   ```bash
   make Processing
   ```
   Runs the neural network model on the images.

4. **To Postprocess data:**
   ```bash
   make Postprocessing
   ```
  Analyzes the output from the neural network 
