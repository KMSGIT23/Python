#1
import calendar
c=calendar.TextCalendar()
m=c.formatmonth(2021, 2)
print(m)

#2
import tkinter as tk

s="Life is short\nUse Python"

root=tk.Tk()
t=tk.Text(root, height=2, width=13)
t.insert(tk.END, s)
t.pack()
tk.mainloop()

#3
import calendar
import tkinter as tk

c=calendar.TextCalendar()
m=c.formatmonth(2021, 3)

root=tk.Tk()
t=tk.Text(root, height=7, width=20)
t.insert(tk.END, m)
t.pack()
tk.mainloop()
