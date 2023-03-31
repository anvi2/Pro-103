import time
import os
import shutil
import random
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/anvit/Downloads'
to_dir = 'C:/Users/anvit/OneDrive/Desktop'

dir_tree = {
    "Image_files" : ['.png' , '.jpg' , '.jpeg' ,'.gif' , '.jfif' ],
    "video_files" : ['.mpg' , '.mp2' , '.mpeg' , '.mpe' , '.mp4' , '.mpv' , '.m4p' , '.m4v' , '.mov' , '.avi'],
    "document_files" : ['.pdf' , '.doc' , '.docx' , '.ppt' , '.txt' , '.xls' , '.csv'],
    "setup_files" : ['.exe' , '.cmd' , '.bin' , '.dmg' , '.msi']
}

class FileEventHandler(FileSystemEventHandler):
 def on_created(self, event):
    print(f"Hey , {event.src_path} has been created.")

 def on_deleted(self, event):
    print(f"Oops!something deleted{event.src_path}.")

 def on_modified(self, event):
   print(f"Hey , {event.src_path} has been modified.")

 
   name , extension = os.path.splitext(event.src_path)

   for key , value in dir_tree.items():
     if extension in value:
       fileName = os.path.basename(event.src_path)

       path1 = from_dir + "/" + fileName
       path2 = to_dir + "/" + key
       path3 = to_dir + "/" + key + "/" + fileName

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler , from_dir , recursive= True)
observer.start()

try:
  while True:
    time.sleep(1)
    print("running")
except KeyboardInterrupt:
  print("stop")
  observer.stopped()  
  

