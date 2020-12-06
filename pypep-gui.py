import tkinter as tk
import sys
from PepTool import *
from Bio.Seq import Seq

class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        # self.frame = tk.Frame(self.master)
        self.master.title("Menu")

        self.butnew("Permutations", "2", Win2)
        self.butnew("Operational", "3", Win3)
        self.butnew("Amino Acid Count", "4", Win4)
        self.B = tk.Button(self.master,text="Exit",command=self.stop,bg="red3",activebackground="red4").pack()
        # self.frame.pack()

    def butnew(self, text, number, _class):
        tk.Button(self.master, text = text, command= lambda: self.new_window(number, _class)).pack()

    def new_window(self, number, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new, number)

    def stop(self):
        sys.exit('stopped')

class Win2:
    def __init__(self, master, number):
        self.master = master
        # self.master.geometry("400x400+200+200")
        # self.frame = tk.Frame(self.master)
        self.master.title("Permutations")
        self.master.config(bg="gray85")

        self.pattern = tk.StringVar()
        self.inputs = tk.StringVar()

        self.l1 = tk.Label(self.master,text="Pattern")
        self.l1.place(x=0,y=0)

        self.l2 = tk.Label(self.master,text="Inputs")
        self.l2.place(x=0,y=30)

        self.e1=tk.Entry(self.master,textvariable=self.pattern)
        self.e1.place(x=120,y=0)

        self.e2=tk.Entry(self.master,textvariable=self.inputs)
        self.e2.place(x=120,y=30)

        self.b1=tk.Button(self.master,text="Enter",command=self.sequence,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=11,column=0,padx=10)
        self.b3=tk.Button(self.master,text="output",command=self.outputs,width=30,bg="light slate blue",activebackground="slate blue")
        self.b3.grid(row=12,column=0,padx=10)

        self.b2=tk.Button(self.master,text="Exit",command=self.close_window,width=30,bg="red3",activebackground="red")
        self.b2.grid(row=13,column=0,padx=10)

        self.t1=tk.Text(self.master,width=80,height=20)
        self.t1.grid(row=0,column=1)
        # self.quit = tk.Button(self.frame, text = f"Quit this window n. {number}", command = self.close_window)
        # self.quit.pack()
        # self.frame.pack()

    def sequence(self):
        patt = self.pattern.get()
        inp = self.inputs.get()

        def split(l):
            return list(l)

        patt_list = split(patt)
        inp_list = split(inp)


        temp = []
        z = []

        for p in range(len(patt_list)):

            for s in range(len(patt_list)):
                temp.insert(s,patt_list[s])

            for q in range(len(inp_list)):

                st = ""
                temp[p] = inp_list[q]
                z1 = st.join(temp)
                z.append(z1)
            del temp[:]
        self.output = (p+1)*(q+1)
        for i in range(len(z)):
            self.t1.insert("end",str(z[i]) + "\n")
            # labels[i].place(x=20,y=30+(20*i))

    def outputs(self):
        self.t1.insert("end", "No. of outputs:: " + str(self.output))

    def close_window(self):
        self.master.destroy()

