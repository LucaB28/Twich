import json
import os
import subprocess

# Ruta de la carpeta donde se encuentran los archivos JSON
json_folder = 'C:/Users/Luca/OneDrive/Escritorio/jsones'

# Ruta de la carpeta donde se guardarán los videos descargados
output_folder = 'C:/Users/Luca/OneDrive/Escritorio/videos'

# Recorrer cada archivo JSON en la carpeta
for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        json_path = os.path.join(json_folder, filename)

        # Leer el archivo JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Recorrer cada elemento en el archivo JSON
        for item in data['data']:
            video_url = item['url']
            broadcaster_name = item['broadcaster_name']

            # Obtener el nombre del archivo de salida basado en el nombre del broadcaster y la URL
            video_filename = f'{broadcaster_name}_' + os.path.basename(video_url)
            output_path = os.path.join(output_folder, video_filename)

            # Descargar el video utilizando youtube-dl
            subprocess.run(['youtube-dl', '-f', 'mp4', '-o', f'{output_path}.%(ext)s', video_url])


