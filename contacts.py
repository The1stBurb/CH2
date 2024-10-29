
# def show_list(self):
#   print()
#   if len(self.contact_list) == 0:
#     self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
#   else:
#     self.view = 'quit'
#   self.handle_choice()
# def handle_choice(self):
#   if self.choice == 'q':
#     self.view = 'quit'
#   elif self.choice == 'a' and self.view == 'list':
#     self.view = 'add'
# class Information:
#   def __init__(self):
#     self.first_name = input('Enter their first name: ')
#     self.last_name = input('Enter their last name: ')
#     self.personal_phone = input('Enter their personal phone number: ')
#     self.personal_email = input('Enter their personal email address: ')
#     self.work_phone = input('Enter their work phone number: ')
#     self.work_email = input('Enter their work email address: ')
#     self.title = input('Enter their work title: ')
# def __add__(self, new_contact):
#   self.contact_list.append(new_contact)
  
# def add_contact(self):
#   self + Information()
#   self.view = 'list'
# Rachel
# Kim
# 555 123-4567
# rachel_k@gmail.com
# 555 890-1234
# rkim@apple.com
# Senior Software Engineer
# contacts = Contacts()
# contacts.display()
# def show_list(self):
#   print()
#   if len(self.contact_list) == 0:
#     self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
#   else:
#     for index, contact in enumerate(self.contact_list):
#       print(f"{index + 1}) {contact.first_name} {contact.last_name}")
#     self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
#   self.handle_choice()
# def handle_choice(self):
#   if self.choice == 'q':
#     self.view = 'quit'
#   elif self.choice == 'a' and self.view == 'list':
#     self.view = 'add'
#   elif self.choice.isnumeric() and self.view == 'list':
#     index = int(self.choice) - 1
#     if index >= 0 and index < len(self.contact_list):
#       self.index = index
#       self.view = 'info'
# Testing Your Code
# Before moving on to the next part of the script, we want to check that our code is displaying all of the contacts in the list. To do that, enter two different contacts. The first one is:
# John
# Calvin
# 555 111-2222
# john.calvin@email.net
# 555 333-4444
# jcalvin@work.org
# Philosopher
# You should see a list that looks like this:
# Contact 1
# Now add a second contact to the list:
# Thomas
# Hobbes
# 555 666-7777
# t_hobbes@email.net
# 555 888-9999
# tom_hobbes@work.org
# Philosopher
# def show_info(self):
#   self.contact_list[self.index].display_info()
#   self.choice = input('\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ').lower()
#   self.handle_choice()
# def display_info(self):
#   print(f'\n{self.first_name} {self.last_name}')
#   print(f'Personal phone number: {self.personal_phone}')
#   print(f'Personal email address: {self.personal_email}')
#   print(f'Work title: {self.title}')
#   print(f'Work phone number: {self.work_phone}')
#   print(f'Work email address: {self.work_email}')
# We want the user to be able to list view of all contacts from the info view when the user enters c. Modify the handle_choice method to set self.view to 'list' when self.choice is c.
# elif self.choice == 'c' and self.view == 'info':
#   self.view = 'list'
# So when the user enters n the index will increase by 1 as long as the index plus 1 is less than the length of the list. If not, the index becomes 0 (the first contact). Similarly, when the user enters p, the index will decrease by 1 as long as the index minus 1 is greater than or equal to 0. If not, the index becomes the length of the list minus 1 (the last contact). Add the following conditional branches to the handle_choice method.
# elif self.choice == 'n' and self.view == 'info':
#   self.index = self.index + 1 if self.index + 1 < len(self.contact_list) else 0
# elif self.choice == 'p' and self.view == 'info':
#   self.index = self.index - 1 if self.index - 1 >= 0 else len(self.contact_list) - 1
class Contacts:
    def __init__(self):
        self.view = 'list'
        self.contact_list = []
        self.choice = None
        self.index = None
    def display(self):
        while True:
            if self.view == 'list':
                self.show_list()
            elif self.view == 'info':
                self.show_info()
            elif self.view == 'add':
                print()
                self.add_contact()
            elif self.view == 'quit':
                print('\nClosing the contact list...\n')
                break
        def show_info(self):
        self.contact_list[self.index].display_info()
        self.choice = input('\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ').lower()
        self.handle_choice()
    def display_info(self):
        print(f'\n{self.first_name} {self.last_name}')
        print(f'Personal phone number: {self.personal_phone}')
        print(f'Personal email address: {self.personal_email}')
        print(f'Work title: {self.title}')
        print(f'Work phone number: {self.work_phone}')
        print(f'Work email address: {self.work_email}')
    def add_contact(self):
        self + Information()
        self.view = 'list'

    def show_list(self):
        print()
        if len(self.contact_list) == 0:
            self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            for index, contact in enumerate(self.contact_list):
                print(f"{index + 1}) {contact.first_name} {contact.last_name}")
            self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
            self.handle_choice()

    def handle_choice(self):
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'
        elif self.choice.isnumeric() and self.view == 'list':
            index = int(self.choice) - 1
            if index >= 0 and index < len(self.contact_list):
                self.index = index
                self.view = 'info'
        elif self.choice == 'c' and self.view == 'info':
            self.view = 'list'
class Information:
    def __init__(self):
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')
    def __add__(self, new_contact):
        self.contact_list.append(new_contact)