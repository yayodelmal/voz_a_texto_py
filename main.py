import speech_recognition as sr

# Configuramos el reconocimiento de voz
r = sr.Recognizer()

# Configuramos el micrófono como fuente de audio
mic = sr.Microphone()

# Establecemos la tasa de muestreo en 16000 Hz
sr.Microphone().list_microphone_names()
mic = sr.Microphone(device_index=1)
mic.CHUNK = 1024
mic.RATE = 8000

# Abrimos el archivo de texto donde se registrarán las transcripciones
with open('transcripciones.txt', 'a') as archivo:
    
    while True:
        try:
            # Escuchamos el audio del micrófono
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            
            # Traducimos el audio a texto
            texto = r.recognize_google(audio, language='es-ES')
            print("Ha dicho: " + texto)
            
            # Escribimos la transcripción en el archivo de texto
            archivo.write(texto + '\n')
            
        except sr.UnknownValueError:
            print("No se ha podido entender lo que ha dicho")
        except sr.RequestError as e:
            print("No se puede obtener respuesta del servicio de reconocimiento de voz; {0}".format(e))
