from .DataProvider.OfflineDataProvider import OfflineDataProvider

from .PreProcessing.ChannelSelection import ChannelSelection
from .PreProcessing.ChannelNames import ChannelNames
from .PreProcessing.EventAndIds import EventAndIds
from .PreProcessing.EpochExtraction import EpochExtraction

from .FeatureExtraction.WaveletTransform import WaveletTransform

from .Classification.NeuralNetworkLayer import NeuralNetworkLayer
from .Classification.NeuralNetworkClassifier import NeuralNetworkClassifier

from .Visualization.EEGPlot import EEGPlot

string_classobject_mapping = {
    OfflineDataProvider.name: OfflineDataProvider(),
    ChannelSelection.name: ChannelSelection(),
    ChannelNames.name: ChannelNames(),
    EventAndIds.name: EventAndIds(),
    EpochExtraction.name: EpochExtraction(),
    WaveletTransform.name: WaveletTransform(),
    NeuralNetworkLayer.name: NeuralNetworkLayer(),
    NeuralNetworkClassifier.name: NeuralNetworkClassifier(),
    EEGPlot.name: EEGPlot()
}