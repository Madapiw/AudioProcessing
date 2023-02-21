import librosa

class Proc:
    
    def __init__(self,filetaken):
        
        self.filetaken = filetaken
        
    def trim(filetaken):
        
        y, sr = librosa.load(filetaken)
        
        yt, index = librosa.effects.trim(y)
        
        yt_trim = yt
        
        filetaken = yt_trim
        
    def pshift(filetaken):
        
        y,sr = librosa.load(filetaken)
        
        steps = float(input("number of semitones to shift audio file: "))
        
        new_y = librosa.effects.pitch_shift(y,sr,steps)
        
        soundfile.write("{filetaken}.wav",new_y,sr,)
        
    def harmonic(filetaken,margin):
        
        y, sr = librosa.load(filetaken)
        
        y_harmonic = librosa.effects.harmonic(y)
        
        y_harmonic
        
        
        
        
        
    
    