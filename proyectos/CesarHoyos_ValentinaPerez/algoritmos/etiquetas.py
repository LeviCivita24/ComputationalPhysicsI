# Requeriments
import warnings
import os
import skimage.draw
import skimage.io
import matplotlib.pyplot as plt
from PIL import Image
import base64
import json
import numpy as np
import tensorflow as tf

# Otras librerías
import cv2 
import matplotlib.pyplot as plt 
import modelo as modellib
import visualize
import numpy as np

# Librerías de cámara
from PIL import Image as im
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Creación de clase

class Detector:
    def __init__(self,in_url):
        self.in_url = in_url
    
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    # Método para cargar modelo y conseguir coordenadas
    def upload(self):
        config=modellib.LaserConfig() # cuando se corra en GPU toca cambiar ajuste
        model = modellib.MaskRCNN(mode="inference", model_dir="peso",config=config)  
        weights_path ="mask_modelo_entrenado.h5"
        model.load_weights(weights_path, by_name=True)

        # Guardar imagenes resultantes en archivo txt
        out_images_path = "C:/Users/Usuario/Semestres/Semestre 2022-1/Etiquetas/out_image"
        if not os.path.exists(out_images_path):
            os.makedirs(out_images_path)
            print("Directorio creado",out_images_path)

        file_names = os.listdir(self.in_url)
        
        
        for i in file_names:
            
            image_path = self.in_url + "/" + i
            image=skimage.io.imread(image_path)
            results = model.detect([image], verbose=1)
            #print(results)
            
            r_laser= results[0]
            coordenadas = r_laser['rois']  
            mascara = r_laser['masks'] 
            mascara = mascara[:,:,0]

            if len(coordenadas) == 1:
                p1 = coordenadas[0][0]
                p2 = coordenadas[0][1]
                p3 = coordenadas[0][2]
                p4 = coordenadas[0][3]
                coord_final = [(p1+p3)/2, (p2+p4)/2]
                visualize.display_instances(image, r_laser['rois'], r_laser['masks'], r_laser['class_ids'], 'punto', r_laser['scores'], title= 'Coordenada: {}'.format(coord_final)) 
                print("La coordenada de la imagen {0}, es {1}".format(i,coord_final))
                archivo = open("out_coordenada_imagen.txt","a")
                archivo.write('coord_final = % s \n' %coord_final )
               

        
                



                  


         



         

