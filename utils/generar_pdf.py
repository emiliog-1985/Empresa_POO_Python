# Importaciones libreria reportLab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(lista:list = [], nombre_archivo:str = "reporte.pdf"):
    print('Iniciando exportacion...')
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    
    if nombre_archivo == 'reporte_empleados.pdf':
        print('Configurando titulo')
        # Configuracion titulo
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height-50, "Listado de Empleados")
        
        print('Configurando cabecera tabla')
        # Generando una tabla con los datos
        y = height - 100
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Usuario")
        c.drawString(110, y, "Nombre")
        c.drawString(180, y, "Apellido")
        c.drawString(250, y, "Dirección")
        c.drawString(370, y, "Teléfono")
        c.drawString(440, y, "email")
        
        # Linea debajo de encabezados
        y -= 15
        c.line(40, y, 580, y)
        
        print('Configurando cuerpo tabla')
        # Contenido tabla
        y -= 15
        c.setFont("Helvetica", 9)
        
        for l in lista:
            print('Generando fila...')
            # Si se acaba la pagina saltamos a otra
            if y < 50:
                c.showPage()
                y -= 50
                c.setFont("Helvetica", 9)
            
            c.drawString(50, y, l['nombre_usuario'])
            c.drawString(110, y, l['nombre'])
            c.drawString(180, y, l['apellido'])
            c.drawString(250, y, str(l['direccion']))
            c.drawString(370, y, str(l['telefono']))
            c.drawString(440, y, l['email'])
            
            y -= 15
        
        c.save()
        print('PDF generado')

    elif nombre_archivo == 'reporte_proyectos.pdf':
        print('Configurando titulo')
        # Configuracion titulo
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height-50, "Listado de Proyectos")
        
        print('Configurando cabecera tabla')
        # Generando una tabla con los datos
        y = height - 100
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "ID")
        c.drawString(80, y, "Nombre")
        c.drawString(220, y, "Fecha Inicio")
        c.drawString(290, y, "Fecha Término")
        c.drawString(380, y, "Descripción")
        c.drawString(520, y, "Estado")
        
        # Linea debajo de encabezados
        y -= 15
        c.line(40, y, 580, y)
        
        print('Configurando cuerpo tabla')
        # Contenido tabla
        y -= 15
        c.setFont("Helvetica", 9)
        
        for l in lista:
            print('Generando fila...')
            # Si se acaba la pagina saltamos a otra
            if y < 50:
                c.showPage()
                y -= 50
                c.setFont("Helvetica", 9)
            
            c.drawString(50, y, str(l['proyecto_id']))
            c.drawString(80, y, l['nombre_proyecto'])
            c.drawString(220, y, str(l['fecha_inicio']))
            c.drawString(290, y, str(l['fecha_termino']))
            c.drawString(380, y, l['descripcion'])
            c.drawString(520, y, l['estado'])
            
            y -= 15
        
        c.save()
        print('PDF generado')
    
    elif nombre_archivo == 'reporte_departamentos.pdf':
        print('Configurando titulo')
        # Configuracion titulo
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height-50, "Listado de Departamentos")
        
        print('Configurando cabecera tabla')
        # Generando una tabla con los datos
        y = height - 100
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "ID")
        c.drawString(80, y, "Nombre")
        c.drawString(220, y, "Ubicación")
        
        # Linea debajo de encabezados
        y -= 15
        c.line(40, y, 580, y)
        
        print('Configurando cuerpo tabla')
        # Contenido tabla
        y -= 15
        c.setFont("Helvetica", 9)
        
        for l in lista:
            print('Generando fila...')
            # Si se acaba la pagina saltamos a otra
            if y < 50:
                c.showPage()
                y -= 50
                c.setFont("Helvetica", 9)
            
            c.drawString(50, y, str(l['departamento_id']))
            c.drawString(80, y, l['nombre'])
            c.drawString(220, y, str(l['ubicacion']))
            
            y -= 15
            
        c.save()
        print('PDF generado')
    
    elif nombre_archivo == 'reporte_registro_tiempo.pdf':
        print('Configurando titulo')
        # Configuracion titulo
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height-50, "Listado de Registros de Tiempo")
        
        print('Configurando cabecera tabla')
        # Generando una tabla con los datos
        y = height - 100
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "ID")
        c.drawString(80, y, "Proyecto")
        c.drawString(150, y, "Nombre")
        c.drawString(220, y, "Apellido")
        c.drawString(290, y, "Fecha")
        c.drawString(350, y, "Horas Trabajo")
        c.drawString(430, y, "Descripción")
        
        # Linea debajo de encabezados
        y -= 15
        c.line(40, y, 580, y)
        
        print('Configurando cuerpo tabla')
        # Contenido tabla
        y -= 15
        c.setFont("Helvetica", 9)
        
        for l in lista:
            print('Generando fila...')
            # Si se acaba la pagina saltamos a otra
            if y < 50:
                c.showPage()
                y -= 50
                c.setFont("Helvetica", 9)
            
            c.drawString(50, y, str(l['registro_id']))
            c.drawString(80, y, l['nombre_proyecto'])
            c.drawString(150, y, l['nombre'])
            c.drawString(220, y, l['apellido'])
            c.drawString(290, y, str(l['fecha']))
            c.drawString(350, y, str(l['horas_trabajo']))
            c.drawString(430, y, str(l['descripcion']))
            
            y -= 15
            
        c.save()
        print('PDF generado')
        
