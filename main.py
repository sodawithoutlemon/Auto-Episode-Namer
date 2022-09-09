import tkinter
import os
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory

bg = "white"
text = "black"

exceptions = ["1080", "720"]

years = 1990
for x in range(50):
    exceptions.append(str(years))
    years +=1

filename = None
encode = ""
extractedloc = []
extractedfiles = []
episodes = []

testrunoutput = []


def convertbrain():
    global filename
    global encode

    episode = ""
    kontroller = False

    filename = askdirectory()

    for root, dirs, files in os.walk(filename, topdown=False):
        for name in files:

            # app open every file in directory and only catch the names
            var = os.path.join(root, name)
            extractedloc.append(var)
            svar = var.split(filename)[1]
            extractedfiles.append(svar)

            # app gets video format name
            encode = svar[-3:]
            stepone = [*svar]
            stepone.pop()

            # app detect every numeric numbers to name episodes
            for x in range(len(stepone)):
                char = stepone[x]
                if (char.isnumeric()):
                    if kontroller == False:
                        episode += "."
                        kontroller = True
                    episode += char
                else:
                    if (kontroller):
                        episode += "."
                        kontroller = False
                    episode += " "

            # reformatting so we can only see numbers
            episode = episode.replace(" ", "")
            episode = episode.replace(".", " ")
            episode = episode[1:]
            episode = episode.split(" ")
            episode = list(filter(None, episode))

            # removing hardcoded numbers like 1080p or 720p
            for item in exceptions:
                try:
                    episode.remove(item)
                except:
                    pass

            # saving episode numbers so we can use it on different functions
            episodes.append(episode)
            episode = ""


# app's main converting style without checking
def mainconvert():
    convertbrain()
    for y in range(len(episodes)):
        os.rename(extractedloc[y], f"{filename}/{episodes[y][0]}.{encode}")
    window.destroy()


# app's asks the users with example videos
def testconvert():
    convertbrain()
    for y in range(len(episodes)):
        newname = f"{filename}/{episodes[y][0]} - {extractedfiles[y][1:]}.{encode}"
        testrunoutput.append(newname)
        os.rename(extractedloc[y], newname)
    main.grid_forget()
    testco.grid_forget()

    # apps creates a button to apply changings
    testaccepter = ttk.Button(window, text="Accept Test Run", command=accepttestrun)
    testaccepter.config(width=15)
    testaccepter.grid(column=0, row=2, columnspan=2)


# applies test run
def accepttestrun():
    for y in range(len(testrunoutput)):
        os.rename(testrunoutput[y], f"{filename}/{episodes[y][0]}.{encode}")
    window.destroy()


# creating tkinter interface
is_true = True
if is_true:

    window = tkinter.Tk()
    window.title("Episode Lister")
    window.config(padx=50, pady=50, bg=bg)

    # create responsiveness
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

    testco = ttk.Button(window, text="Test Run", command=testconvert)
    testco.config(width=15)
    testco.grid(column=1, row=1)

    window.mainloop()
