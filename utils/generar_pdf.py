# Importaciones libreria reportLab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf_usuarios(usuarios:list = [], nombre_archivo:str = "usuarios.pdf"):
    print('Iniciando exportacion...')
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    
    print('Configurando titulo')
    # Configuracion titulo
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height-50, "Listado de usuarios")
    
    
    print('Configurando cabecera tabla')
    # Generando una tabla con los datos
    y = height - 100
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Rut")
    c.drawString(100, y, "Nombre Completo")
    c.drawString(250, y, "Usuario")
    c.drawString(350, y, "Sueldo")
    
    # Linea debajo de encabezados
    y -= 15
    c.line(40, y, 560, y)
    
    
    print('Configurando cuerpo tabla')
    # Contenido tabla
    y -= 15
    c.setFont("Helvetica-Bold", 9)
    
    for u in usuarios:
        print('Generando fila...')
        # Si se acaba la pagina saltamos a otra
        if y < 50:
            c.showPage()
            y -= 50
            c.setFont("Helvetica-Bold", 9)
        
        c.drawString(50, y, u['rut'])
        c.drawString(100, y, u['nombre'])
        c.drawString(250, y, u['usuario'])
        c.drawString(350, y, str(u['sueldo']))
        
        y -= 15
    
    c.save()
    print('PDF generado')
    
    