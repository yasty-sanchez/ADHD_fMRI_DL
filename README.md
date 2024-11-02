# ADHD Diagnosis from fMRI Data Using Deep Learning Models

This project explores using deep learning models for classifying ADHD using fMRI data. Implemented using PyTorch, the project uses Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) models to preprocess, train, and evaluate on fMRI data for accurate ADHD diagnosis.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Notebook Structure](#notebook-structure)
- [Data Preprocessing](#data-preprocessing)
- [Model Architecture](#model-architecture)
- [Training and Evaluation](#training-and-evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [References](#references)

---

## Project Overview
This Jupyter Notebook project applies deep learning to identify ADHD patterns in fMRI data from the ADHD-200 dataset. It covers:
1. **Data Loading and Preprocessing**: Standardizing fMRI data for model input.
2. **Model Training**: CNN and CNN-LSTM models, with the option to use pretrained CNN-AE weights for enhanced performance.
3. **Evaluation**: Performance analysis and metrics for accurate ADHD classification.

## Setup Instructions
### Requirements
- Python 3.8+
- Jupyter Notebook
- Install dependencies with:
  ```bash
  pip install -r requirements.txt
  ```
  **Required Libraries**:
  - PyTorch
  - NiBabel
  - NumPy
  - SciPy
  - Matplotlib

### Launching the Notebook
1. Clone this repository and navigate to the project folder.
2. Launch the Jupyter Notebook server:
   ```bash
   jupyter notebook
   ```
3. Open the main notebook (`experiments.ipynb`) and run each cell sequentially to reproduce the analysis.

## Notebook Structure
1. **Introduction and Setup**: Imports necessary libraries, defines helper functions, and initializes settings.
2. **Data Preprocessing**: Loads and preprocesses the fMRI data, converting it into a format suitable for model input.
3. **Model Definitions**: Defines the CNN-AE and CNN-LSTM architectures used for feature extraction and classification.
4. **Training**: Trains both models on the ADHD-200 dataset and logs the results.
5. **Evaluation and Results**: Evaluates model performance using accuracy, precision, recall, and F1-score.

## Data Preprocessing
The preprocessing pipeline includes:
- **Normalization**: Standardizes data to a common scale.
- **Augmentation**: Includes rotation, noise, and intensity shifts to increase data diversity.
- **Tensor Conversion**: Converts fMRI data to PyTorch tensors and resizes as needed for the model.

## Model Architecture

### CNN-Autoencoder (CNN-AE)
A convolutional autoencoder model used to compress high-dimensional fMRI data into a lower-dimensional latent space. It includes:
- **Encoder**: 3D convolutional layers that reduce spatial dimensions progressively.
- **Decoder**: Transpose convolutional layers to reconstruct data from the compressed representation.

### CNN-LSTM
This model combines CNN for spatial feature extraction and LSTM for temporal feature learning. Pretrained CNN weights from the CNN-AE model can be used to initialize the CNN layers for improved performance in ADHD classification.

## Training and Evaluation
- **Training**: The notebook trains models using Mean Squared Error for the CNN-AE and Cross-Entropy Loss for CNN-LSTM. A learning rate scheduler is applied for adaptive learning rates.
- **Evaluation**: Evaluates models with metrics such as accuracy, precision, recall, and F1-score, which are logged and displayed.

## Results
All evaluation metrics are displayed in the notebook for easy interpretation and comparison. The final results include model accuracy, confusion matrices, and any misclassification insights.

## Future Work
Potential areas for improvement include:
- Trying different architectures like Transformers to improve temporal feature capture.
- Enhancing data preprocessing techniques.
- Exploring additional datasets to improve model generalizability.

## References
- ADHD-200 Consortium for providing the ADHD-200 dataset.
- Various studies on CNNs, LSTMs, and autoencoders in neuroimaging.
