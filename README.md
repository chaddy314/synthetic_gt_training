# Synthetic GT Training
This Tool provides a simple workflow to train models for [Calamari-OCR](https://github.com/Calamari-OCR) using synthetically generated Ground Truth Data including using the trained models as Pre-Training model for the next one. It also provides automatic prediction and evaluation for all generated models.

## Installation
Unfortunately this tool uses other non-replacable tools which have conflicting packages. Therefore one has to install at least one virtual environment for Calamari-OCR and it is recommended to use one for TRDG. The requirements for the latter can be found in this repository.
If you want to use a different Virtual Environment Tool other than `venv` you have to edit the `bash` file to fully take use of it.

## Usage
Before running the tool you have to configure the `json` file. Two examples are given in this repository. Make sure that every source folder/file exists and the path to den `venv` executable is set.

To then execute the specified workflow you simply run ```bash run.sh /path/to/json```.

## Requirements
Tensorflow is recommended to really get a use out of this tool.
Make sure to have enough disk space freed up as, depending on the number of generated lines, the generated data gets quite large.

## Evaluation
At this time only PageXML data can be used for evaluating different models.

## Data
Be sure to check out [CC-100](https://data.statmt.org/cc-100/) if you cant find any suitable text data.
