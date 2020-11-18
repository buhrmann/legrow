import tkinter as tk


class Frame(tk.Frame):
    """A drawing canvas with scroll and zoom.

    From https://www.semicolonworld.com/question/59868/move-and-zoom-a-tkinter-canvas-with-mouse
    """

    def __init__(self, root, w=400, h=400):
        tk.Frame.__init__(self, root)

        self.canvas = tk.Canvas(self, width=w, height=h)
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0, 0, 1000, 1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        root.bind("<Button-1>", self.click)
        root.bind("<B1-Motion>", self.drag)
        root.bind("<Button-4>", self.zoomer_plus)
        root.bind("<Button-5>", self.zoomer_minus)
        root.bind("<MouseWheel>", self.zoomer)

        self.pack(fill="both", expand=True)

    def click(self, event):
        print("click: ", event.x, event.y)
        self.canvas.scan_mark(event.x, event.y)

    def drag(self, event):
        print("drag: ", event.x, event.y)
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def zoomer(self, event):
        if event.delta > 0:
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif event.delta < 0:
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def zoomer_plus(self, event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def zoomer_minus(self, event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def draw(self, **kwargs):
        raise NotImplementedError

    @classmethod
    def render(cls, **kwargs):
        root = tk.Tk()
        frame = cls(root)
        frame.draw(**kwargs)
        root.mainloop()
