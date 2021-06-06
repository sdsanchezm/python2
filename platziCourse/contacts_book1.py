import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def showContacts(self):
        print('''
        Nombre: {}
        Phone: {}
        Emmail: {}
        '''.format(self.name, self.phone, self.email))

class ContactBook:
    def __init__(self):
        self._contact = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contact.append(contact)
        self._save()
        print('contact added...\n')

    def search(self, name):
        for contact in self._contact:
            if contact.name == name:
                self.printContact(contact)
                break
            else:
                self.notFound()
                break
    
    def listAll(self):
        for contact in self._contact:
            self.printContact(contact)

    def deleteContact(self, name):
        for index, contact in enumerate(self._contact):
            if contact.name == name:
                del self._contact[index]
                self._save()
                break

    def update(self, name):
        for index, contact in enumerate(self._contact):
            if contact.name == name:
                contact.name = str( input( 'Please enter new name: ' ) )
                contact.phone = str( input( 'Please enter new phone: ' ) )
                contact.email = str( input( 'Please enter new email: ' ) )
                self._contact[index] = contact
                self._save()
                break

    def printContact(self, contact):
        print('''
        Nombre: {}
        Phone: {}
        Emmail: {}
        '''.format(contact.name, contact.phone, contact.email))

    def _save(self):
        with open('contacts.csv', 'r+', encoding='utf-8') as f:
            writer = csv.writer(f, lineterminator='\r')
            writer.writerow( ('name', 'phone', 'phone') )

            for contact in self._contact:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def notFound(self):
        print('''
        Record not Found!
        ''')

def run():
    
    contactBook1 = ContactBook()

    with open('contacts.csv', 'r+', encoding='utf-8') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if len(row) == 0:
                continue
            if index == 0:
                continue

            contactBook1.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            What would you like to do?

            [a]dd contact
            [u]pdate a contact
            [f]ind a contact
            [d]elete a contact
            [l]ist contacts
            [e]xit
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            
            contactBook1.add(name, phone, email)

        elif command == 'u':
            name = str(input('Type the name of the contact you want to update: '))
            contactBook1.update(name)

        elif command == 'f':
            name = str(input('Type the name of the contact to find: '))
            contactBook1.search(name)

        elif command == 'd':
            name = str(input('Type the name of the contact to delete: '))
            contactBook1.deleteContact(name)

        elif command == 'l':
            contactBook1.listAll()

        # elif command == 's':
        #     contactBook1.save

        elif command == 'e':
            break
        else:
            print('Invalid commmand.')


if __name__ == '__main__':
    print('contacts book')
    run()