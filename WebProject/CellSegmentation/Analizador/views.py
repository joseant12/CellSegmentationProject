from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import os
import shutil
import sys
sys.path.append('..')
from ImageApp.models import Usuario
from ImageApp.models import Coleccion
from CellSegmentation.Adaptador import Adaptador
from CellSegmentation.contador import pintarCelulas

def create_zip(request):
    shutil.make_archive("../media/zip_files/46/output_filename", 'zip', "../media/images/46")

def get_variables(value):
    img, preds, counts = has_preds(value)
    img = zip(img,preds,counts)
    coleccion_obj = Coleccion.objects.get(id = value)
    print(preds)
    return img, coleccion_obj.tiempo

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
    elif request.method == "GET":
        print("aloja")
    img, tiempo = get_variables(value) 
    return render(request, 'Colection_Preds.html', {'id_value':value, 'img':img, 'alert':alert, 'tiempo':tiempo})

def list_collections(request):
    """Función que se encarga de listar las colecciones por usuario
    @param request: captura los datos del web form
    @return render que instancia el template
    """
    usuario_creador = Usuario.objects.get(id = request.session["usuario_id"])
    colecciones = list(Coleccion.objects.filter(fk_Usuario = usuario_creador ))
    return render(request, 'Colection_List.html', {'colecciones':colecciones})

def download_files(request, value):
    alert = False
    create_zip(request)
    with open('../media/zip_files/46/output_filename.zip', 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/x-zip-compressed")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename('../media/zip_files/46/output_filename.zip')
    img, tiempo = get_variables(value) 
    #return render(request, 'Colection_Preds.html', {'id_value':value, 'img':img, 'alert':alert, 'tiempo':tiempo})
    return response