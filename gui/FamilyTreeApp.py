import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd()+"../../"))

from Tkinter import *

from core.FamilyTree import *
from core.Person import *
from db.DatabaseManager import *
 
class FamilyTreeApp(Frame):
	def __init__(self, master):

		# family tree
		self.currentFamily = None
		self.database = DatabaseManager()
		self.currentFamilyId = -1

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
		self.menuBar = Menu(self.master)

		# create menu file
		self.menuFile = Menu(self.menuBar, tearoff=0)
		self.menuFile.add_command(label="New family", command=self.onClickNewFamily)
		self.menuFile.add_command(label="Choose existed family", command=self.onClickChooseFamily)
		self.menuFile.add_separator()
		self.menuFile.add_command(label="Commit all changes", command=self.onClickCommit)
		self.menuFile.add_separator()
		self.menuFile.add_command(label="Exit", command=self.master.quit)
		self.menuBar.add_cascade(label="File", menu=self.menuFile)

		# create menu edit
		self.menuEdit = Menu(self.menuBar, tearoff=0)
		self.menuEdit.add_command(label="Add person", command=self.onClickAddPerson)
		self.menuEdit.add_command(label="Edit person", command=self.onClickEditPerson)
		self.menuEdit.add_command(label="Remove person", command=self.onClickRemovePerson)
		self.menuBar.add_cascade(label="Edit", menu=self.menuEdit)
		self.menuBar.entryconfig("Edit", state="disabled")

		# create menu help
		self.menuHelp = Menu(self.menuBar, tearoff=0)
		self.menuHelp.add_command(label="Instruction", command=self.onClickInstruction)
		self.menuHelp.add_command(label="About", command=self.onClickAbout)
		self.menuBar.add_cascade(label="Help", menu=self.menuHelp)

		# display menu
		self.master.config(menu=self.menuBar)

	def onClickNewFamily(self):
		def onClickCreateFamily():
			global popup
			global entry
			currentFamilyName = entry.get()
			self.database.storeFamily(currentFamilyName)
			self.currentFamilyId = self.database.getCurrentId("family")
			self.currentFamily = FamilyTree(self.currentFamilyId, currentFamilyName)
			popup.destroy()
			# edit currentFamilyName
			self.varFamilyName.set(currentFamilyName+"'s family")

		def createNewFamily():
			global popup
			global entry
			popup = Toplevel()
			label = Label(popup, text="Family name: ")
			label.pack(side=LEFT)
			entry = Entry(popup, width=30)
			entry.pack(side=LEFT)
			value = ""
			createButton = Button(popup, width=10, text='Create', command=onClickCreateFamily)
			createButton.pack()

		def onClickYes():
			apopup.destroy()
			createNewFamily()

		def onClickNo():
			# TODO: remove all data of this family from database
			apopup.destroy()
			createNewFamily()

		self.menuBar.entryconfig("Edit", state="normal")
		if self.currentFamily is not None:
			apopup = Toplevel()
			alabel = Label(apopup, text="Would you like to store current family?")
			alabel.pack()
			yesButton = Button(apopup, width=10, text='Yes', command=onClickYes)
			yesButton.pack(side=LEFT)
			noButton = Button(apopup, width=10, text='No', command=onClickNo)
			noButton.pack(side=LEFT)
		else:
			createNewFamily()

	def onClickChooseFamily(self):
		self.textPersonList.insert(END, 'Family information')

	def onClickCommit(self):
		self.database.commit()

	def onClickAddPerson(self):
		def onClickAdd():
			name = inputName.get()
			year = int(inputYear.get())
			gender = GENDER.MALE
			try:
				gender = GENDER.fromInt(map(int, genderBox.curselection()))
			except:
				pass	
			self.database.storePerson(self.currentFamilyId, name, year, gender)
			currentPersonId = self.database.getCurrentId("person")
			person = Person(currentPersonId, name, year, gender)
			self.currentFamily.addPerson(person)
			print("[App] Added person ",currentPersonId, name, year, gender)
			popup.destroy()

		def onClickCancel():
			popup.destroy()

		popup = Toplevel()
		nameLabel = Label(popup, width=20, text="Full name:")
		nameLabel.grid(row=0, column=0)
		inputName = Entry(popup, width=30)
		inputName.grid(row=0, column=1)
		yearLabel = Label(popup, width=20, text="Year of birth:")
		yearLabel.grid(row=1, column=0)
		inputYear = Entry(popup, width=30)
		inputYear.grid(row=1, column=1)
		genderLabel = Label(popup, width=20, text="Gender:")
		genderLabel.grid(row=2, column=0)
		genderBox = Listbox(popup, selectmode=SINGLE, width=30, height=2)
		genderBox.insert(END, "MALE")
		genderBox.insert(END, "FEMALE")
		genderBox.grid(row=2, column=1)

		addButton = Button(popup, text='Add', width=10, command=onClickAdd)
		addButton.grid(row=3, column=0)
		cancelButton = Button(popup, text='Cancel', width=10, command=onClickCancel)
		cancelButton.grid(row=3, column=1)

	def onClickEditPerson(self):
		print("edit person")

	def onClickRemovePerson(self):
		print("remove person")

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