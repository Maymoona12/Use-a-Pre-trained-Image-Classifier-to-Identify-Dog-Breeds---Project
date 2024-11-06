# Dog Breed Image Classifier Project

## Project Overview
This project utilizes a pre-trained image classification model to identify dog breeds, designed to support registration for a citywide dog show by ensuring only dog images are classified. It also includes functionality to distinguish between various dog breeds and filter out non-dog images submitted by participants. The goal is to utilize an existing deep learning image classifier in Python, specifically focusing on using models from the ImageNet dataset.

The classifier will be evaluated on three main Convolutional Neural Network (CNN) architectures:
- **AlexNet**
- **VGG**
- **ResNet**

Each architecture will be assessed for:
1. Accuracy in identifying dog images vs. non-dog images.
2. Accuracy in identifying specific dog breeds.
3. Computational time required for processing.

## Key Objectives
1. **Identify if the image is of a dog**: Ensure images are correctly classified as either "dog" or "not dog" to filter entries.
2. **Classify Dog Breeds**: For images classified as "dogs," identify the breed of the dog.
3. **Compare CNN Architectures**: Determine which model architecture (ResNet, AlexNet, or VGG) achieves the best results for the tasks.
4. **Evaluate Computational Efficiency**: Measure runtime to find a balance between accuracy and computational efficiency.
