import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def exportar_agenda(agenda):
    datos = []
    for dia, actividades in agenda.items():
        if actividades:
            for hora, info in sorted(actividades.items()):
                datos.append([dia, hora, info.get("actividad", ""), info.get("categoria", "")])
        else:
            datos.append([dia, "", "", ""])
    df = pd.DataFrame(datos, columns=["Día", "Hora", "Actividad", "Categoría"])
    df.to_excel("agenda.xlsx", index=False)
    doc = SimpleDocTemplate("agenda.pdf", pagesize=letter)
    estilos = getSampleStyleSheet()
    contenido = []
    contenido.append(Paragraph("Agenda Semanal", estilos['Title']))
    contenido.append(Spacer(1, 12))
    tabla = Table([df.columns.tolist()] + df.values.tolist())
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ]))
    contenido.append(tabla)
    doc.build(contenido)
    print("\n✅ Agenda exportada como 'agenda.xlsx' y 'agenda.pdf'")
