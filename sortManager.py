# -*- coding: utf-8 -*-
import subprocess, os, re

"""
    Clase encargada de administrar el ordenamiento de los archivos existentes en la carpeta Descargas
    @author github.com/LKezHn
    @version 1.0.0
    @date 2021/01/31
"""

class SortManager:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.createFolders()
        self.getItems()
        self.orderItems()

    """
        Método encargado de crear, si no existen, las carpetas que contendrán los archivos a ordenar.
    """
    def createFolders(self):
        folders = ["PDF's",'Images','Docs','Compressed','DevFiles']
        for folder in folders:
            try:
                os.stat("%s/Descargas/%s" % (self.path, folder))
            except:
                os.mkdir("%s/Descargas/%s" % (self.path, folder))

    """
        Método encargado de obtener el listado de archivos existentes en la carpeta Descargas
    """
    def getItems(self):
        os.chdir('%s/Descargas' % self.path)
        self.fileList = subprocess.run(['ls','-1'], stdout=subprocess.PIPE,).stdout.decode('utf-8')

    """
        Método encargado de pasar el nombre de cada arcihvo existente al método que mueve los archivos a la carpeta correspondiente.
    """
    def orderItems(self):
        for file in self.fileList.split('\n')[:-1]:
            self.moveItem(file)
        quit("Files have been sorted")

    """
        Método encargado de mover un archivo a la carpeta correspondiente, dependiendo de la extensión del mismo
        @param filename Nombre del archivo que se quiere mover
    """
    def moveItem(self,filename):
        if re.match(r'[\w\W]*\.(png|gif|svg|jpg|jpeg )', filename):
            subprocess.run(['mv', '%s' % filename, '%s/Descargas/Images' % self.path])
        elif re.match(r'[\w\W]*\.(xlsx|docx|xls|doc|txt)', filename):
            subprocess.run(['mv', '%s' % filename, '%s/Descargas/Docs' % self.path])
        elif re.match(r'[\w\W]*\.pdf', filename):
            subprocess.run(['mv', '%s' % filename, "%s/Descargas/PDF's" % self.path])
        elif re.match(r'[\w\W]*\.(zip|rar|tar.gz|deb)', filename):
            subprocess.run(['mv', '%s' % filename, "%s/Descargas/Compressed" % self.path])
        elif re.match(r'[\w\W]*\.\w+', filename):
            subprocess.run(['mv', '%s' % filename, "%s/Descargas/DevFiles" % self.path])

# Instancia de SortManager, con el cual se ejecuta el ordenamiento
(SortManager())