from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles
miles_label = Label(text="Miles", font=("Ariel", 14))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Equal
is_equal = Label(text="is equal to", font=("Ariel", 14))
is_equal.grid(column=0, row=1)
is_equal.config(pady=10, padx=10)


# Kilometer result
kilometer_result_label = Label(text="0", font=("Ariel", 14))
kilometer_result_label.grid(column=1, row=1)

# Kilometer label
kilometer_label = Label(text="km", font=("Ariel", 14))
kilometer_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(pady=10, padx=10)



window.mainloop()
