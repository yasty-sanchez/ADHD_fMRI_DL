import os
import shutil

# Paths to ADHD, TDC, and non-rest directories
target_dir = os.path.join('preprocessed')
non_rest_dir = os.path.join(target_dir, 'non_rest')

# Create the non_rest directory if it doesn’t exist
os.makedirs(non_rest_dir, exist_ok=True)

# Loop through ADHD and TDC folders
for diagnosis_folder in ['ADHD', 'TDC']:
    folder_path = os.path.join(target_dir, diagnosis_folder)
    
    # Ensure the folder exists
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            # Check if the file contains "rest" in its name
            if file.endswith('.nii.gz') and 'rest' not in file.lower() and 'run' not in file.lower():
                # Define source and destination paths
                src = os.path.join(folder_path, file)
                dest = os.path.join(non_rest_dir, file)
                
                # Move the file
                print(f"Moviendo archivo NON-REST: {src} a {dest}")  # Debug print
                shutil.move(src, dest)
