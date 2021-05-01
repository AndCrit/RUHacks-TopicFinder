import webbrowser
from tkinter import *
count=0



# Create the scraper
root = Tk()
def scrapper(url):
    value =" text too be scrapped"
    print("From: "+ url + " Scrapped information: "+ value)
def login():
    for element in root.winfo_children():
        element.destroy()
    loginLabel = Label(root, text="Please login to d2l")
    loginLabel.grid(row=6, column=6)
    # launching website to login
    #webbrowser.open('https://cas.ryerson.ca/login?service=https://my.ryerson.ca/uPortal/Login%3FrefUrl%3D%2FuPortal%2Ff%2Fmyryerson%2Fnormal%2Frender.uP', new=0)

def pasteLinks():
    global pasteInput
    pasteInput = Entry(root)
    pasteInput.grid(row=6,column=6)
    submitButton = Button(root, text="Submit",command = SubmitPressed)
    submitButton.grid(row=7,column=6)

def SubmitPressed():
    url=pasteInput.get()
    for element in root.winfo_children():
        element.destroy()
    LinkLabel = Label(root, text="Your link is "+url)
    LinkLabel.grid(row=6,column=6)
    scrapper(url)

MenuLabel = Label(root, text="Menu")
MenuLabel.grid(row=0, column=0)


D2LLoginButton = Button(root, text="Login to D2L", command = login)
PasteLinksButton = Button(root, text="Paste Zoom Links",command = pasteLinks)
UploadFilesButton = Button(root, text="Upload Files")
SearchEveryThingButton = Button(root, text='Search everything')


D2LLoginButton.grid(row=3, column=-0,)
PasteLinksButton.grid(row=4,column=0)
UploadFilesButton.grid(row=5,column=0)
SearchEveryThingButton.grid(row=6,column=0)



root.mainloop()