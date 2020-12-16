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
        self.master.config(bg="gray26")

        self.butnew("Permutations", "2", Win2)
        self.butnew("Operational", "3", Win3)
        self.butnew("Amino Acid Count", "4", Win4)
        self.B = tk.Button(self.master,text="Exit",command=self.stop,relief="raised",bd=6,bg="red3",activebackground="red4",width=30).pack()
        # self.frame.pack()

    def butnew(self, text, number, _class):
        tk.Button(self.master, text = text,bd=6,relief='raised', command= lambda: self.new_window(number, _class),
        height=5,width=30,bg="green3",activebackground="green4").pack()

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
        self.master.config(bg="light steel blue")

        self.pattern = tk.StringVar()
        self.inputs = tk.StringVar()

        self.l1 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="Pattern")
        self.l1.place(x=0,y=30)

        self.l2 = tk.Label(self.master,relief="groove",bd=4,text="Inputs")
        self.l2.place(x=0,y=60)

        self.e1=tk.Entry(self.master,bd=4,textvariable=self.pattern)
        self.e1.place(x=120,y=30)

        self.e2=tk.Entry(self.master,bd=4,textvariable=self.inputs)
        self.e2.place(x=120,y=60)

        self.b1=tk.Button(self.master,text="Sequencer",command=self.sequence,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b1.grid(row=10,column=0,padx=10)

        self.b4=tk.Button(self.master,text="X Sequencer",command=self.Xsequence,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b4.grid(row=11,column=0,padx=10)

        self.b3=tk.Button(self.master,text="output",command=self.outputs,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b3.grid(row=12,column=0,padx=10)

        self.b2=tk.Button(self.master,text="Exit",command=self.close_window,width=30,bd=4,bg="red3",activebackground="red")
        self.b2.grid(row=13,column=0,padx=10)

        self.b=tk.Button(self.master,text="Clear",command=self.clear,width=30,bd=4,bg="red3",activebackground="red")
        self.b.grid(row=14,column=0,padx=10)

        self.t1=tk.Text(self.master,bd=4,width=80,height=20)
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

    def Xsequence(self):
        patt = self.pattern.get()
        inp = self.inputs.get()

        def split(l):
            return list(l)

        patt_list = split(patt)
        inp_list = split(inp)


        temp = []
        z = []
        self.t1.insert("end","Sequence - Molecular Weight - Isoelectric point\n")
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
            X = PepTool(str(z[i]))
            self.t1.insert("end",str(z[i]) + "--->" + str(X.molecular_weight()) + "--->" + str(X.isoelectric_point()) + "\n")

    def outputs(self):
        self.t1.insert("end", "No. of outputs:: " + str(self.output))

    def close_window(self):
        self.master.destroy()

    def clear(self):
        self.t1.delete('1.0',"end")

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

        self.l1 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="Sequence")
        self.l1.place(x=0,y=30)

        self.l2 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="Other Sequence")
        self.l2.place(x=0,y=60)

        self.l3 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="Integer")
        self.l3.place(x=0,y=90)

        self.e1=tk.Entry(self.master,bd=4,textvariable=self.pattern)
        self.e1.place(x=120,y=30)

        self.e2=tk.Entry(self.master,bd=4,textvariable=self.other)
        self.e2.place(x=120,y=60)

        self.e3=tk.Entry(self.master,bd=4,textvariable=self.intother)
        self.e3.place(x=120,y=90)

        self.b1=tk.Button(self.master,text="Add",command=self.add,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b1.grid(row=1,column=0,padx=10)

        self.b2=tk.Button(self.master,text="Add to left",command=self.ladd,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b2.grid(row=2,column=0,padx=10)

        self.b4=tk.Button(self.master,text="Multiply",command=self.mul,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b4.grid(row=3,column=0,padx=10)

        self.b3=tk.Button(self.master,text="Complement",command=self.complement,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b3.grid(row=4,column=0,padx=10)

        self.B1=tk.Button(self.master,text="Overlapping count",command=self.Overlap,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.B1.grid(row=1,column=1,padx=10)

        self.B2=tk.Button(self.master,text="Non-overlapping count",command=self.Nonoverlap,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.B2.grid(row=2,column=1,padx=10)

        self.B3=tk.Button(self.master,text="Find",command=self.Find,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.B3.grid(row=3,column=1,padx=10)

        self.B3=tk.Button(self.master,text="Contains?",command=self.Contains,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.B3.grid(row=4,column=1,padx=10)

        self.b=tk.Button(self.master,text="Exit",command=self.close_window,width=30,bd=4,bg="red3",activebackground="red")
        self.b.grid(row=5,column=0,padx=10)

        self.c=tk.Button(self.master,text="Clear",command=self.clear,width=30,bd=4,bg="red3",activebackground="red")
        self.c.grid(row=5,column=1,padx=10)

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

    def Overlap(self):
        patt = Seq(self.pattern.get())
        sub = str(self.other.get())
        self.t1.insert("end","\n" + "Overlapping Count of " + sub + "::" + str(patt.count_overlap(sub)))

    def Nonoverlap(self):
        patt = Seq(self.pattern.get())
        sub = str(self.other.get())
        self.t1.insert("end","\n" + "Non-overlapping Count of " + sub + "::" + str(patt.count(sub)))

    def Find(self):
        patt = Seq(self.pattern.get())
        sub = str(self.other.get())
        self.t1.insert("end","\n" + "Result of search " + sub + "::" + str(patt.find(sub)))

    def Contains(self):
        patt = Seq(self.pattern.get())
        sub = str(self.other.get())
        if sub in patt:
            self.t1.insert("end","\n" + "Result of search " + sub + "::" + "True")
        else:
            self.t1.insert("end","\n" + "Result of search " + sub + "::" + "False")

    def close_window(self):
        self.master.destroy()

    def clear(self):
        self.t1.delete('1.0',"end")

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

        self.l1 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="Sequence")
        self.l1.place(x=0,y=30)

        self.l2 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="Amino acid")
        self.l2.place(x=0,y=60)

        self.l3 = tk.Label(self.master,relief="groove",bd=4,bg="gray78",text="charge at pH")
        self.l3.place(x=0,y=90)

        self.e1=tk.Entry(self.master,bd=4,textvariable=self.pattern)
        self.e1.place(x=120,y=30)

        self.e2=tk.Entry(self.master,bd=4,textvariable=self.other)
        self.e2.place(x=120,y=60)

        self.e3=tk.Entry(self.master,bd=4,textvariable=self.phVal)
        self.e3.place(x=120,y=90)

        self.b1=tk.Button(self.master,text="Calculate",command=self.AminoCount,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b1.grid(row=8,column=0,padx=10)

        self.b2=tk.Button(self.master,text="Amino Count",command=self.AminoCountSp,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b2.grid(row=9,column=0,padx=10)

        self.b1=tk.Button(self.master,text="Isoelectric Point",command=self.IsoPoint,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b1.grid(row=10,column=0,padx=10)

        self.b1=tk.Button(self.master,text="Chage at pH",command=self.pHcharge,width=30,bd=4,bg="OliveDrab2",activebackground="OliveDrab4")
        self.b1.grid(row=11,column=0,padx=10)

        self.b=tk.Button(self.master,text="Exit",command=self.close_window,width=30,bd=4,bg="red3",activebackground="red")
        self.b.grid(row=12,column=0,padx=10)

        self.c=tk.Button(self.master,text="Clear",command=self.clear,width=30,bd=4,bg="red3",activebackground="red")
        self.c.grid(row=13,column=0,padx=10)

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

    def clear(self):
        self.t1.delete('1.0',"end")


root = tk.Tk()
app = Win1(root)
root.mainloop()
