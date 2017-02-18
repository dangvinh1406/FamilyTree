import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd()+"../../"))

from Tkinter import *

from core.FamilyTree import *
from core.Person import *
 
class FamilyTreeApp(Frame):
	def __init__(self, master):

		# family tree
		self.currentFamily = None

		# Initialize window using the parent's constructor
		Frame.__init__(self, master, width=800, height=600)

		# Set the title
		self.master.title('Family Tree Application')
		# This allows the size specification to take effect
		self.pack_propagate(0)
		# Fixed size window
		self.master.resizable(width=False, height=False)
		self.pack()

		# create label family name
		self.varFamilyName = StringVar(value="Family name")
		self.labelFamilyName = Label(self.master, textvariable=self.varFamilyName, \
			font=("Helvetica", 16))
		self.labelFamilyName.pack()

		# create person information area
		self.textPersonList = Text(self, width=70)
		scrollbar = Scrollbar(self, orient="vertical", command=self.textPersonList.yview)
		self.textPersonList.configure(yscrollcommand=scrollbar.set)
		scrollbar.pack(side="left", fill="y")
		self.textPersonList.pack(side="left", fill="both", expand=False)
		self.textPersonList.bind("<Key>", lambda e: "break")

		# create menu bar
		menuBar = Menu(self.master)

		# create menu file
		menuFile = Menu(menuBar, tearoff=0)
		menuFile.add_command(label="New family", command=self.onClickNewFamily)
		menuFile.add_command(label="Choose an existed family", command=self.onClickChooseFamily)
		menuFile.add_command(label="Save family", command=self.onClickSaveFamily)
		menuFile.add_separator()
		menuFile.add_command(label="Exit", command=self.master.quit)
		menuBar.add_cascade(label="File", menu=menuFile)

		# create menu help
		menuHelp = Menu(menuBar, tearoff=0)
		menuHelp.add_command(label="Instruction", command=self.onClickInstruction)
		menuHelp.add_command(label="About", command=self.onClickAbout)
		menuBar.add_cascade(label="Help", menu=menuHelp)

		# display menu
		self.master.config(menu=menuBar)

	def onClickNewFamily(self):
		def onClickCreateFamily():
			global popup
			global entry
			currentFamilyName = entry.get()
			self.currentFamily = FamilyTree(currentFamilyName)
			popup.destroy()
			# edit currentFamilyName
			self.varFamilyName.set(currentFamilyName+"'s family")

		def createNewFamily():
			global popup
			global entry
			popup = Toplevel()
			label = Label(popup, text="Create a family")
			label.pack()
			entry = Entry(popup)
			entry.pack()
			value = ""
			createButton = Button(popup, text='Create', \
				command=onClickCreateFamily)
			createButton.pack()

		def onClickYes():
			self.onClickSaveFamily()
			apopup.destroy()
			createNewFamily()

		def onClickNo():
			apopup.destroy()
			createNewFamily()

		if self.currentFamily is not None:
			apopup = Toplevel()
			alabel = Label(apopup, text="Would you like to save current family?")
			alabel.pack()
			yesButton = Button(apopup, text='Yes', \
				command=onClickYes)
			yesButton.pack()
			noButton = Button(apopup, text='No', \
				command=onClickNo)
			noButton.pack()
		else:
			createNewFamily()


	def onClickSaveFamily(self):
		print("save family")

	def onClickChooseFamily(self):
		self.textPersonList.insert(END, 'Family information')

	def onClickInstruction(self):
		print("instruction")

	def onClickAbout(self):
		print("about")

	def run(self):
		''' Run the app '''
		self.mainloop()

if __name__ == '__main__':
	app = FamilyTreeApp(Tk())
	app.run()