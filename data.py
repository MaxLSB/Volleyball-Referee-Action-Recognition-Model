import os
import shutil
import time
import mediapipe as mp
import utils.dataCollection as dataCollection
from utils.actions import all_actions_training
from utils.config import get_paremeters

# Collect data though webcam for each action, save everythin in the dedicated folders !

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

DATA_PATH = get_paremeters()['DATA_PATH']
actions = all_actions_training() # Actions that we try to detect
no_sequences = get_paremeters()['no_sequences'] # Thirty videos worth of data
sequence_length = get_paremeters()['sequence_length'] # Videos are going to be 30 frames in length
start_folder = get_paremeters()['start_folder'] # Folder start

# Check if the folder already exists
if os.path.isdir(DATA_PATH):
    print("The Data folder already exists.")
    user_input = input("Do you want to delete the folder in order to create a new one? (yes/no): ").strip().lower()

    if user_input in ["yes", "y"]:
        # Delete the folder and all its contents
        
        shutil.rmtree(DATA_PATH)
        print("The folder and all its contents have been deleted.")
        os.makedirs(DATA_PATH)
        for i in range(len(actions)):
            os.makedirs(os.path.join(DATA_PATH, actions[i]))
        print("New folder has been created.")
        time.sleep(1)
        
        dataCollection.data_collection(actions, DATA_PATH, no_sequences, sequence_length, start_folder)
    
    elif user_input in ["no", "n"]:
        print("The folder has been kept.")
    else:
        print("Invalid response. No action has been taken.")
else:
    # Create the folder if it does not exist
    os.makedirs(DATA_PATH)
    for i in range(len(actions)):
            os.makedirs(os.path.join(DATA_PATH, actions[i]))
    print(f"The folder has been created.")
    time.sleep(1)
    
    dataCollection.data_collection(actions, DATA_PATH, no_sequences, sequence_length, start_folder)

