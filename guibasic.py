import customtkinter
from minage_lightwork import show_graph_1

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Graph Viewer (MNT1)")
root.geometry("1050x500")

color_blindness_index = 0


# root.iconbitmap('c:\PyImg')

# if we wanted images
# imgcl = ImageTk.PhotoImage(Image.open(""))
# imglab = Label(image=imgcl)
# imglab.grid(row=10,column=0)

# Functions when a graph button is clicked. Add the thing that opens the correct graph with the rest of the settings set here
def click1():
    disp = customtkinter.CTkLabel(root, text=" A separate window is now displaying Graph 1", font=("Ariel", 20))
    disp.grid(row=1, column=4, padx=10)
    show_graph_1(slider.get(), color_blindness_index)


def click2():
    disp2 = customtkinter.CTkLabel(root, text=" A separate window is now displaying Graph 2", font=("Ariel", 20))
    disp2.grid(row=1, column=4, padx=10)
    # show_graph_2(slider.get(), color_blindness_index)


def click3():
    disp3 = customtkinter.CTkLabel(root, text=" A separate window is now displaying Graph 3", font=("Ariel", 20))
    disp3.grid(row=1, column=4, padx=10)
    # show_graph_3(slider.get(), color_blindness_index)


def click4():
    disp4 = customtkinter.CTkLabel(root, text=" A separate window is now displaying Graph 4", font=("Ariel", 20))
    disp4.grid(row=1, column=4, padx=10)
    # show_graph_4(slider.get(), color_blindness_index)


def click5():
    disp5 = customtkinter.CTkLabel(root, text=" A separate window is now displaying Graph 5", font=("Ariel", 20))
    disp5.grid(row=1, column=4, padx=10)
    # show_graph_5(slider.get(), color_blindness_index)


def click6():
    disp6 = customtkinter.CTkLabel(root, text=" A separate window is now displaying Graph 6", font=("Ariel", 20))
    disp6.grid(row=1, column=4, padx=10)
    # show_graph_6(slider.get(), color_blindness_index)


# functions to change color mode, change graph color variables with these functions
def colormode_update1():
    global colormode_label
    colormode_label = customtkinter.CTkLabel(root, text="Color mode set to Deuteranopia", font=("Ariel", 20))
    colormode_label.grid(row=3, column=4)
    global color_blindness_index
    color_blindness_index = 1
# change colors in graph for deuteranopia


def colormode_update2():
    global colormode_label
    colormode_label = customtkinter.CTkLabel(root, text="   Color mode set to Protanopia   ", font=("Ariel", 20))
    colormode_label.grid(row=3, column=4)
    global color_blindness_index
    color_blindness_index = 2
# change colors in graph for protanopia


def colormode_update3():
    global colormode_label
    colormode_label = customtkinter.CTkLabel(root, text="      Color mode set to Tritanopia      ", font=("Ariel", 20))
    colormode_label.grid(row=3, column=4)
    global color_blindness_index
    color_blindness_index = 3
# change colors in graph for tritanopia


def defaultcmode():
    cmmd = customtkinter.CTkLabel(root, text="       Color mode set to default       ", font=("Ariel", 20))
    cmmd.grid(row=3, column=4)
    global color_blindness_index
    color_blindness_index = 0


colormode_label = customtkinter.CTkLabel(root, text="       Color mode set to default       ", font=("Ariel", 20))
colormode_label.grid(row=3, column=4)

# graph button header
viewg = customtkinter.CTkLabel(root, text="Select graph to view:", font=("Ariel", 20))
viewg.grid(row=1, column=0, padx=10)

# graph buttons
g1 = customtkinter.CTkButton(root, text="Display Graph 1", command=click1, font=("Ariel", 20), height=50,
                             width=150)  # actual buttons that do above commands
g1.grid(row=0, column=1, padx=10, pady=10)
g2 = customtkinter.CTkButton(root, text="Display Graph 2", command=click2, font=("Ariel", 20), height=50, width=150)
g2.grid(row=1, column=1, padx=10, pady=10)
g3 = customtkinter.CTkButton(root, text="Display Graph 3", command=click3, font=("Ariel", 20), height=50, width=150)
g3.grid(row=2, column=1, padx=10, pady=10)
g4 = customtkinter.CTkButton(root, text="Display Graph 4", command=click4, font=("Ariel", 20), height=50, width=150)
g4.grid(row=0, column=2, padx=10, pady=10)
g5 = customtkinter.CTkButton(root, text="Display Graph 5", command=click5, font=("Ariel", 20), height=50, width=150)
g5.grid(row=1, column=2, padx=10, pady=10)
g6 = customtkinter.CTkButton(root, text="Display Graph 6", command=click6, font=("Ariel", 20), height=50, width=150)
g6.grid(row=2, column=2, padx=10, pady=10)

# color buttons header
cbfunct = customtkinter.CTkLabel(root, text="Set color mode:", font=("Ariel", 20))
cbfunct.grid(row=3, column=0)

# buttons (change color on click?)
cbm1 = customtkinter.CTkButton(master=root, text="Deuteranopia", command=colormode_update1, font=("Ariel", 20), height=50,
                               width=150)  # command=cbmode1
cbm1.grid(row=3, column=1, padx=10, pady=10)
cbm2 = customtkinter.CTkButton(master=root, text="Protanopia", command=colormode_update2, font=("Ariel", 20), height=50,
                               width=150)
cbm2.grid(row=3, column=2, padx=10, pady=10)
cbm3 = customtkinter.CTkButton(master=root, text="Tritanopia", command=colormode_update3, font=("Ariel", 20), height=50,
                               width=150)
cbm3.grid(row=4, column=1, padx=10, pady=10)
cbmd = customtkinter.CTkButton(master=root, text="Default", command=defaultcmode, font=("Ariel", 20), height=50,
                               width=150)  # command=defaultcmode
cbmd.grid(row=4, column=2, padx=10, pady=10)

# def sll(var):
# tsshow = customtkinter.CTkLabel(root, text=str(hori.get()))
# tsshow.grid(row=6, column=2)
# change text size values here (if we are doing that)

# text change slider header
tslabel = customtkinter.CTkLabel(root, text="Text size on graph:", font=("Ariel", 20))
tslabel.grid(row=6, column=0)


# slider stuf
def slider_event(value):
    tsshow = customtkinter.CTkLabel(root, text=int(value))
    # gets value from slider and makes it an int (do the same wherever text size is decided for graphs so you can use slider values)
    tsshow.grid(row=6, column=2)


slider = customtkinter.CTkSlider(master=root, from_=12, to=48, command=slider_event)
# lowest txt size: 12, highest: 48, can change if there is a better min/max
slider.grid(row=6, column=1)

# credit1 = customtkinter.CTkLabel(root, text="  ")
# credit1.grid(row=7, column=1, padx=10)
credit = customtkinter.CTkLabel(root, text="Built by Millard North Team 1")
credit.grid(row=8, column=1, padx=10)

root.mainloop()
