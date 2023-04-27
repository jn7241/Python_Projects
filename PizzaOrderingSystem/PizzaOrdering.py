import tkinter as tk 
import pizza

options = pizza.pizza()

form = tk.Tk()
form.title("Pizza Ordering System")
form.geometry("450x350")
form.minsize(width=350, height=250)

label = tk.Label(text = "Pizza Ordering System")
label.config(font = ("arial", 18, "bold"))
label.pack()

pizzaSize = tk.StringVar()
sizeOptions = tk.OptionMenu(form, pizzaSize, *options.pizzaSize)
pizzaSize.set("--Select pizza size--")
sizeOptions.pack()

other1val = tk.StringVar(value = 0)
other1 =  tk.Checkbutton(form, variable = other1val, text = "Pepperoni")
other1.pack()

other2val = tk.StringVar(value = 0)
other2 = tk.Checkbutton(form, variable = other2val, text = "Extra cheese")
other2.pack()

drinkType = tk.StringVar()

typeOptions = tk.OptionMenu(form, drinkType, *options.drinkType)
drinkType.set("--Select drink--")
typeOptions.pack()

result = tk.Text(form, width = 40, height = 5)
result.pack()

def SubmitOrder():
    print(f"Pizza type: {pizzaSize.get()}")
    print(f"Pepperonni: {other1val.get()}")
    print(f"Extra cheese: {other2val.get()}")
    print(f"Drink: {drinkType.get()}")
    print(result.get("1.0", tk.END))
          
submission = tk.Button(text = "Order", height = 5, width = 15, command = SubmitOrder)
submission.pack()






form.mainloop()


