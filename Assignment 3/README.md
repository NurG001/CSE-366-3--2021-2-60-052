# Computer Vision: Image Classification with Custom CNN and DenseNet121

This repository contains the implementation of two deep learning models for image classification: a Custom Convolutional Neural Network (CNN) and DenseNet121. The models are trained and evaluated on a dataset from Mendeley Data, which includes various images classified of coffee leafs into different categories.

## Overview

This project involves developing and training two different models for image classification. The main steps are:

1. **Data Preprocessing:** Load and preprocess the dataset, including data augmentation and normalization.
2. **Model Implementation:** Define and compile a Custom CNN model and a DenseNet121 model.
3. **Training:** Train both models using the preprocessed dataset, with early stopping and checkpointing to prevent overfitting.
4. **Evaluation:** Evaluate the models based on accuracy and loss, and visualize the results.
5. **Visualization:** Display predictions to understand model performance.

The goal is to compare the performance of the `Custom CNN` and `DenseNet121` models and identify the strengths and weaknesses of each.

## Dataset

The dataset used for this assignment can be accessed at [Mendeley Data](https://data.mendeley.com/datasets/brfgw46wzb/1). It contains multiple images classified into different categories.

## Data Preprocessing
The dataset is loaded and preprocessed using TensorFlow's image_dataset_from_directory function. Data augmentation techniques such as random horizontal flip, rotation, and zoom are applied to the training dataset. Images are also normalized to a range of [0, 1].

## Models
- `Custom CNN Model`: 
A custom CNN model is defined with multiple convolutional layers, max-pooling layers, and dense layers. The architecture is designed to be simple yet effective for image classification tasks.

- `DenseNet121 Model`: 
DenseNet121 is a pre-trained model known for its efficiency and ability to handle complex image classification tasks. In this implementation, the DenseNet121 model is modified to fit the current dataset by adding custom dense layers on top.

### Training
Both models are trained using the Adam optimizer and sparse categorical cross-entropy loss. Early stopping and model checkpointing are used to prevent overfitting and save the best model weights.

### Evaluation
The models are evaluated based on accuracy and loss on the validation dataset. The results are visualized using Matplotlib to show the training and validation accuracy over epochs.


## Requirements

To run the code, you will need the following libraries:
- TensorFlow
- Matplotlib
- NumPy

## Files
- `Computer_Vision_Assignment_Report.ipynb`: This notebook contains the implementation of the Custom CNN model and MobileNetV2. It includes data preprocessing, model training, evaluation, and visualization of results.
- `Computer_Vision_Assignment_Report_Report.pdf`: This is the detailed report of the assignment, summarizing the approach, methodology, results, and conclusions.
- `README.md`: This document provides a quick overview of the project and instructions on how to use the notebook.

## You'll Need
- Kaggle, Google Colab or Jupyter Notebook
- Python libraries: TensorFlow, matplotlib, numpy

## How to Use

1. **Open the Notebook**: Launch the `Computer_Vision_Assignment.ipynb` file in Kaggle or Jupyter Notebook.
2. **Load Dataset**: Ensure the dataset is accessible and update the dataset path in the notebook accordingly.
3. **Run the Notebook**: Execute the cells in the notebook sequentially to preprocess the data, train the models, and evaluate their performance.
4. **Choose Models**: The notebook includes implementations for both the Custom CNN and DenseNet121 models. You can execute and compare both.
5. **Visualization**: The notebook contains code to visualize training accuracy, validation accuracy, and predictions. Execute those cells to create these visualizations.
6. **Read the Report**: For an in-depth explanation of the methodology, results, and conclusions, refer to the `Computer_Vision_Assignment_Report.pdf`.


You can install the required libraries using pip:

```bash
pip install tensorflow matplotlib numpy
