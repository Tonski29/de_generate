from lib.fs import create_file, delete_file
from lib.crypt import aes_encrypt

class File:
    def __init__(self, file_path, contents): #for every evdfile used an object is created
        self.file_path = file_path
        self.contents = contents
        self.hidden = False
        self.delete = False
        self.encrypt = False

    # an instance this calss allows for creatuion of files file path aswell as its contents are passed and initially th
    #it alos dtermines how the files are when created
    def run(self):
        mode = 'w'
        if self.hidden:
            path_parts = self.file_path.split("/")
            file_name = "." + "".join(path_parts[-1:])
            path_parts[-1:] = ""
            path_parts.append(file_name)
            self.file_path = "/".join(path_parts)
            print("[+] Creating hidden file %s" % self.file_path)

        elif self.encrypt:
            passphrase = "testing"
            self.contents = aes_encrypt(self.contents, passphrase)
            print(self.contents)
            self.file_path = self.file_path + ".gpg"
            print("[+] Creating encrypted file %s" % self.file_path)


        create_file(self.file_path, self.contents, mode=mode)

        if self.delete:
            delete_file(self.file_path)
            print("[+] Deleting file %s" % self.file_path)

