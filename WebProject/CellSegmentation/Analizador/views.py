from django.http import HttpResponse
from django.shortcuts import render
import os
import sys
sys.path.append('..')
from ImageApp.models import Usuario
from ImageApp.models import Coleccion
from CellSegmentation.Adaptador import Adaptador

def has_preds(value):
    """Función que se encarga de crear las listas de imagenes y predicciones
    @param value: id de la colección a tratar.
    @return lista de paths de imágenes y predicciones
    """
    path = '../media/images/'+str(value)+'/preds'
    preds_paths = []
    img_paths = []
    hasPreds = False
    if os.path.exists(path):
        hasPreds = True
        for filename in os.listdir(path):
            string_path = path[2:] + '/' + filename
            preds_paths.append(string_path)
    path = '../media/images/'+str(value)
    for filename in os.listdir(path):
        if not hasPreds:
            preds_paths.append('/media/default.png')
        string_path = path[2:] + '/' + filename
        img_paths.append(string_path)

    return img_paths, preds_paths

def predict_collection(request, value):
    """Función que se encarga de invocar al segmentador de células
    @param request: captura el método POST
    @param value: id de la colección a tratar.
    @return: render del formulario con las variables actualizadas.
    """
    alert = False
    if request.method == 'POST':
        Ad = Adaptador()
        path = '../media/images/' + str(value) + '/*.png'
        Ad.analizar(path)
        alert = True
    img, preds = has_preds(value)
    img = zip(img,preds)
    print(img)
    return render(request, 'Colection_Preds.html', {'id_value':value, 'img':img, 'alert':alert})

def list_collections(request):
    """Función que se encarga de listar las colecciones por usuario
    @param request: captura los datos del web form
    @return render que instancia el template
    """
    usuario_creador = Usuario.objects.get(id = request.session["usuario_id"])
    colecciones = list(Coleccion.objects.filter(fk_Usuario = usuario_creador ))
    return render(request, 'Colection_List.html', {'colecciones':colecciones})