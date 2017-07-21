# CNTK Examples: Image/Detection/Faster R-CNN

## Overview

This folder contains an end-to-end solution for using Faster R-CNN to perform object detection. 
Base models that are supported by the contained configuration are AlexNet and VGG16. 
Two image set that are preconfigured are Pascal VOC 2007 and Grocery. 
Other base models or image sets can be used by adapting config.py.

## Running the example

### Getting the data and AlexNet model

we use a toy dataset of images captured from a refrigerator to demonstrate Faster R-CNN. Both the dataset and the pre-trained AlexNet model can be downloaded by running the following Python command:

`python install_data-and-model.py`

After running the script, the toy dataset will be installed under the `Image/DataSets/Grocery` folder. And the AlexNet model will be downloaded to the `Image/PretrainedModels` folder. 
We recommend you to keep the downloaded data in the respective folder while downloading, as the configuration files in this folder assumes that by default.

### Running Faster R-CNN training and evaluation

To train and evaluate Faster R-CNN run 

`python FasterRCNN.py`

The results for end-to-end training on Grocery using AlexNet as the base model should look similar to these:

```
AP for          eggBox = 1.0000
AP for          tomato = 1.0000
AP for     orangeJuice = 1.0000
AP for         ketchup = 0.6667
AP for         mustard = 1.0000
AP for           water = 0.5000
AP for       champagne = 1.0000
AP for         joghurt = 1.0000
AP for          pepper = 1.0000
AP for         avocado = 1.0000
AP for           onion = 1.0000
AP for         tabasco = 1.0000
AP for            milk = 1.0000
AP for          orange = 1.0000
AP for          gerkin = 1.0000
AP for          butter = 1.0000
Mean AP = 0.9479
```

All options and parameters are in `config.py`. These include

```
__C.CNTK.DATASET = "Grocery"    # "Grocery" or "Pascal"
__C.CNTK.BASE_MODEL = "AlexNet" # "VGG16" or "AlexNet"

__C.CNTK.TRAIN_E2E = True       # E2E or 4-stage training

__C.CNTK.E2E_MAX_EPOCHS = 20
__C.CNTK.E2E_LR_PER_SAMPLE = [0.001] * 10 + [0.0001] * 10 + [0.00001]
```

