import cv2 as cv
import speech_recognition as sr
import pyttsx3 as ttx
import datetime
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
training_images, testing_images = training_images / 255, testing_images / 255

class_name = ['Avion','Voiture','Oiseau','Chat','Cerf','Chien','Grenouille','Cheval','Bateau','Camion']

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_name[training_labels[i][0]])
plt.show()

training_images = training_images[:20000]
training_labels = training_labels[:20000]
training_images = training_images[:4000]
training_labels = training_labels[:4000]


model = models.load_model('image_classifier.model')

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')


#FONCTION VOIX
def parle(text):
    engine.say(text)
    engine.runAndWait()

def ecoute():
    try:
        with sr.Microphone() as source:
            print("Parler ")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')

    except:
        pass
    return command

def assistant():
    commander = ecoute()
    print(commander)
    if 'bonjour' in commander:
        parle('bonjour Monsieur')
    elif 'Qui est tu?' in commander:
        parle("Je suis une intelligence artificiel de classification d'image simple basé sur le modèle de reseau de neurone convolutif")
    elif 'heure' in commander:
        heure = datetime.datetime.now().strftime('%H:%M')
        parle("Il est " +heure)
    elif 'au revoir' in commander:
        parle("Ok à plus tard")
    elif 'quitter' in commander:
        parle("Ok")
        root.quit()
        root.destroy()


#FONCTION CLASSIFICATION
def classify_image():
    # Sélection image
    Tk().withdraw()
    selected_file = askopenfilename(title="Sélectionnez une image")

    if selected_file:
        # Chargement image
        selection = cv.imread(selected_file)
        image = Image.open(selected_file)
        target_width = 400  # Largeur cible de l'image
        target_height = 400  # Hauteur cible de l'image
        image = resize_image(image, target_width, target_height)
        image_for_tkinter = ImageTk.PhotoImage(image)

        if selection is not None:  # Vérification
            selection = cv.cvtColor(selection, cv.COLOR_BGR2RGB)
            img = cv.resize(selection, (32, 32))
            parle("L'image a été sélectionné avec succès")

            #prédiction
            prediction = model.predict(np.array([img]) / 255)
            index = np.argmax(prediction)

            # Affichage
            image_label.config(image=image_for_tkinter)
            image_label.image = image_for_tkinter
            result_label.config(text=f"L'image sélectionnée est un {class_name[index]} , ", font=("Arial", 12))
            parle(f"L'image sélectionnée est un {class_name[index]}")
        else:
            result_label.config(text="Impossible de charger l'image sélectionnée")

def on_quit():
    parle('Vous avez appuyer sur quitter')
    root.quit()
    root.destroy()


def resize_image(image, target_width, target_height):
    image.thumbnail((target_width, target_height))
    return image

root = Tk()
root.title("Classification d'image")
root.geometry("800x900")
root.minsize(250, 150)
root.iconbitmap("icone2.ico")
root.config(background='#4065A4')

frame = Frame(root, bg='#4065A4')
frame.pack(expand=YES)

# texte
label_title = Label(frame, text="Bienvenue sur notre classeur d'image", font=("Courier", 28), bg='#4065A4', fg='white')
label_title.pack(expand=YES, pady=20)

label_subtitle = Label(frame, text="Veuillez choisir l'une des options suivantes", font=("Courier", 10), bg='#4065A4', fg='white')
label_subtitle.pack(expand=YES, pady=10)

# Conteneur Frame pour les boutons
button_frame = Frame(root, bg='#4065A4')
classify_button = Button(button_frame, text="Classer l'image", font=("Courier", 10), bg='white', fg='#4065A4', command=classify_image)
quit_button = Button(button_frame, text="Quitter", font=("Courier", 10), bg='white', fg='#4065A4', command=on_quit)
classify_button.pack(pady=10, fill=X)
quit_button.pack(pady=10, fill=X)
button_frame.pack()

# Conteneur Frame pour l'image
image_label = Label(root, bg='#4065A4')
result_label = Label(root, text="", bg='#4065A4', fg='white', font=("Arial", 12))
image_label.pack(pady=20)
result_label.pack()

root.mainloop()

while True:
    assistant()
