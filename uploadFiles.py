from os import access
import dropbox

class TransferData:
    def __init__(self,access_Token):
        self.access_Token=access_Token

    def uploadFiles(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_Token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_Token="3R8OINiphSwAAAAAAAAAAUofLEP0cQvc_HfphYnPFhQBXIIJ1jwuEjISiD2g2JGZ"
    transferData=TransferData(access_Token)

    files_From=input("Enter from where do you want to upload the file")
    files_To=input("To where do you want to upload: ")

    transferData.uploadFiles(files_From,files_To)

main()