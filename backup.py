import os
import shutil
import datetime
import schedule
import time

source_dir = "SOURCE DIRECTORY YOU WANNA BACKUP FROM"

destination_dir = "DESTINATION DIRECTORY YOU WANNA BACKUP TO"

def copy_folder_to_directory(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to : {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in : {dest}")    

schedule.every().day.at("23:35").do(lambda: copy_folder_to_directory(source_dir,destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)


