import audioProcessing
import librosa as lb
import numpy as np

class audioEqualizer(audioProcessing):
    def __init__(self) -> None:
        super().__init__()
        self.outputaudio = None
        
    def bassboost(self):
        