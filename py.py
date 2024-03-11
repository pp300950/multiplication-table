import tkinter as tk

window = tk.Tk()

def show_output():
    # ดึงข้อมูล
    user = int(input_var.get())
    
    output = ' '
    for i in range(1,13):
        output += str(user) + ' x ' + str(i)
        output += ' = ' + str(user * i) + '\n'
        
    output_label.configure(text=output)

title_label = tk.Label(master = window , text ='เเม่สูตรคูณ')
title_label.pack()

input_var = tk.StringVar()

text_input = tk.Entry(master = window , textvariable = input_var)
text_input.pack()

ok_button = tk.Button(master = window , text = 'ได้เเก่' , command = show_output)
ok_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()