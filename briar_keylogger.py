from pynput import keyboard

texto = ""

def on_press(key):
    global texto
    try:
        texto += key.char
    
    except AttributeError:
        if key == keyboard.Key.space:
            texto += " "
        elif key == keyboard.Key.enter:
            texto += "\n"
        elif key == keyboard.Key.tab:
            texto += "\t"

        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.alt:
            pass
        
        elif key == keyboard.Key.backspace and len(texto) == 0:
            pass
        elif key == keyboard.Key.backspace and len(texto) > 0:
            texto = texto[:-1]
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

print("Escuchando... Presiona teclas para capturar")
print("Presiona 'Esc' para parar y ver las palabras.")

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        ) as listener:
    listener.join()

with open("teclas.txt", "w") as outputfile:
    outputfile.write(texto)

palabras = texto.split()


print("\n--- Texto Capturado ---")
print(f"Número de palabras: {len(palabras)}")
print(f"{texto}")
