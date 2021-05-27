# LISTBOX
import tkinter
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import *  
from tkinter import messagebox  
from tkdocviewer import *
from ttkthemes import themed_tk as tk 
from tkinter import ttk
import pdfkit
import math
import mmh3
from bitarray import bitarray
from random import shuffle
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
# from tkinter.ttk import *

Z = []
import csv
with open('articles.csv', 'r',encoding='utf8') as file:
	reader = csv.reader(file)
	for row in reader:
		Z.append(row[4])
        


class Window:
 
	def __init__(self):
		self.root = Tk()
		self.root.title("Article Search")
		self.root.geometry("1920x1080")
		self.A = Z  ### EXAMPLE LIST HAS TO BE ARTICLE LIST
		self.widgets()
		self.CHECK()
		self.Lst = []
		self.path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
		self.root.mainloop()

	
	#CREATING WIDGETS ...........................................

	def widgets(self):
		self.create_Canvas()
		self.createLabel()
		self.create_entry()
		self.create_listbox()
		self.create_Menu()
		self.create_Button()
    	
	def create_Canvas(self):
		self.canvas = Canvas(self.root,width=300, height=500,highlightbackground = "orange", highlightthickness = "5")
		# self.canvas.create_rectangle(10, 10,500, 400)
		self.canvas.place(x = 10,y = 10,height = 380,width = 485)
    	
	def create_Canvas2(self):
		self.canvas = Canvas(self.root,width=300, height=500,highlightbackground = "orange", highlightthickness = "5")
		# self.canvas.create_rectangle(10, 10,500, 400)
		self.canvas.place(x = 1220,y = 10,height = 900,width = 600)

	
	def create_PDF(self,event):
		
		# path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
		config = pdfkit.configuration(wkhtmltopdf=self.path_wkhtmltopdf)
	

		self.a = self.my_list.get(self.my_list.curselection())

		
		
		Searched_IVD = start(self.a)
		
		print(Searched_IVD)
		self.Lst = []
		with open('articles.csv', 'r',encoding='utf8') as file:
			reader = csv.reader(file)
			for row in reader:
				if row[4] != self.a:
					x = remove_punctuation(row[4])
					x = word_tokenize(x)
					x = stemming(x)
					if BLOOM(Searched_IVD,x) > 0:
						self.Lst.append(row[4])

		print("SUGGESTION : ",self.Lst)			



		with open('articles.csv', 'r',encoding='utf8') as file:
			reader = csv.reader(file)
			for row in reader:
				if row[4] == self.a:
					link = row[3]
					break
		pdfkit.from_url(link,r'.\PDFs\test1.pdf',configuration=config)
		

		self.v = DocViewer(self.root)
		self.v.place(relx = 0.45, y = 460,anchor = CENTER,height= 900,width = 700)
		# Display some document
		self.v.display_file("PDFs/test1.pdf")
		self.create_SuggestionLabels()

	def open_OP1(self,event):
    		# Window.a = self.my_list.get(self.my_list.curselection())
		# PDF()
		config = pdfkit.configuration(wkhtmltopdf=self.path_wkhtmltopdf)
		
		# Display some document
		with open('articles.csv', 'r',encoding='utf8') as file:
			reader = csv.reader(file)
			for row in reader:
				if row[4] == self.Lst[0]:
					link = row[3]
					break
		pdfkit.from_url(link,r'.\PDFs\test1.pdf',configuration=config)
		self.v = DocViewer(self.root)
		self.v.place(relx = 0.45, y = 460,anchor = CENTER,height= 900,width = 700)
		self.v.display_file("PDFs/test1.pdf")
		self.create_SuggestionLabels()
	
	def open_OP2(self,event):
    		# Window.a = self.my_list.get(self.my_list.curselection())
		# PDF()
		config = pdfkit.configuration(wkhtmltopdf=self.path_wkhtmltopdf)
		# Display some document
		with open('articles.csv', 'r',encoding='utf8') as file:
			reader = csv.reader(file)
			for row in reader:
				if row[4] == self.Lst[1]:
					link = row[3]
					break
		pdfkit.from_url(link,r'.\PDFs\test1.pdf',configuration=config)
		self.v = DocViewer(self.root)
		self.v.place(relx = 0.45, y = 460,anchor = CENTER,height= 900,width = 700)
		self.v.display_file("PDFs/test1.pdf")
		self.create_SuggestionLabels()

	def create_entry(self):
		self.my_entry = Entry(self.root, font=("Ubuntu",20))
		self.my_entry.place(x = 300, y = 100,anchor = CENTER)

	def createLabel(self):
		self.my_label = Label(self.root, text = "Search Here ", font = ("Ubuntu",14),fg = "orange")
		self.my_label.place(x =90, y = 100,anchor = CENTER)
	
	
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


	def create_SuggestionLabels(self):
    		
		if len(self.Lst) > 0:
			self.create_Canvas2()
			self.Heading = Label(self.root, text = "You may also like :", font = ("Ubuntu",14),fg = "orange")
			self.Heading.place(x = 1530, y = 30,anchor = CENTER)

			if len(self.Lst) == 1:
				self.option1 = Label(self.root, text = str(self.Lst[0]), font = ("Ubuntu",9),fg = "black",relief=RAISED,cursor= 'hand2')
				self.option1.place(x = 1530, y = 70,anchor = CENTER)
				self.option1.bind("<Button-1>", self.open_OP1)
			elif len(self.Lst) > 1:
				self.option1 = Label(self.root, text = str(self.Lst[0]), font = ("Ubuntu",9),fg = "black",relief=RAISED,cursor= 'hand2')
				self.option2 = Label(self.root, text = str(self.Lst[1]), font = ("Ubuntu",9),fg = "black",relief=RAISED,cursor= 'hand2')
				self.option1.place(x = 1530, y = 70,anchor = CENTER)
				self.option2.place(x = 1530, y = 100,anchor = CENTER)
				self.option1.bind("<Button-1>", self.open_OP1)
				self.option2.bind("<Button-1>", self.open_OP2)

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
			if len(self.data)*20 <= 300:	
				self.my_list.place_configure(x = 197,y = 120,height = len(self.data)*20)
			else:
				self.my_list.place_configure(x = 197,y = 120,height = 250)	
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
 

