
from tkinter import *  
from tkinter import messagebox  
root = Tk()  
root.title('Trying')
root.geometry("1000x500")
# Code to add widget will go here……..  


#Updating List Box

class Example(root):
    A = ["Data", "DSA" , "DS2", "Dime", "Pizza", "Cheese", "Pepperoni" , "Pepper"]



    def update(self,data):
            # Clear List Box
        my_list.delete(0, END)

        # adding Article to List Box
        for item in data:
            my_list.insert(END,item)

    # # Update Search (Entry) Box with listbox Clicked

    # def fillout(event):
    #     # Delete whatever in Entry Box
    #     my_entry.delete(0,END)

    #     #Add clicked list item to entry box
    #     my_entry.insert(0,my_list.get(ACTIVE))

    # Create Funct to check entry vs listbox

    def check(self,event):
        #grab what was typed
        
        typed = my_entry.get()

        if typed == "":
            data = []
            # my_list.place(relx = 0.1,y = -2200,anchor = CENTER)     # not a good mehtod xddd
            my_list.forget()
        else:
            data = []
            for item in A:
                if typed.lower() in item.lower():
                    data.append(item)
            # my_list.place(relx = 0.5,y = 200,anchor = CENTER)
            my_list.place_configure(relx = 0.5,y = 200,anchor = CENTER)
        #update listbox with selected item
        update(data)



    def __init__(self):
        super().__init__()
        self.createWidgets()()


    def createWidgets(self):
        # Create Label
        my_label = Label(self.root, text = "Start Typing...", font = ("Helvetica",14),fg = "grey")
        my_label.place(relx = 0.5, y = 10,anchor = CENTER)


        # Create Search Box
        my_entry = Entry(self.root, font=("Helvetica",20))
        my_entry.place(relx = 0.5, y = 50,anchor = CENTER)

        # Create List Box
        # def create_list():
        #     global my_list
        my_list = Listbox(self.root,width = 50)
        my_list.place(relx = 0.5,y = 200,anchor = CENTER)
        my_list.place_forget()

        my_entry.bind("<KeyRelease>",check)
        # Gets the selected item from the list after clicking on it
        my_list.bind('<<ListboxSelect>>', clickEvent)

   

    def clickEvent(event):
        a = my_list.get(my_list.curselection())
        messagebox.showinfo("Info",a)




    # Create Label


    
   

    # menubar = Menu(root)
    # root.config(menu=menubar)
    # fileMenu = Menu(menubar)
    # submenu = Menu(fileMenu)
    # submenu.add_command(label="New feed")





    # Article example List

    # Add Article to List Box
    # update(A)

    #create a binding on the list box onclick
    # my_list.bind("<<ListboxSelect>>",fillout)

    # create a binding on the entry box
    

def main():
    
    root = Tk()  
    root.title('Trying')
    root.geometry("1000x500")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()