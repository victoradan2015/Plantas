from class_configuracion import Configuracion
from class_sockets import Websockets

miConfiguracion = Configuracion()
miWebsockets = Websockets()

class Main:
    miConfiguracion.IniciarSensores()
    miConfiguracion.SetTemperaturaActual()
    miConfiguracion.SetHumedadActual()
    miConfiguracion.ControlHumedadActual()
    miConfiguracion.ControlTemperaturaActual()
    miConfiguracion.GenerarDiccionario()
    miConfiguracion.ConexionMongoLocal(miConfiguracion.GetDiccionario())
    miConfiguracion.AccionarMySQL()
    
    miWebsockets.send_message()
