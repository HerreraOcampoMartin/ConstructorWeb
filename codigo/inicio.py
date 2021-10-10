import json

class Iniciar:
    def __init__(self):
        arcProyecto = open('../guardados/proyecto.json', 'r')
        self.guardado = json.load(arcProyecto)

        arcProyecto.close()

    def copiado_recursivo(self, listado, documento=''):
        for componente in listado:
            uri = '../componentes/%s/%s.html' % (componente['categoria'], componente['tipo'])

            htmlArc = open(uri, 'r')
            html = htmlArc.read()
            htmlArc.close()

            if componente['tieneComponentes']:
                temp = self.copiado_recursivo(componente['contenido'], documento=documento)
                documento = documento + html.replace('<!-- CONTENIDO -->', temp)

            else:
                if componente['contenido']['texto']:
                    html = html.replace('%== TEXTO ==%', componente['contenido']['texto'])

                if componente['contenido']['src']:
                    html.replace('%== SRC ==%', componente['contenido']['src'] or '')

                if componente['contenido']['alt']:
                    html.replace('%== ALT ==%', componente['contenido']['alt'] or '')

                if componente['contenido']['enlace']:
                    html.replace('%== ENLACE ==%', componente['contenido']['enlace'] or '')

                documento = documento + html
        
        return documento

    def compilar(self, idioma, titulo):
        self.archivoFinal = open('../procs/index.html', 'w')
        baseArc = open('../componentes/base.html', 'r')
        self.base = baseArc.read()
        baseArc.close()

        final = self.base.replace('<!-- CONTENIDO -->', self.copiado_recursivo(self.guardado))
        final = final.replace('%== IDIOMA ==%', idioma)
        final = final.replace('%== TITULO ==%', titulo)
       
        self.archivoFinal.write(final)
        self.archivoFinal.close()

programa = Iniciar()
programa.compilar('es', 'Prueba')
