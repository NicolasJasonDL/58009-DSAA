from tkinter import *
from tkinter.ttk import *

class ShoppingCart:
    items = []

    @classmethod
    def add_item(cls, item, price):
        cls.items.append({"name": item, "price": price})

    @classmethod
    def remove_item(cls, index):
        if 0 <= index < len(cls.items):
            del cls.items[index]

    @classmethod
    def get_items(cls):
        return cls.items
class MyWindow:
    def __init__(self,window):

        self.window = window
        # Labels and items
        self.lbl1 = Label(window,text="Item List")
        self.lbl1.place(x = 120, y = 20)
        self.item1 = Label(window,text="Item1 - P10.00")
        self.item1.place(x = 25, y = 52)
        self.item2 = Label(window,text="Item2 - P20.00")
        self.item2.place(x = 25, y = 87)

        # Buttons
        self.cart = Button(window, text="My Cart", command=self.MyCart)
        self.cart.place(x=210, y=10)
        self.ibut1 = Button(window, text = "Add to Cart", command=lambda: self.add_to_cart("Item1", 10.00))
        self.ibut1.place(x = 120, y = 50)
        self.ibut2 = Button(window, text = "Add to Cart", command=lambda: self.add_to_cart("Item2", 20.00))
        self.ibut2.place(x = 120, y = 85)


    #https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/


    def MyCart(self):
        new_window = Toplevel(self.window)
        new_window.title("CpE Shop")
        new_window.geometry("300x300")
        NewWindow(new_window)

    def add_to_cart(self, item, price):
        ShoppingCart.add_item(item, price)


class NewWindow:
    def __init__(self, window):
        self.window = window

        # Label
        self.nlbl1 = Label(window, text="My Cart")
        self.nlbl1.place(x=120, y=20)

        # Listbox to display items in the cart
        self.cart_listbox = Listbox(window)
        self.cart_listbox.place(x=80, y=50)

        # Display items in the cart
        for cart_item in ShoppingCart.get_items():
            self.cart_listbox.insert(END, f"{cart_item['name']} - P{cart_item['price']:.2f}")

        # Delete Function
        delete_button = Button(window, text="Remove Selected", command=self.delete_selected)
        delete_button.place(x=100, y=220)

        self.selected_item = -1

        self.cart_listbox.bind('<ListboxSelect>>', self.on_select)

        def delete_selected(self):
            if self.delete_selected != -1:
                ShoppingCart.remove_item(self.delete_selected)
                self.cart_listbox.delete(self.delete_selected)
                self.delete_selected = -1

        def on_select(self, event):
            delete_selected = self.cart_listbox.curselection()
            if delete_selected:
                self.selected_index = int(delete_selected[0])


if __name__ == "__main__":
    window = Tk()
    window.geometry("300x300+20+10")
    window.title('CpE Shop')
    my_window = MyWindow(window)
    window.mainloop()
