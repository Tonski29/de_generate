import sys
import random
from db.SQLite import init_db, EvidenceFile, Session, seed_db, Scenario, EvidenceWebDownload
import subprocess
from modules.files import File
from lib.fs import download_file
from settings import *



def init():

    init_db()
    rc = subprocess.call("./users/mkusers.sh")
    copy_rc = subprocess.call("/bin/cp ./av_logs/* /var/log/", shell=True)  #  files for antivirus scan are copied here
    print("db/users created")


# random num gen
def get_index(files_length, affected):
    rand_index = random.randint(0, files_length -1)
    while rand_index in affected:
        rand_index = random.randint(0, files_length)
    return rand_index


def generate_files(session, scenario_id):
    murder_scenario = session.query(Scenario).filter_by(name="murder").first()

    # Get all files related to scenario make list tof file objects with the rel data  every file entry from db  scen
    files = [File(file.file_path, file.contents) for file in
             session.query(EvidenceFile).filter_by(scenario=scenario_id).all()]

    # Find out how many files there are, used for generating a random index
    files_length = len(files)
    affected = []

    # Download a file to a specified location
    # download_file("https:", HOME_DIR+".pdf")
    # get index generates number using filelenght aka no of files affected= already used
    for i in range(HIDE_NUM):
        index = get_index(files_length, affected)
        files[index].hidden = True
        affected.append(index)
    for i in range(DELETE_NUM):
        index = get_index(files_length, affected)
        files[index].delete = True
        affected.append(index)  # makes sure the same file isnt affected twice
    for i in range(ENCRYPT_NUM):
        index = get_index(files_length, affected)
        files[index].encrypt = True  # files = index list of all files
        affected.append(index)

    for file in files:
         file.run()  # loops through all files and then depending on the object properties,generated in files
        # Getting Scenario from db by name


def download_evidence_files(session, scenario_id):
    downloads = [(download.file_path, download.url) for download in session.query(EvidenceWebDownload).filter_by(scenario=scenario_id).all()]
    for download in downloads:
        download_file_path = download[0]
        download_url = download[1]
        download_file(download_url, download_file_path)


#start of script below -----------------------------------------------------------------------
if __name__ == "__main__":
    init()
    scenario_id = 1
    if len(sys.argv) > 1:
        if sys.argv[1] == "seed":
            seed_db()
    session = Session()

    generate_files(session, scenario_id)
    download_evidence_files(session, scenario_id)





