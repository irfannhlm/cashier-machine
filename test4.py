from PIL import ImageTk, Image as pil
from tkinter import *
import os

filepath = os.path.dirname(os.path.realpath(__file__))

window = Tk()
window.geometry("720x720")
bg_image = ImageTk.PhotoImage(pil.open(f"{filepath}/images/bg_info.jpg").resize((720, 720), pil.Resampling.LANCZOS))

bgcanvas = Canvas(window)
bgcanvas.pack(expand=1, fill=BOTH)
bgcanvas.create_image(0, 0, image=bg_image, anchor=NW)

bgcanvas.create_text(360, 360, width=720, font=("Maiandra GD", 25), text="awdmwaiawldwijwaidlimwanldiaai;dawj;awjijasidjaw;d")

window.mainloop()