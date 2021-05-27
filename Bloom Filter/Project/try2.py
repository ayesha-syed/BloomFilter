# LISTBOX
import tkinter
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import *  
from tkinter import messagebox  
from tkdocviewer import *
from ttkthemes import themed_tk as tk 
from tkinter import ttk
# from tkinter.ttk import *

class Window:
 
	def __init__(self):
		self.root = Tk()
		# self.root.get_themes()
		# self.root.set_theme("plastik")
		self.root.title("Article Search")
		self.root.geometry("1920x1080")
		# self.root.attributes('-fullscreen', True)
		self.A = ["sample", "DSA" , "DS2", "Dime", "Pizza", "Cheese", "Pepperoni" , "Pepper","Foodandhealth_TheBlackwellEncyclopediaofSociology"]  ### EXAMPLE LIST HAS TO BE ARTICLE LIST
		self.widgets()
		self.CHECK()
		self.root.mainloop()
	
	#CREATING WIDGETS ...........................................

	def widgets(self):
		self.createLabel()
		self.create_entry()
		self.create_listbox()
		self.create_Menu()
		self.create_Button()
		

	def create_PDF(self,event):
		# Window.a = self.my_list.get(self.my_list.curselection())
		# PDF()

		self.a = self.my_list.get(self.my_list.curselection())
		self.v = DocViewer(self.root)
		self.v.place(relx = 0.45, y = 500,anchor = CENTER,height= 900,width = 700)
		# Display some document
		self.v.display_file("PDFs/"+str(self.a)+".pdf")
		self.create_SuggestionLabels()


    def create_Canvas(self):
        




	def open_OP1(self,event):
    		# Window.a = self.my_list.get(self.my_list.curselection())
		# PDF()

		self.a = self.option1['text']
		self.v = DocViewer(self.root)
		self.v.place(relx = 0.45, y = 500,anchor = CENTER,height= 900,width = 700)
		# Display some document
		self.v.display_file("PDFs/"+str(self.a)+".pdf")
		self.create_SuggestionLabels()
	
	def open_OP2(self,event):
    		# Window.a = self.my_list.get(self.my_list.curselection())
		# PDF()

		self.a = self.option2['text']
		self.v = DocViewer(self.root)
		self.v.place(relx = 0.45, y = 500,anchor = CENTER,height= 900,width = 700)
		# Display some document
		self.v.display_file("PDFs/"+str(self.a)+".pdf")
		self.create_SuggestionLabels()

	def create_entry(self):
		self.my_entry = Entry(self.root, font=("Helvetica",20))
		self.my_entry.place(x = 300, y = 100,anchor = CENTER)

	def createLabel(self):
		self.my_label = Label(self.root, text = "Search Here ", font = ("Helvetica",14),fg = "grey")
		self.my_label.place(x =70, y = 100,anchor = CENTER)
	
	
	def create_listbox(self): 		# Create List Box
		self.my_list = Listbox(self.root,width = 50)
		self.my_list.place(x = 200,y = 300,anchor = CENTER)
		self.my_list.place_forget()

	def create_Menu(self):
		self.mainMenu = Menu(self.root)  # Creates a Main Menu 
		self.m1 = Menu(self.mainMenu, tearoff=0)		#m1 is the sub menu options
		self.m1.add_command(label="Help", command=self.hello)    
		self.m1.add_command(label="Quit",command = self.exitProgram)  
		self.mainMenu.add_cascade(label="Options", menu=self.m1)
		
		self.root.config(menu=self.mainMenu)


	# Creating The Suggestion Options 
	def create_SuggestionLabels(self):
		self.Heading = Label(self.root, text = "You may also like :", font = ("Helvetica",14),fg = "black")
		self.Heading.place(x = 1500, y = 200,anchor = CENTER)

		self.option1 = Label(self.root, text = str(self.A[0]), font = ("Helvetica",14),fg = "black",relief=GROOVE,cursor= 'hand2')
		self.option2 = Label(self.root, text = str(self.A[8]), font = ("Helvetica",14),fg = "black",relief=RAISED,cursor= 'hand2')

		self.option1.place(x = 1500, y = 240,anchor = CENTER)
		self.option2.place(x = 1500, y = 280,anchor = CENTER)

		self.option1.bind("<Button-1>", self.open_OP1)
		self.option2.bind("<Button-1>", self.open_OP2)
    	

	# def sunk_Label(self,event):
    # 	pass


	# Triggering Event Fucntion
	def CHECK(self):	
		self.my_entry.bind("<KeyRelease>",self.check)   # Triggers check() whenever a key is pressed on search box
		self.my_list.bind('<<ListboxSelect>>', self.create_PDF)   # Triggers clickEvent() whenever you click on a item in the listbox
		

	# FUNCTIONS THAT WORK ON SOME EVENTS ......................
	def hello(self):
		messagebox.showinfo("Info","helo")

	def exitProgram(self):
		exit()

	def check(self,event):
		#grab what was typed
		self.typed = self.my_entry.get()

		if self.typed == "":	## NEED TO IMPLEMENT A BETTER SEARCH CODE LIKE TRIES OR INVERTED INDEX
			self.data = []
 		# my_list.place(relx = 0.1,y = -2200,anchor = CENTER)     # not a good mehtod xddd
			self.my_list.place_forget()
		else:
			self.data = []
			for item in self.A:
				if self.typed.lower() in item.lower():
					self.data.append(item)
			# my_list.place(relx = 0.5,y = 200,anchor = CENTER)
			self.my_list.place_configure(x = 147,y = 120,height = len(self.data)*20)
		#update listbox with selected item
		self.update(self.data)

	def update(self,data):
            # Clear List Box
		self.my_list.delete(0, END)

        # adding Article to List Box
		for item in data:
			self.my_list.insert(END,item)
	
	def clickEvent(self,event):
    	# SHows a message box whatever is clicked on messagebox
		self.a = self.my_list.get(self.my_list.curselection())
		messagebox.showinfo("Info",self.a)
	
	def create_Button(self):
		self.B = Button(self.root, text ="Exit", command = self.GoBack)
		self.B.place(x = 20 , y = 600)

	def GoBack(self):
		self.root.destroy()
 
# class PDF():
     
# 	def __init__(self):
# 		self.top = Toplevel()
# 		self.top.title("View PDF")
# 		self.top.geometry("1920x1080")
# 		# self.top.attributes('-fullscreen', True)
# 		self.widgets()
# 		self.top.mainloop()
	
# 	#CREATING WIDGETS ...........................................

# 	def widgets(self):
# 		self.create_PDF()
# 		self.create_Button()
	
# 	def create_PDF(self):
# 		pass

# 	def create_Button(self):
# 		self.B = Button(self.top, text ="Exit", command = self.GoBack)
# 		self.B.place(x = 20 , y = 10)

# 	def GoBack(self):
# 		self.top.destroy()
		
		




Window()