# EEG Blocks Documentation

Documentaion guide to all the pre-implemented EEG signal processing and classification blocks.

## Table of Content

* [Data Provider](#data-provider)
    * [Offline Data Provider](#offline-data-provider)
* [Pre Processing](#pre-processing)
    * [Channel Selection](#channel-selection)
    * [Channel Names](#channel-names)
    * [Epoch Extraction](#epoch-extraction)
    * [Epoch averaging](#epoch-averaging)
    * [Filter](#filter)
    * [Event and Ids](#event-and-ids)
* [Feature Extraction](#feature-extraction)
    * [Wavelet Transform](#wavelet-transform)
    * [Feature Labeling](#feature-labeling)
* [Classification](#classification)
    * [Neural Network Layer](#neural-network-layer)
    * [Neural Network Classifier](#neural-network-classifier)
    * [Save Model](#save-model)
* [Visualization](#visualization)
    * [EEG Plot](#eeg-plot)
    * [Epoch Plot](#epoch-plot)


## Data Provider

### Offline Data Provider
Offline Data Provider block is for importing the .eeg extenstion files to the workflow. The .eeg exntension files are total 3 in number:
- <filename>.eeg
- <filename>.vhdr
- <filename>.vmrk
Note it does not allow any other EEG signal file extensions/types. 
<div id="container" style="white-space:nowrap">
    <div id="image" style="display:inline;" >
        <img src="assets/EEG_blocks/dataprovider/offline1.png" width="400" height="250"/>
    </div>
    <div id="image" style="display:inline;">
        <img src="assets/EEG_blocks/dataprovider/offline2.png" width="400" height="250"/>
    </div>
</div>

## Pre Processing





