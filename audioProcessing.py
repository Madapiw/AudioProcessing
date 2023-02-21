import librosa as lb
import soundfile as sf
import numpy as np
import fileIO

class AudioProc(fileIO):
    def __init__(self, audioObject):
        self.samplerate = super().samplerate
        self.newaudio = super().audioobj
        self.fourietransofmed = None
        self.audiotempo = lb.feature.tempo(onset_envelope=lb.onset.onset_strength(y=self.newaudio, sr=self.samplerate), sr=self.samplerate)
        
    def trim(self): 
        self.newaudio, index = lb.effects.trim(self.newaudio)
        
    def pshift(self):
        self.newaudio, self.samplerate = lb.load(self.newaudio)
        
        steps = float(input("number of semitones to shift audio file: "))
        
        self.newaudio = lb.effects.pitch_shift(self.newaudio, self.samplerate,steps)
        
    def harmonic(self):
        
        self.newaudio, sr = lb.load(self.newaudio)
        
        self.newaudio = lb.effects.harmonic(self.newaudio)
        
        pass    
    
    def bassboost(self):
        S = lb.stft(self.newaudio)

        magnitude = np.abs(S)
        phase = np.exp(1j*np.angle(S))

        freq = lb.fft_frequencies(self.samplerate, magnitude.shape[0])

        bass_range = (freq >= 20) & (freq <= 20)

        magnitude[bass_range,:]*=10

        D_modified = magnitude*phase

        audio_modified = lb.istft(D_modified)

        self.newaudio = audio_modified



    

        

        
        
        
        
        
    
    