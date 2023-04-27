import tkinter as tk


class App(tk.Frame):

    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        
        
        weightList = ["kilogram", "pound", "ounze"]
        distanceList = ["kilometer", "meter", "mile", "yard"]
        temperatureList = ["celsius", "fahrenheit", "kelvin"]
    
    
        self.dict = {'weight': weightList,
                     'distance': distanceList,
                     'temperature': temperatureList}
       
        
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
    
        self.variable_a.trace('w', self.update_options)
    
        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')
    
        self.variable_a.set('weight')
        
        
        self.optionmenu_a.place(relx = 0.1, rely = 0.1)
        self.optionmenu_b.place(relx = 0.75, rely = 0.1)
        
        self.pack(fill = "both", expand = 1)
        
        
       
    
    def update_options(self, *args):
        Units = self.dict[self.variable_a.get()]
        self.variable_b.set(Units[0])
    
        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')
    
        for i in Units:
            menu.add_command(label=i, command=lambda current=i: self.variable_b.set(current))

    def calc():
        if win.variable_a.get() == "weight":
            km.config(text="kilometers")
            m.config(text ="meters")
            mll.config(text = "miles")
            y.config(text = "yards")
            c.config(text = "celsius")
            f.config(text = "fahrenheit")
            k.config(text = "kelvin")
            if win.variable_b.get() == "kilogram":
                kg.config(text = str(amount.get())+ " kg")
                
                res = 2.2046 * float(amount.get())
                
                p.config(text = str(round(res, 4)) + " lb")

                res = 35.274 * float(amount.get())

                o.config(text = str(round(res, 4)) + " oz.")

            if win.variable_b.get() == "pound":
                p.config(text = str(amount.get())+ " lb")
                
                res = float(amount.get()) / 2.205

                kg.config(text = str(round(res, 4)) + " kg")

                res = 16.0 * float(amount.get())

                o.config(text = str(round(res, 4)) + " oz.")
                
            if win.variable_b.get() == "ounze":
                o.config(text = str(amount.get())+ " oz.")
                
                res = float(amount.get()) / 35.274

                kg.config(text = str(round(res, 4)) + " kg")

                res = float(amount.get()) / 16.0

                p.config(text = str(round(res, 4)) + " lb")
            
        if win.variable_a.get() == "distance":
            kg.config(text="kilograms")
            p.config(text ="pounds")
            o.config(text = "ounces")
            c.config(text = "celsius")
            f.config(text = "fahrenheit")
            k.config(text = "kelvin")
            if win.variable_b.get() == "kilometer":
                km.config(text = str(amount.get())+ " km")
                
                res = float(amount.get()) * 1000.0

                m.config(text = str(round(res, 4)) + " m")

                res = float(amount.get()) * 0.62137119

                mll.config(text = str(round(res, 4)) + " mi.")

                res = float(amount.get()) * 1094

                y.config(text = str(round(res, 4)) + " yd")
                                

            if win.variable_b.get() == "meter":
                m.config(text = str(amount.get())+ " m")
                
                res = float(amount.get()) / 1000.0

                km.config(text = str(round(res, 4)) + " km")

                res = float(amount.get()) * 0.00062137

                mll.config(text = str(round(res, 4)) + " mi.")

                res = float(amount.get()) * 1.0936

                y.config(text = str(round(res, 4)) + " yd")
                
                
            if win.variable_b.get() == "mile":
                mll.config(text = str(amount.get())+ " mi.")
                
                res = float(amount.get()) * 1.609344

                km.config(text = str(round(res, 4)) + " km")

                res = float(amount.get()) * 1609.344

                m.config(text = str(round(res, 4)) + " m")

                res = float(amount.get()) * 1760.0

                y.config(text = str(round(res, 4)) + " yd")

                
            if win.variable_b.get() == "yard":
                y.config(text = str(amount.get())+ " yd")
                
                res = float(amount.get()) * 0.000914

                km.config(text = str(round(res, 4)) + " km")

                res = float(amount.get()) * 0.9144

                m.config(text = str(round(res, 4)) + " m")

                res = float(amount.get()) / 1760.0

                mll.config(text = str(round(res, 4)) + " mi.")

                
        if win.variable_a.get() == "temperature":
            kg.config(text="kilograms")
            p.config(text ="pounds")
            o.config(text = "ounces")
            km.config(text="kilometers")
            m.config(text ="meters")
            mll.config(text = "miles")
            y.config(text = "yards")
            
            if win.variable_b.get() == "celsius":
                c.config(text = str(amount.get())+ " C" + u"\u00b0")
                
                res = (float(amount.get())* 1.8) + 32.0
                
                f.config(text = str(round(res, 4)) + " F" + u"\u00b0")

                res = float(amount.get()) + 273.15

                k.config(text = str(round(res, 4)) + " K")

                
            if win.variable_b.get() == "fahrenheit":
                f.config(text = str(amount.get())+ " F" + u"\u00b0")
                
                res = ((float(amount.get()) - 32.0) * 5.0)/9.0
                
                c.config(text = str(round(res, 4)) + " C" + u"\u00b0")

                res = (5 * (float(amount.get())-32) / 9) + 273.15
                
                k.config(text = str(round(res, 4)) + " K")

                
            if win.variable_b.get() == "kelvin":
                k.config(text = str(amount.get())+ " K")
                
                res = float(amount.get()) - 273.15
                
                c.config(text = str(round(res, 4)) + " C" + u"\u00b0")

                res = (1.8 * (float(amount.get())-273.15 ))  + 32
                            
                f.config(text = str(round(res, 4)) + " F" + u"\u00b0")


win = tk.Tk()
win.title("Unit Converter")
win.geometry("500x300")
win = App(win)

#amount
tk.Label(win, text = "Amount").place(relx = 0.35, rely = 0.12)
amount = tk.Entry(win)
amount.place(relx = 0.45, rely = 0.12)

# get button

get = tk.Button(win, text= "get result", command = App.calc)
get.place(relx = 0.45, rely = 0.2)


#OUTPUTS

# WEIGHTS

kg = tk.Label(text= "kilograms")

kg.place(relx = 0.1, rely = 0.5)



p = tk.Label(text= "pounds")

p.place(relx = 0.45, rely = 0.5)


o = tk.Label(text= "ounze")

o.place(relx = 0.8, rely = 0.5)

# DISTANCES

km = tk.Label(text= "kilometres")

km.place(relx = 0.1, rely = 0.7)


m = tk.Label(text= "meters")

m.place(relx = 0.35, rely = 0.7)


mll = tk.Label(text= "miles")

mll.place(relx = 0.6, rely = 0.7)


y = tk.Label(text= "yards")

y.place(relx = 0.8, rely = 0.7)

#TEMPERATURES
c = tk.Label(text= "celsius")

c.place(relx = 0.1, rely = 0.9)



f = tk.Label(text= "fahrenheit")

f.place(relx = 0.45, rely = 0.9)


k = tk.Label(text= "kelvin")

k.place(relx = 0.8, rely = 0.9)

win.mainloop()

