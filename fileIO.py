import librosa as lb
import soundfile as sf

class fileIO:
    def __init__(self, filepath, savepath: None) -> None:
        self.filepath = filepath
        self.fileextension = filepath.split(".")[-1:]
        self.savepath = savepath
        self.audioobj = None
        self.samplerate = None
        
    def loadFile(self):
        if lb.util.valid_audio(self.filepath):
            self.audioobj, self.samplerate = sf.read(self.filepath)
        else:
            return Exception("Bad file")
    
    def saveFile(self, objtosave, savepath, savesamplerate: None):
        fileext = savepath.split(".")[-1]
        if savesamplerate != None:
            return sf.write(savepath, objtosave, savesamplerate)
        else:
            return sf.write(savepath, objtosave, self.samplerate)
        
    def getAudioObj(self):
        return self.audioobj
    
    def getFilePath(self):
        return self.filepath

    def getSamplerate(self):
        return self.samplerate
    
    def setSamplerate(self, sr):
        self.samplerate = sr

    
    
    
    
