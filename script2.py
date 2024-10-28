import os
import pandas as pd

# Ruta a la carpeta que contiene los archivos nii.gz
data_dir = os.path.join('datasets')
target_dir = os.path.join('datasets', 'preprocessed')

# Leer archivo de etiquetas fenotípicas
try:
    phenotypes_file = os.path.join(data_dir, 'adhd200_preprocessed_phenotypics.csv')
    phenotypes_df = pd.read_csv(phenotypes_file)

    # Verificar que las columnas necesarias estén presentes
    required_columns = ['ScanDir ID', 'DX']
    if not all(col in phenotypes_df.columns for col in required_columns):
        raise ValueError("El archivo CSV no contiene las columnas requeridas")

    # Asegurarse de que los IDs tengan 7 dígitos
    phenotypes_df['ScanDir ID'] = phenotypes_df['ScanDir ID'].apply(lambda x: str(x).zfill(7))

    # Crear un diccionario de fenotipos
    phenotypes = phenotypes_df.set_index('ScanDir ID')['DX'].to_dict()
    print("Fenotipos cargados correctamente:", phenotypes)  # Debug print
except FileNotFoundError:
    print("El archivo de fenotipos no se encontró")
except pd.errors.EmptyDataError:
    print("El archivo de fenotipos está vacío")
except pd.errors.ParserError as e:
    print(f"Error al parsear el archivo de fenotipos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")

# Traverse the data_dir to search for .nii files organized in subject ID folders
for root, dirs, files in os.walk(data_dir):
    # Only process if it's the last folder (i.e., no subdirectories)
    if not dirs:
        # Check if the folder name is a subject ID in phenotypes
        subject_id = os.path.basename(root)
        if subject_id in phenotypes:
            print(f"Procesando ID: {subject_id} en carpeta {root}")  # Debug print
            for file in files:
                if file.endswith('.nii.gz'):
                    # Determine diagnosis based on subject_id
                    diagnosis = phenotypes.get(subject_id)

                    # Define new file name and target directory based on diagnosis
                    new_filename = f"{subject_id}_session_{file}"
                    target_subdir = os.path.join(target_dir, 'TDC' if diagnosis == '0' else 'ADHD')

                    # Create target subdirectory if it doesn’t exist
                    os.makedirs(target_subdir, exist_ok=True)

                    # Move the file
                    src = os.path.join(root, file)
                    dest = os.path.join(target_subdir, new_filename)
                    print(f"Moviendo archivo: {src} a {dest}")  # Debug print
                    os.rename(src, dest)
