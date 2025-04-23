import ipywidgets as widgets
from IPython.display import display

# Crear widgets para la encuesta
nombre = widgets.Text(
    description='Nombre:',
)

edad = widgets.IntSlider(
    value=18,
    min=0,
    max=100,
    step=1,
    description='Edad:',
)

satisfaccion = widgets.RadioButtons(
    options=['Muy satisfecho', 'Satisfecho', 'Neutral', 'Insatisfecho', 'Muy insatisfecho'],
    description='Satisfacción:'
)

boton_enviar = widgets.Button(
    description='Enviar',
    button_style='success'
)

salida = widgets.Output()

def on_enviar_clicked(b):
    with salida:
        print("Nombre:", nombre.value)
        print("Edad:", edad.value)
        print("Satisfacción:", satisfaccion.value)
        print("¡Gracias por participar!\n")

boton_enviar.on_click(on_enviar_clicked)

# Mostrar la encuesta
display(nombre, edad, satisfaccion, boton_enviar, salida)





p1 = widgets.RadioButtons(
    options=[1, 2, 3, 4, 5, "No estratificado"],
    description='Estrato socio-economico:'
)
p2 = widgets.RadioButtons(
    options=['1 a 2', ' 3 y 4 ', '+4 ', "-1"],
    description='Ingreso promedio del hogar:'
)
p3 = widgets.RadioButtons(
    options=["si", "no"],
    description='Apoyo del estado'
)

