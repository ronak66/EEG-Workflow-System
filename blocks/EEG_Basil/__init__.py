from .DataProvider.OfflineDataProvider import OfflineDataProvider

from .PreProcessing.ChannelSelection import ChannelSelection
from .PreProcessing.ChannelNames import ChannelNames
from .PreProcessing.EventAndIds import EventAndIds
from .PreProcessing.EpochExtraction import EpochExtraction
from .PreProcessing.Filter import Filter
from .PreProcessing.EpochAveraging import EpochAveraging

from .FeatureExtraction.WaveletTransform import WaveletTransform
from .FeatureExtraction.FeatureLabeling import FeatureLabeling

from .Classification.SaveModel import SaveModel
from .Classification.NeuralNetworkLayer import NeuralNetworkLayer
from .Classification.NeuralNetworkClassifier import NeuralNetworkClassifier

from .Visualization.EpochPlot import EpochPlot
from .Visualization.EEGPlot import EEGPlot

string_classobject_mapping = {
    OfflineDataProvider.name: OfflineDataProvider(),
    ChannelSelection.name: ChannelSelection(),
    ChannelNames.name: ChannelNames(),
    EventAndIds.name: EventAndIds(),
    EpochExtraction.name: EpochExtraction(),
    EpochAveraging.name: EpochAveraging(),
    Filter.name: Filter(),
    WaveletTransform.name: WaveletTransform(),
    FeatureLabeling.name: FeatureLabeling(),
    SaveModel.name: SaveModel(),
    NeuralNetworkLayer.name: NeuralNetworkLayer(),
    NeuralNetworkClassifier.name: NeuralNetworkClassifier(),
    EpochPlot.name: EpochPlot(),
    EEGPlot.name: EEGPlot()
}