class Win3:
    def __init__(self, master, number):
        self.master = master
        # self.master.geometry("400x400+200+200")
        # self.frame = tk.Frame(self.master)
        self.master.title("Permutations")
        self.master.config(bg="gray85")

        self.pattern = tk.StringVar()
        self.other = tk.StringVar()
        self.intother = tk.StringVar()

        self.l1 = tk.Label(self.master,text="Sequence")
        self.l1.place(x=0,y=0)

        self.l2 = tk.Label(self.master,text="Other Sequence")
        self.l2.place(x=0,y=30)

        self.l3 = tk.Label(self.master,text="Integer")
        self.l3.place(x=0,y=60)

        self.e1=tk.Entry(self.master,textvariable=self.pattern)
        self.e1.place(x=120,y=0)

        self.e2=tk.Entry(self.master,textvariable=self.other)
        self.e2.place(x=120,y=30)

        self.e3=tk.Entry(self.master,textvariable=self.intother)
        self.e3.place(x=120,y=60)

        self.b1=tk.Button(self.master,text="Add",command=self.add,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=8,column=0,padx=10)

        self.b2=tk.Button(self.master,text="Add to left",command=self.ladd,width=30,bg="light slate blue",activebackground="slate blue")
        self.b2.grid(row=9,column=0,padx=10)

        self.b1=tk.Button(self.master,text="Multiply",command=self.mul,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=10,column=0,padx=10)

        self.b1=tk.Button(self.master,text="Complement",command=self.complement,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=11,column=0,padx=10)

        self.b=tk.Button(self.master,text="Exit",command=self.close_window,width=30,bg="red3",activebackground="red")
        self.b.grid(row=12,column=0,padx=10)

        self.t1=tk.Text(self.master,width=80,height=20)
        self.t1.grid(row=0,column=1)

    def add(self):
        add = Seq(self.pattern.get()) + str(self.other.get())
        self.t1.insert("end","\n" + "Added Sequence:: " + add)

    def mul(self):
        mul = Seq(self.pattern.get()) * int(self.intother.get())
        self.t1.insert("end","\n" + "Multiplied Sequence::" + mul)

    def ladd(self):
        ladd = str(self.other.get()) + Seq(self.pattern.get())
        self.t1.insert("end","\n" + "Added Sequence:: " + ladd)

    def complement(self):
        complement = Seq(self.pattern.get()).complement()
        self.t1.insert("end","\n" + "Complement:: " + complement)

    def close_window(self):
        self.master.destroy()

class Win4:
    def __init__(self, master, number):
        self.master = master
        # self.master.geometry("400x400+200+200")
        # self.frame = tk.Frame(self.master)
        self.master.title("Amino acid operations")
        self.master.config(bg="gray85")

        self.pattern = tk.StringVar()
        self.other = tk.StringVar()
        self.phVal = tk.StringVar()

        self.l1 = tk.Label(self.master,text="Sequence")
        self.l1.place(x=0,y=0)

        self.l2 = tk.Label(self.master,text="Amino acid")
        self.l2.place(x=0,y=30)

        self.l3 = tk.Label(self.master,text="charge at pH")
        self.l3.place(x=0,y=60)

        self.e1=tk.Entry(self.master,textvariable=self.pattern)
        self.e1.place(x=120,y=0)

        self.e2=tk.Entry(self.master,textvariable=self.other)
        self.e2.place(x=120,y=30)

        self.e3=tk.Entry(self.master,textvariable=self.phVal)
        self.e3.place(x=120,y=60)

        self.b1=tk.Button(self.master,text="Calculate",command=self.AminoCount,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=8,column=0,padx=10)

        self.b2=tk.Button(self.master,text="Amino Count",command=self.AminoCountSp,width=30,bg="light slate blue",activebackground="slate blue")
        self.b2.grid(row=9,column=0,padx=10)

        self.b1=tk.Button(self.master,text="Isoelectric Point",command=self.IsoPoint,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=10,column=0,padx=10)

        self.b1=tk.Button(self.master,text="Chage at pH",command=self.pHcharge,width=30,bg="light slate blue",activebackground="slate blue")
        self.b1.grid(row=11,column=0,padx=10)

        self.b=tk.Button(self.master,text="Exit",command=self.close_window,width=30,bg="red3",activebackground="red")
        self.b.grid(row=12,column=0,padx=10)

        self.t1=tk.Text(self.master,width=80,height=20)
        self.t1.grid(row=0,column=1)

    def AminoCount(self):
        X = PepTool(self.pattern.get())
        self.t1.insert("end","\n" + "Amino Counts:: " + str(X.amino_count()))

    def AminoCountSp(self):
        X = PepTool(self.pattern.get())
        Y = self.other.get()
        self.t1.insert("end","\n" + "Amino Count of " + Y + "::" + str(X.amino_count()[Y]))

    def IsoPoint(self):
        X = PepTool(self.pattern.get())
        self.t1.insert("end","\n" + "Isoelectric Point:: " + str(X.isoelectric_point()))

    def pHcharge(self):
        X = PepTool(self.pattern.get())
        pH = self.phVal.get()
        self.t1.insert("end","\n" + "Charge at pH " + pH + ":: " + str(X.charge_at_pH(float(pH))))

    def close_window(self):
        self.master.destroy()


root = tk.Tk()
app = Win1(root)
root.mainloop()
