import dropbox

class TransferData:
    def _init_ (self,access_token):
        self.access_token
        
    def upload(self, TakeFile, ToFile):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(TakeFile, 'rb')
        dbx.FileTale(f.read(), ToFile)
        
def main():
    access_token = 'sl.BBqI9JYQSfJ-iLJgAPp428SUai8Z7loOb4NiHScJ8cBOy5QsaTo5vPtkrX476Zy7sNfVoAGwAo_xcWDD-kGlzC3Suc5h1JzsPyslv16-d1ho9GPBxCv_mLQNAHKNKEv_6VM1_V0'
    SendData = TransferData(access_token)
    
    TakeFile = input("Please enter file path: ")
    ToFile = input("Please enter path to send to cloud 🌥 ")
    
    SendData.upload_file(Takefile, Tofile)
    print("✉")
    print("File is sent   ")
main()
