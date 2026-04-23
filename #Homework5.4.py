#Homework 5.4

def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)

def find_by_name(contacts,name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def all_emails(contacts):
    emails = []
    for contact in contacts:
        emails.append(contact["email"])
    return emails

contacts = [ ]

add_contact(contacts, "Alice", "123-456-7891", "alice@example.com")
add_contact(contacts, "Bob", "234-567-8901", "bob@example.com")
add_contact(contacts, "Charlie", "345-678-9012", "charlie@example.com")

print("All contacts:")
print(contacts)

print("\nFind Bob:")
print(find_by_name(contacts, "Bob"))

print("\nAll emails:")
print(all_emails(contacts))

