from django.http import HttpResponse
from django.shortcuts import render
import os
import sys
sys.path.append('..')
from ImageApp.models import Usuario
from ImageApp.models import Coleccion
from CellSegmentation.Adaptador import Adaptador
from CellSegmentation.contador import pintarCelulas

def has_preds(value):
    """Función que se encarga de crear las listas de imagenes y predicciones
    @param value: id de la colección a tratar.
    @return lista de paths de imágenes y predicciones
    """
    path = '../media/images/'+str(value)+'/preds'
    preds_paths = []
    img_paths = []
    count_path = []
    hasPreds = False
    if os.path.exists(path):
        hasPreds = True
        for filename in os.listdir(path):
            if filename != "count":
                string_path = path[2:] + '/' + filename
                count_string_path =  path[2:] + '/count/' + filename[:-9] + ".png"
                preds_paths.append(string_path)
                count_path.append(count_string_path)

    path = '../media/images/'+str(value)
    for filename in os.listdir(path):
        if filename != "preds":
            if not hasPreds:
                preds_paths.append('/media/default.png')
                count_path.append('/media/default.png')
            string_path = path[2:] + '/' + filename
            img_paths.append(string_path)

    return img_paths, preds_paths, count_path

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
        Ad.analizar(path,value)
        alert = True
    img, preds, counts = has_preds(value)
    """
    del img[-1]
    del preds[-1]
    del counts[-1]
    """
    print(img)
    print(preds)
    print(counts)
    img = zip(img,preds,counts)
    return render(request, 'Colection_Preds.html', {'id_value':value, 'img':img, 'alert':alert})

def list_collections(request):
    """Función que se encarga de listar las colecciones por usuario
    @param request: captura los datos del web form
    @return render que instancia el template
    """
    usuario_creador = Usuario.objects.get(id = request.session["usuario_id"])
    colecciones = list(Coleccion.objects.filter(fk_Usuario = usuario_creador ))
    return render(request, 'Colection_List.html', {'colecciones':colecciones})