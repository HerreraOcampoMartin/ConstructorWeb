
class InsertarCodigo:
    def insertarContenido(self, html, contenido):
        if "texto" in contenido and contenido['texto']:
            html = html.replace('%== TEXTO ==%', contenido['texto'])

        if "src" in contenido and contenido['src']:
            html = html.replace('%== SRC ==%', contenido['src'])

        if "alt" in contenido and contenido['alt']:
            html = html.replace('%== ALT ==%', contenido['alt'])

        if "enlace" in contenido and contenido['enlace']:
            html = html.replace('%== ENLACE ==%', contenido['enlace'])

        return html
