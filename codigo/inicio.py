import json
from InsertarCodigo import InsertarCodigo

class Iniciar:
    def __init__(self, proyecto):
        arcProyecto = open('../guardados/' + proyecto + '.json', 'r')
        self.guardado = json.load(arcProyecto)
        self.insertar = InsertarCodigo()

        arcProyecto.close()

    def copiado_recursivo(self, listado):
        documento = ""

        for componente in listado:
            uri = '../componentes/%s/%s.html' % (componente['categoria'], componente['tipo'])

            htmlArc = open(uri, 'r')
            html = htmlArc.read()
            htmlArc.close()

            if 'tieneComponentes' in componente and componente["tieneComponentes"]:
                temp = self.copiado_recursivo(componente['contenido'])
                documento = documento + html.replace('<!-- CONTENIDO -->', temp)
            else:
                html = self.insertar.insertarContenido(html, componente['contenido'])
                documento = documento + html
        
        return documento

    def copiar_css(self):
        arcCSS = open('../componentes/css/styles.css', 'r')
        procCSS = open('../procs/css/styles.css', 'w')

        css = arcCSS.read()
        procCSS.write(css)

        arcCSS.close()
        procCSS.close()

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

programa = Iniciar('proyecto')
programa.compilar('es', 'Prueba')
programa.copiar_css()