#######################################               BLOOM FILTER                  ###########################################################

 
class BloomFilter(object):
    '''
    Class for Bloom filter, using murmur3 hash function
    '''
    def __init__(self, items_count, fp_prob):
        '''
        items_count : int
            Number of items expected to be stored in bloom filter
        fp_prob : float
            False Positive probability in decimal
        '''
        # False posible probability in decimal
        self.fp_prob = fp_prob
 
        # Size of bit array to use
        self.size = self.get_size(items_count, fp_prob)
 
        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, items_count)
 
        # Bit array of given size
        self.bit_array = bitarray(self.size)
 
        # initialize all bits as 0
        self.bit_array.setall(0)
 
    def add(self, item):
        '''
        Add an item in the filter
        '''
        digests = []
        for i in range(self.hash_count):
 
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)
 
            # set the bit True in bit_array
            self.bit_array[digest] = True
 
    def check(self, item):
        '''
        Check for existence of an item in filter
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
 
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True
 
    @classmethod
    def get_size(self, n, p):
        '''
        Return the size of bit array(m) to used using
        following formula
        m = -(n * lg(p)) / (lg(2)^2)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        '''
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)
 
    @classmethod
    def get_hash_count(self, m, n):
        '''
        Return the hash function(k) to be used using
        following formula
        k = (m/n) * lg(2)
 
        m : int
            size of bit array
        n : int
            number of items expected to be stored in filter
        '''
        k = (m/n) * math.log(2)
        return int(k)




def BLOOM(word_present,word_absent):
	n = 20 #no of items to add
	p = 0.2 #false positive probability
	
	bloomf = BloomFilter(n,p)
	
	for item in word_present:
		bloomf.add(item)
	
	i = 0
	test_words = word_present
	for word in test_words:
		if bloomf.check(word):
			if word in word_absent:
				i = i + 1
			else: i = i - 0.2
		else:
			i = i - 0.2
	return i


#######################################                 INVERTED INDEX 		     		#####################################################

def create_InvertedIndex(D):
    dict = {}

    for item in D:
        if item not in dict:
            dict[item] = 1
        if item in dict:
            dict[item] = dict.get(item)+1

    return dict

def remove_stopwords(D):
	text_tokens = word_tokenize(D)

	tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
	return tokens_without_sw

def stemming(D):
	L = []
	porter = PorterStemmer()
	for i in D:
		a = porter.stem(i)
		L.append(a)
	return L

def remove_punctuation(D):
    punc = '''!()-[]{};:’'"\‘,“”—<>•./?@#$%^&*_~1234567890'''
    for ele in D:  
        if ele in punc:  
            D = D.replace(ele, " ")  
        
    # to maintain uniformity
    D=D.lower()                    
    return D

def start(title):    ### find term frequesncy of each word

	with open('articles.csv', 'r',encoding='utf8') as file:
		reader = csv.reader(file)
		for row in reader:
			if row[4] == title:
				D = row[5]
				D = remove_punctuation(D)
				D = remove_stopwords(D)
				D = stemming(D)
				Dict = create_InvertedIndex(D)
				return term_frequency(Dict)

def term_frequency(IVD):
	
	sort_orders = sorted(IVD.items(), key=lambda x: x[1], reverse=True)
	L = []
	i = 0

	for key,value in sort_orders:
		L.append(key)
		i += 1
		if i > 10:
			break
	
	return L

Window()