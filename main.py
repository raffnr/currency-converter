from tkinter import Tk, ttk
from tkinter import *
from currencies import list_currencies
import requests


# Color
cor0 = "#FFFFFF"  # putih
cor1 = "#333333"  # hitam
cor2 = "#EB5D51"  # merah


# Convertion function
def convert ():
    host = 'api.frankfurter.app'
    from_currency = from_curr_combobox.get()
    to_currency = to_curr_combobox.get()
    amount = amount_entry.get()

    if from_currency == to_currency:
        result['text'] = f'{to_currency[:3]}' + " {:,.2f}".format(float(amount))
    else:
        convert_response = requests.get(f'https://{host}/latest?amount={amount}&from={from_currency[:3]}&to={to_currency[:3]}')
        convert_result = convert_response.json()
        rates_result = convert_result['rates'][to_currency[:3]]
        formatted = to_currency[:3] + " " + " {:,.2f}".format(rates_result)

        result['text'] = formatted


# Window
window = Tk()
window.geometry('600x640')
window.title('Konversi Mata Uang')
window.configure(bg=cor0)
window.resizable(height=True, width=True)

# Main Frame
frame = Frame(window, width=300, height=260, bg=cor0, pady=60)
frame.pack()

# Result frame
result_frame = Frame(frame)
result_frame.grid(row= 0, column=0, padx=20, pady=10)
result = Label(result_frame, text = " ",width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
result.grid(row=0, column=0)

# Currency input frame
curr_input_frame = Frame(frame, bg=cor0)
curr_input_frame.grid(row= 1, column=0, padx=20, pady=10)

from_curr_label = Label(curr_input_frame, text="From", bg=cor0)
from_curr_combobox = ttk.Combobox(curr_input_frame, values=list_currencies)
from_curr_label.grid(row=0, column=0)
from_curr_combobox.grid(row=1, column=0)

to_curr_label = Label(curr_input_frame, text="To", bg=cor0)
to_curr_combobox = ttk.Combobox(curr_input_frame, values=list_currencies)
to_curr_label.grid(row=0, column=2)
to_curr_combobox.grid(row=1, column=2)

for widget in curr_input_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Amount Frame
amount_frame = Frame(frame, bg=cor0)
amount_frame.grid(row= 2, column=0, padx=20, pady=10)

amount_label = Label(amount_frame, text='Masukan Nominal', bg=cor0)
amount_label.grid(row=0, column=0)

amount_entry = Entry(amount_frame, width=50, relief=SOLID)
amount_entry.grid(row=1, column=0)

for widget in amount_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button Frame
button_frame = Frame(frame, bg=cor0)
button_frame.grid(row= 3, column=0, padx=20, pady=10)

button = Button(button_frame, text="Convert", width=19, padx=5, height=1, bg=cor1, fg=cor0 ,font=("Ivy 12 bold"), command=convert)
button.grid(row=0, column=0)

window.mainloop()



