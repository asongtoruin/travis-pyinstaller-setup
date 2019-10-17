#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Label


root = Tk()
text = Label(root, text='Hello World')
text.grid(row=1, column=1)
root.mainloop()
