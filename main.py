import tkinter
import os
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory
FONT_NAME = "Courier"

bg = "white"
bgforbutton = "#4285F4"
text = "black"

exceptions = ["1080", "720"]

encode = ""
extractedpos = []
extractedloc = []
extractedfiles = []
filename = askdirectory()
nepisodes = []
testrunoutput = []

def convertbrain():
    global encode
    for root, dirs, files in os.walk(filename, topdown=False):
        for name in files:
            var = os.path.join(root, name)
            extractedloc.append(var)
            svar = var.split(filename)[1]
            extractedfiles.append(svar)
    word = ""
    episodes = []
    kontroller = False
    for item in extractedfiles:
        encode = item[-3:]
        stepone = [*item]
        stepone.pop()
        for x in range(len(stepone)):

            char = stepone[x]

            if (char.isnumeric()):
                if kontroller == False:
                    word += "."
                    kontroller = True
                word += char
            else:
                if (kontroller):
                    word += "."
                    kontroller = False
                word += " "
        word = word.replace(" ", "")
        word = word.replace(".", " ")
        word = word[1:]
        episodes.append(word)
        word = ""
    for item in episodes:
        ntvar = item.split(" ")
        ntvar = list(filter(None, ntvar))

        for item in exceptions:
            try:
                ntvar.remove(item)
            except:
                pass

        nepisodes.append(ntvar)

def accepttestrun():
    for y in range(len(testrunoutput)):
        os.rename(testrunoutput[y], f"{filename}/{nepisodes[y][0]}.{encode}")
    window.destroy()

def testconvert():
    convertbrain()
    for y in range(len(nepisodes)):
        newname = f"{filename}/{nepisodes[y][0]} - {extractedfiles[y][1:]}.{encode}"
        testrunoutput.append(newname)
        os.rename(extractedloc[y], newname)
    main.grid_forget()
    testco.grid_forget()
    testaccepter = ttk.Button(window, text="Accept Test Run", command=accepttestrun)
    testaccepter.config(width=15)
    testaccepter.grid(column=0, row=2, columnspan=2)

def mainconvert():
    convertbrain()
    for y in range(len(nepisodes)):
        os.rename(extractedloc[y], f"{filename}/{nepisodes[y][0]}.{encode}")
    window.destroy()

is_true = True
if is_true:
    window = tkinter.Tk()
    window.title("Episode Lister")
    window.config(padx=50, pady=50, bg=bg)
    n_rows = 2
    n_columns = 2
    for i in range(n_rows):
        window.grid_rowconfigure(i, weight=1)
    for i in range(n_columns):
        window.grid_columnconfigure(i, weight=1)

    info = tkinter.Label(text="simple way to sort \n videos by episode numbers", font=(25))
    info.config(bg=bg, fg=text, width=30)
    info.grid(column=0, row=0, columnspan=2, pady=20)

    main = ttk.Button(window, text="Main Run", command=mainconvert)
    main.config(width=15)
    main.grid(column=0, row=1)

    testco = ttk.Button(window, text="Test Run", command=testconvert)
    testco.config(width=15)
    testco.grid(column=1, row=1)

    window.mainloop()

