from tkinter import *
from PIL import Image, ImageTk, ImageSequence


root = Tk()
root.title("Classification d'image")
image = Image.open('dog.jpg')
# target_width = 800  # Largeur cible de l'image
# target_height = 700  # Hauteur cible de l'image
# image = resize_image(image, target_width, target_height)
image_for_tkinter = ImageTk.PhotoImage(image)
root.geometry('800x600')

#Utilisation de canvas
canvas = Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

canvas.create_image(0,0, image=image_for_tkinter, anchor="nw")

canvas.create_text(800, 400,text="welcome", font=("Helvetica", 50), fill="white")

button = Button(root, text="Begin")
button_window = canvas.create_window(10, 10, anchor="nw", window=button)



#Autre methode

# image_label = Label(root, image=image_for_tkinter)
# image_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# #TEXT
# lbl=Label(root, text="Welcome", font=("Helvetica", 50), fg="white", bg="black")
# lbl.pack(pady=50)
#
# #frame
# frame = Frame(root, bg="black")
# frame.pack(pady=20)
#
# #Button
# button = Button(frame, text="Begin")
# button.grid(row=0, column=0,padx=20)



root.mainloop()

# root = Tk()
# root.title("Classification d'image")
# root.geometry("600x400")
#
# def play_gif():
#     global img
#     img = Image.open("loading.gif")
#     lbl = Label(root)
#     lbl.place(x=0, y=0)
#
#     for img in ImageSequence.Iterator(img):
#         img = ImageTk.PhotoImage(img)
#         lbl.config(image=img)
#         root.update()
#     root.after(0,play_gif())
#
# def exit():
#     root.destroy()
#
#
# play = Button(root, text="play",command = play_gif)
# exit = Button(root, text="exit",command = exit)
#
# play.pack(pady=25, fill=X)
# exit.pack(pady=2, fill=X)
#
# root.mainloop()