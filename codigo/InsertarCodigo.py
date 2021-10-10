
class InsertarCodigo:
    def insertarContenido(self, html, contenido): 
        if contenido['texto']:
            html = html.replace('%== TEXTO ==%', contenido['texto'])

        if contenido['src']:
            html.replace('%== SRC ==%', contenido['src'] or '')

        if contenido['alt']:
            html.replace('%== ALT ==%', contenido['alt'] or '')

        if contenido['enlace']:
            html.replace('%== ENLACE ==%', contenido['enlace'] or '')

        return html
