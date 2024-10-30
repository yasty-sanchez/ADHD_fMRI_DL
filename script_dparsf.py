import os
import pandas as pd
import shutil

# Paths to your directories
data_directory = os.path.join('archive', 'ADHD200_DPARSF')
meta_file_path = os.path.join('archive', 'meta.csv')
output_directory = os.path.join('data', 'preprocessed')  # Directory to save organized data

# Load the meta data file
meta_df = pd.read_csv(meta_file_path)

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Create folders for ADHD and TDC
adhd_directory = os.path.join(output_directory, 'ADHD')
tdc_directory = os.path.join(output_directory, 'TDC')
os.makedirs(adhd_directory, exist_ok=True)
os.makedirs(tdc_directory, exist_ok=True)

# Iterate over each participant folder in the data directory
for participant_folder in os.listdir(data_directory):
    participant_path = os.path.join(data_directory, participant_folder)
    
    if os.path.isdir(participant_path):
        # Extract participant ID from the folder name
        participant_id = participant_folder
        
        # Get the label from the meta DataFrame
        label_row = meta_df[meta_df['Subject'] == participant_id]
        
        if not label_row.empty:
            diagnosis = label_row['Diagnosis'].values[0]
            
            # Determine the output folder based on diagnosis
            if diagnosis == 'ADHD':
                participant_output_path = os.path.join(adhd_directory, f"{participant_id}_{diagnosis}")
            elif diagnosis == 'HC':
                participant_output_path = os.path.join(tdc_directory, f"{participant_id}_{diagnosis}")
            else:
                continue  # Skip if diagnosis is neither ADHD nor TDC

            # Create a new folder for the participant's data in the appropriate directory
            os.makedirs(participant_output_path, exist_ok=True)
            
            # Copy only .nii.gz files to the new output path
            results_path = os.path.join(participant_path, 'Results')
            for result_folder in os.listdir(results_path):
                result_folder_path = os.path.join(results_path, result_folder)
                if os.path.isdir(result_folder_path):
                    for file_name in os.listdir(result_folder_path):
                        if file_name.endswith('.nii.gz'):
                            file_path = os.path.join(result_folder_path, file_name)
                            shutil.copy(file_path, participant_output_path)
                            print(f"Copied {file_name} to {participant_output_path}")
                    
            print(f"Processed participant {participant_id}: Diagnosis - {diagnosis}")

print("Data organization completed.")