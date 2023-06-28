
import PySimpleGUI as sg

def centrador(content, horizontal_only=False, **column_parameters) -> sg.Column:
    '''Centra un contenido en una columna.

    Args:
        content: contenido a centrar.
        horizontal_only: por defecto : false.
        column_parameters: todos los parámetros de columna que se aplicarán como configuración.
    Devuelve: 
        Una columna con el contenido centrado y los parámetros de columna aplicados.'''
    column_parameters['element_justification'] = 'center'
    column_parameters['expand_y'] = not horizontal_only
    column_parameters['expand_x'] = True
    column_parameters['pad'] = 0
    background_color = column_parameters.get('background_color', None)

    match content:
        case [*elements] if all(isinstance(element, list) for element in elements):
            layout = content
        case [*elements] if all(issubclass(type(element), sg.Element) for element in elements):
            layout = [content]
        case sg.Element():
            layout = [[content]]

    layout = layout if horizontal_only else [
        [sg.VPush(background_color)], *layout, [sg.VPush(background_color)]
    ]
    return sg.Column(
        layout,
        **column_parameters
    )