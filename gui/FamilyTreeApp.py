import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd()+"../../"))

from Tkinter import *

from core.FamilyTree import *
from core.Person import *
from db.DatabaseManager import *
from utils.Utils import *
 
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
		self.menuFile.add_command(label="Save all changes", command=self.onClickSave)
		self.menuFile.add_command(label="Abort all changes", command=self.onClickAbort)
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
			# update value of current family
			currentFamilyName = entry.get()
			self.database.storeFamily(currentFamilyName)
			self.currentFamilyId = self.database.getCurrentId()
			self.currentFamily = FamilyTree(self.currentFamilyId, currentFamilyName)
			popup.destroy()
			# edit currentFamilyName
			self.varFamilyName.set(currentFamilyName+"'s family")

		def createNewFamily():
			global popup
			global entry
			popup = Toplevel()
			# use this function to disable main window until popup window close 
			popup.grab_set()
			# family name label
			label = Label(popup, text="Family name: ")
			label.pack(side=LEFT)
			# entry text to input family name
			entry = Entry(popup, width=30)
			entry.pack(side=LEFT)
			# button to create family
			createButton = Button(popup, width=10, text='Create', command=onClickCreateFamily)
			createButton.pack()

		def onClickYes():
			apopup.destroy()
			self.database.commit()
			createNewFamily()

		def onClickNo():
			apopup.destroy()
			self.database.abort()
			createNewFamily()

		self.menuBar.entryconfig("Edit", state="normal")
		if self.currentFamily is not None:
			apopup = Toplevel()
			# use this function to disable main window until popup window close
			apopup.grab_set() 
			# label information
			alabel = Label(apopup, text="Would you like to store current family?")
			alabel.pack()
			# button Yes
			yesButton = Button(apopup, width=10, text='Yes', command=onClickYes)
			yesButton.pack(side=LEFT)
			# button No
			noButton = Button(apopup, width=10, text='No', command=onClickNo)
			noButton.pack(side=LEFT)
		else:
			createNewFamily()

	def onClickChooseFamily(self):
		self.textPersonList.insert(END, 'Family information')

	def onClickSave(self):
		self.database.commit()

	def onClickAbort(self):
		self.database.abort()

	def onClickAddPerson(self):
		def onClickAdd():
			# read input data
			name = inputName.get()
			year = int(inputYear.get())
			gender = GENDER.fromString(genderChoiceVar.get())
			fatherId = Utils.cropIndex(fatherChoiceVar.get())
			motherId = Utils.cropIndex(motherChoiceVar.get())
			coupleId = Utils.cropIndex(coupleChoiceVar.get())
			# create objects and database record
			self.database.storePerson(self.currentFamilyId, \
				name, year, gender, fatherId, motherId)
			currentPersonId = self.database.getCurrentId()
			if coupleId > 0:
				if gender == GENDER.MALE:
					self.database.storeCouple(currentPersonId, coupleId)
				else:
					self.database.storeCouple(currentPersonId, coupleId)
			person = Person(currentPersonId, name, year, gender)
			self.currentFamily.addPerson(person)
			self.currentFamily.setFather(fatherId, currentPersonId)
			self.currentFamily.setMother(motherId, currentPersonId)
			self.currentFamily.setCouple(coupleId, currentPersonId)
			popup.destroy()

		def onClickCancel():
			popup.destroy()

		popup = Toplevel()
		# use this function to disable main window until popup window close
		popup.grab_set() 
		# name label
		nameLabel = Label(popup, width=20, text="Full name:")
		nameLabel.grid(row=0, column=0)
		# input name
		inputName = Entry(popup, width=30)
		inputName.grid(row=0, column=1)
		# year label
		yearLabel = Label(popup, width=20, text="Year of birth:")
		yearLabel.grid(row=1, column=0)
		# input year
		inputYear = Entry(popup, width=30)
		inputYear.grid(row=1, column=1)
		# gender label
		genderLabel = Label(popup, width=20, text="Gender:")
		genderLabel.grid(row=2, column=0)
		# gender menu choice
		genderChoice = ["MALE", "FEMALE"]
		genderChoiceVar = StringVar(popup, value="Choose gender")
		genderBox = OptionMenu(popup, genderChoiceVar, *genderChoice)
		genderBox.config(width=25)
		genderBox.grid(row=2, column=1)
		# father label
		fatherLabel = Label(popup, width=20, text="Father:")
		fatherLabel.grid(row=3, column=0)
		# father menu choice
		fatherChoice = self.currentFamily.toListString(omitGender=GENDER.FEMALE)
		fatherChoiceVar = StringVar(popup, value="Choose father")
		fatherBox = OptionMenu(popup, fatherChoiceVar, *fatherChoice)
		fatherBox.config(width=25)
		fatherBox.grid(row=3, column=1)
		# mother label
		motherLabel = Label(popup, width=20, text="Mother:")
		motherLabel.grid(row=4, column=0)
		# mother menu choice
		motherChoice =  self.currentFamily.toListString(omitGender=GENDER.MALE)
		motherChoiceVar = StringVar(popup, value="Choose mother")
		motherBox = OptionMenu(popup, motherChoiceVar, *motherChoice)
		motherBox.config(width=25)
		motherBox.grid(row=4, column=1)
		# couple label
		coupleLabel = Label(popup, width=20, text="Couple:")
		coupleLabel.grid(row=5, column=0)
		# couple menu choice
		coupleChoice = ["a couple"]
		coupleChoiceVar = StringVar(popup, value="Choose couple")
		coupleBox = OptionMenu(popup, coupleChoiceVar, *coupleChoice)
		coupleBox.config(width=25)
		coupleBox.grid(row=5, column=1)
		# button Add
		addButton = Button(popup, text='Add', width=10, command=onClickAdd)
		addButton.grid(row=6, column=0)
		# button Cancel
		cancelButton = Button(popup, text='Cancel', width=10, command=onClickCancel)
		cancelButton.grid(row=6, column=1)

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