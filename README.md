# Smoker Classifier

Smoking persons classification using pretrained ResNet50

## Overview
This project uses a pretrained ResNet model to classify images of smokers. 


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

5. **Run the Docker Container:**
   Check where the FSE_final_project is located
   ```bash
   docker run -it -v <Your full path to FSE_final_project>/FSE_final_project/out/:/app/out/  clasdss
   ```

6. **Check the result in the 'out' directory**

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
