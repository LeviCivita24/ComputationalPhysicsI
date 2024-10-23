import etiquetas

# Inicialización.
if __name__=='__main__':
    print('Inicializando cálculo de coordenadas')

# Creación del objeto
    imagen = etiquetas.Detector("C:/Users/Usuario/Semestres/Semestre 2022-1/Etiquetas/coordenada_imagen")
    coordenada = imagen.upload()
    print(coordenada)