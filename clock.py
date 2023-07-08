import datetime
import tkinter as tk
import winsound
from PIL import ImageTk, Image


def establecer_alarma():
    hora = int(entry_hora.get())
    minutos = int(entry_minutos.get())
    alarma_establecida.config(text=f"Alarma establecida para {hora:02d}:{minutos:02d}")

def actualizar_hora():
    now = datetime.datetime.now()
    hora_actual = now.strftime("%H:%M:%S")
    label.config(text=hora_actual)

    # Comprobar si es la hora de la alarma
    if entry_hora.get() == str(now.hour) and entry_minutos.get() == str(now.minute):
        label.config(fg="green")
        label.after(1000, lambda: label.config(fg="black"))
        alarma_establecida.config(text="¡Despierta!")
        # Reproducir sonido de la alarma
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    else:
        alarma_establecida.config(text=f"Alarma establecida para {entry_hora.get()}:{entry_minutos.get()}")
    label.after(1000, actualizar_hora)

root = tk.Tk()
root.title("Reloj y Alarma")
root.geometry("300x300")

label = tk.Label(root, font=("Helvetica", 24), fg="black")
label.pack(pady=20)

alarma_establecida = tk.Label(root, text="No hay alarma establecida")
alarma_establecida.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

label_hora = tk.Label(frame, text="Hora:")
label_hora.grid(row=0, column=0, padx=5)

entry_hora = tk.Entry(frame, width=2)
entry_hora.grid(row=0, column=1)

label_dos_puntos = tk.Label(frame, text=":")
label_dos_puntos.grid(row=0, column=2)

entry_minutos = tk.Entry(frame, width=2)
entry_minutos.grid(row=0, column=3)

boton_establecer = tk.Button(frame, text="Establecer Alarma", command=establecer_alarma)
boton_establecer.grid(row=0, column=4, padx=5)

imagen = ImageTk.PhotoImage(Image.open("image.png"))
label_imagen = tk.Label(root, image=imagen)
label_imagen.pack(pady=10)

actualizar_hora()
root.mainloop()
