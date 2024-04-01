import os
import pandas as pd

folder_path = 'Your folder'

file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

df = pd.DataFrame(file_names, columns=['Filename'])

excel_path = 'file_names.xlsx'

df.to_excel(excel_path, index=False)

print(f'File names have been saved to {excel_path}')
