from tkinter import *

class SimpleFrame:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        bar1 = Frame(frame)
        bar2 = Frame(frame)
        bar3 = Frame(frame)
        bar4 = Frame(frame)
        bar5 = Frame(frame)
        bar6 = Frame(frame)
        bar7 = Frame(frame)
        bar8 = Frame(frame)

        self.q1 = Label(bar1, text="Please rate your overall experience.")
        self.q2 = Label(bar2,
                        text="Do you plan to attend future events sponsored by USF's Center for Asia Pacific Studies?")
        self.q3 = Label(bar3, text="How did you hear about this event?")
        self.q4 = Label(bar4,
                        text="How likely are you to recommend the Center's activites to friends, families, or colleagues?")

        self.q5 = Label(bar5, text="Is there anything about our events that we could improve in the future?")
        self.q6 = Label(bar6, text="What other topics would you like us to explore?")
        self.q7 = Label(bar7, text="Do you have any other comments?")
        self.q8 = Label(bar8, text="Email?")

        self.a5 = Entry(bar5)
        self.a6 = Entry(bar6)
        self.a7 = Entry(bar7)
        self.a8 = Entry(bar8)

        self.submit = Button(frame, text="Submit", command=self.doNothing)

        self.q1.pack(side=LEFT, padx=2, pady=2)
        a1 = IntVar()
        for i in range(10):
            Radiobutton(bar1, text=str(i), variable=a1, value=i).pack(side=LEFT)
        bar1.pack(side=TOP, fill=X)

        self.q2.pack(side=LEFT, padx=2, pady=2)
        a2 = IntVar()
        Radiobutton(bar2, text='yes', variable=a2, value=1).pack(side=LEFT)
        Radiobutton(bar2, text='no', variable=a2, value=2).pack(side=LEFT)
        Radiobutton(bar2, text='undecided', variable=a2, value=3).pack(side=LEFT)
        bar2.pack(side=TOP, fill=X)

        self.q3.pack(side=LEFT, padx=2, pady=2)
        a3 = IntVar()
        Radiobutton(bar3, text='eventbrite', variable=a3, value=1).pack(side=LEFT)
        Radiobutton(bar3, text='center email', variable=a3, value=2).pack(side=LEFT)
        Radiobutton(bar3, text='poster', variable=a3, value=3).pack(side=LEFT)
        Radiobutton(bar3, text='website', variable=a3, value=4).pack(side=LEFT)
        Radiobutton(bar3, text='other', variable=a3, value=5).pack(side=LEFT)
        bar3.pack(side=TOP, fill=X)

        self.q4.pack(side=LEFT, padx=2, pady=2)
        a4 = IntVar()
        for i in range(10):
            Radiobutton(bar4, text=str(i), variable=a4, value=i).pack(side=LEFT)
        bar4.pack(side=TOP, fill=X)

        self.q5.pack(side=LEFT, padx=2, pady=2)
        self.a5.pack(side=LEFT)
        self.q6.pack(side=LEFT, padx=2, pady=2)
        self.a6.pack(side=LEFT)
        self.q7.pack(side=LEFT, padx=2, pady=2)
        self.a7.pack(side=LEFT)
        self.q8.pack(side=LEFT, padx=2, pady=2)
        self.a8.pack(side=LEFT)

        bar5.pack(side=TOP, fill=X)
        bar6.pack(side=TOP, fill=X)
        bar7.pack(side=TOP, fill=X)
        bar8.pack(side=TOP, fill=X)

        self.submit.pack(side=LEFT, padx=2, pady=2)

    def doNothing(self):
        print("")


# we can fix it by making the colmnspan or something similar bigger for the long word options

root = Tk()
root.title("USF Center for Asia Pacific Studies")
frame = SimpleFrame(root)
root.mainloop()