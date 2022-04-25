 # 0. About
This is a code repository for the final year project "Evaluation Of Multimodal Subtitle Generator" by Elizabeth Sarell.
The code for the Multimodal Machine Translator (MMT) is provided by Yan Meng and Paulius Staugaitis.
The following documentation describes how to set up the environment and run the translation software.

# 1. Setup
## 1.1 Obtaining the Required Data
The VaTeX dataset should be downloaded from https://vatex.org/main/download.html.

In particular, the following files are needed:
* Training dataset: https://vatex.org/main/data/vatex_training_v1.0.json
* Validation dataset: https://vatex.org/main/data/vatex_validation_v1.0.json
* I3D video features for the training and validation datasets: https://vatex-feats.s3.amazonaws.com/trainval.zip 

JSON files may be renamed to use shorter names, and the video feature archive should be unzipped (caution: there is a
 large number of files in the archive). The values in the included settings files in the `settings` directory provide
 examples of how the directories and files can be structured.

To replicate results described in the final report, the original training dataset should be split into two datasets 
(new training and new test), as detailed in Subsection 3.1 "Experimental Setup" of the report. Although for testing
purposes, any files with the same structure will work.

The filepaths of the datasets should be entered in the settings files, described next.

## 1.2 Configuring the Settings Files
Depending on the environment that the translation system is going to be run in, one or more settings files should
 be configured. 
 
 When using the google collab .ipynb files use the .base file when selecting the parameters.
`settings/base.py` should always be configured, as any other "child settings" files "inherit" from it. If the
 translation system is run on a personal computer, configuring just `settings/base.py` is enough. This settings
 module specifies default values that are used to quickly test whether the code is working correctly while developing
 the system (i.e. not for generating meaningful results). For instance, it only uses 96 sequence pairs for
 training the model instead of the 116955 sequence pairs that `settings/google_cloud.py` uses.
 
A second settings module should be configured if one wants to train the translation system on Google Cloud 
(`settings/google_cloud.py`, Floydhub (`settings/floydhub.py`), or Leeds University HPC cluster (`settings/hpc.py`).
Every settings value can be adjusted as needed. E.g. it's not necessary to always use the full dataset. 



## 1.3 How Settings Modules Work
The reasoning behind using settings modules is provided in Subsection 3.1.1 "Multimodal MT" of the final report.
When the command-line interface is used, one or two settings modules should be specified in the command by setting the
 environment variable `SIMPLE_SETTINGS` to an appropriate value. Specifying no settings modules will result 
 in an error, as the entire system depends on the values inside them.

If two modules are specified, the duplicate values contained in the second module override the values in the first
module. For example, the value `TRAINING_SEQUENCE_PAIRS_LIMIT = 116955` in `settings/google_cloud.py` would override
the value `TRAINING_SEQUENCE_PAIRS_LIMIT = 96` in `settings/base.py` when the following command is used:
`SIMPLE_SETTINGS=settings.base,settings.google_cloud python run.py preprocess`

The following examples illustrate this:
```
# 1) Run the script on a personal computer 
SIMPLE_SETTINGS=settings.base python run.py preprocess
# 2) Run the script on Google Cloud
SIMPLE_SETTINGS=settings.base,settings.google_cloud python run.py preprocess
```
The first command starts the model training process on a personal computer, using values from `settings/base.py`.
The second command starts the model training process on Google Cloud, using a combination of values from both 
`settings/base.py` and `settings/google_cloud.py`

The above command format is suitable to be used when the current working directory is the base directory of the
project (i.e.the directory that contains the `run.py` file).

## 1.4 Setting up the Virtual Environment
Python 3.6.8 and pip 20.1 was used during the development. It is recommended to use the same Python version.

First, a new virtual environment should be created:
```
python3 -m venv <myenvname>
```

The new virtual environment should then be activated:
```
source myenvname/bin/activate
```

Finally, the required packages should be installed:
```
pip install -r requirements.txt
```

# 2. Running the Software
The piplines to run the MMT system is already set up in the "MMT_Training.Pipline.ipynb" file. If this is opened in google collab where it was developed, just follow through the installation and set up guide and it should train and then test the sysetm. 

After the set-up is completed, `run.py` can be used to run the translation system.
The boolean variable `USE_VIDEO_EMBEDDINGS` in the settings determines whether **NMT-1** or **VMT-1** is run.

The examples that follow use the `settings/base.py` module but they can be modified for different environments,
as described above. Sample arguments are used in the examples (test batch at index 0 is chosen).

The help page for each command choice (see 2.1.2) provides more details about its parameters.

## 2.1. Displaying CLI Help
### 2.1.1. General Help
```
SIMPLE_SETTINGS=settings.base python run.py --help
```
### 2.1.2. Command-Specific Help

```
# Replace "train" with the relevant command
SIMPLE_SETTINGS=settings.base python run.py train --help
```


## 2.2. Pre-processing Data
```
SIMPLE_SETTINGS=settings.base python run.py preprocess
```

## 2.3. Training Model
```
SIMPLE_SETTINGS=settings.base python run.py train
```

## 2.4. Testing Translation Quality
Change the file path to point to your trained model
```
SIMPLE_SETTINGS=settings.base python run.py translate_test_dataset -m /home/paul/PycharmProjects/fyp/saved/2020-05-04_0022/model-04_3.231.hdf5
```
# 3 Other MT Model
Along side the MMT model this system tested two Machine Translation (MT) system which only used text whilst translating. 

## 3.1 NV-MT
To run the NV-MT system simply go into the base.py file and change the paramater "USE_VIDEO_EMBEDDINGS" to False.

## 3.2 BMT
Another system was implemented using the Hugging Face Pipline. This pipline is set up in the "Quality_Estimation.ipynb".


# 4 Quality Estimation System
Load the "Quality_Estimation.ipynb" file in google collab. There it will show all the relevant steps to use the TransQuest System.
There are two levels of evaluating. Sentence Level and Word Level. They are have both been clearly lined out with the MonoTransQuest System being used by the Sentence Level and the MicroTransQuest System being used by the Word Level.
Both system with output the data in a csv file. The sentence level, produces a score between 0 and 1 for each sentence, with 1 being the best and 0 the worst. 
The word level, produces a string of "OK" and "BAD"'s for each word and space in the sentence.



