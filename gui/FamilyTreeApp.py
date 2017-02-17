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
		# We'll use the flexible pack layout manager
		self.pack()

		# create entry name
		self.entryFamilyName = Entry(self.master, width=300)
		self.entryFamilyName.pack()
		self.entryFamilyName.insert(0, "CURRENT FAMILY: ")

		# create menu bar
		menuBar = Menu(self.master)

		# create menu file
		menuFile = Menu(menuBar, tearoff=0)
		menuFile.add_command(label="New family", command=self.onClickNewFamily)
		menuFile.add_command(label="Choose an existed family", command=self.onClickChooseFamily)
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
		global popup
		global entry

		def onClickCreateFamily():
			global popup
			global entry
			currentFamilyName = entry.get()
			self.currentFamily = FamilyTree(currentFamilyName)
			popup.destroy()
			# create entry
			log = " CURRENT FAMILY: "+currentFamilyName+"'s family "
			self.entryFamilyName.delete(0, END)
			self.entryFamilyName.insert(0, log)

		popup = Toplevel()
		label = Label(popup, text="Create a family")
		label.pack()
		entry = Entry(popup)
		entry.pack()
		value = ""
		createButton = Button(popup, text='Create', \
			command=onClickCreateFamily)
		createButton.pack()

	def onClickChooseFamily(self):
		print("choose family")

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