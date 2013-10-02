import Tkinter

def ende():
	main.destroy()

main = Tkinter.Tk()

lb1 = Tkinter.Label(main, text = "TK Application")
lb1["font"] = "Arial 12 normal"
lb1["height"] = "2"
lb1["width"] = "20"
lb1["anchor"] = "w"
lb1.pack()

lb2 = Tkinter.Label(main)
im = Tkinter.PhotoImage(file="vmware_logo.gif")
lb2["image"] = im
lb2.pack(side = "bottom")

e = Tkinter.Entry(main, width=60)
e.pack()

b = Tkinter.Button(main, text= "Ende", command = ende)
b.pack()

main.mainloop()
