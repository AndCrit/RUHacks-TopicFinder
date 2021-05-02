import webbrowser
from tkinter import *
from tkinter.ttk import *
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
    ##launching website to login
    webbrowser.open('https://cas.ryerson.ca/login?service=https://my.ryerson.ca/uPortal/Login%3FrefUrl%3D%2FuPortal%2Ff%2Fmyryerson%2Fnormal%2Frender.uP', new=0)

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

root.geometry("1000x600")

style1=Style()
style1.configure('TButton', font=('calibri', 19, 'bold'),
                foreground = 'black', background='white')

MenuLabel = Label(root, text="Topic Finder",style='TButton')
MenuLabel.grid(row=0, column=1)
img = PhotoImage(file = r"bars.png")
Label(root, image = img).grid(row = 0, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)
img_f = PhotoImage(file = r"search.png")
Label(root, image = img_f).grid(row = 0, column = 2,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

style=Style()
style.configure('W.TButton', font=('calibri', 16, 'bold'),
                background='blue',foreground = 'black')

D2LLoginButton = Button(root, text="Login to D2L",style='W.TButton',command = login)
PasteLinksButton = Button(root, text="Paste Zoom Links",style='W.TButton',command = pasteLinks)
UploadFilesButton = Button(root, text="Upload Files",style='W.TButton')
SearchEveryThingButton = Button(root, text='Search everything',style='W.TButton')

D2LLoginButton.grid(row=3, column=1,)
img1 = PhotoImage(file = r"brightspace.png")
#img1 = img.subsample(2, 2)
Label(root, image = img1).grid(row = 3, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

PasteLinksButton.grid(row=4,column=1)
img2 = PhotoImage(file = r"link.png")
Label(root, image = img2).grid(row = 4, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

UploadFilesButton.grid(row=5,column=1)
img3 = PhotoImage(file = r"upload.png")
Label(root, image = img3).grid(row = 5, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

SearchEveryThingButton.grid(row=6,column=1)
img4 = PhotoImage(file = r"search.png")
Label(root, image = img4).grid(row = 6, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

root.mainloop()
