
#coding:utf-8
import sqlite3
conn = sqlite3.connect('contacts.db')
cur = conn.cursor()

#création du tableau de contacts
'''cur.execute("""create table contacts 
                (id integer primary key autoincrement,
                name text not null,
                first_name text not null,
                Email text,
                number integer not null,
                adresse text)
            """)'''

# Ajouter un contact
def add_contact():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    
    k_name = input("Quel est ton nom ...?")
    k_firts_name = input("Quel est ton prenom ...?")
    k_Email = input("Saisir ton E-mail ...?")
    k_number = int(input("Saisir ton numero de tele...?"))
    k_adresse = input("Entrer ton adresse ...?")
    cur.execute(f"insert into contacts(name,first_name,Email,number,adresse) values('{k_name}','{k_firts_name}','{k_Email}','{k_number}','{k_adresse}')")
                  
    
    conn.commit()
    conn.close  

       
        

# Modifier un contact
def update_contact(id):
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("update contacts set number = 77546587 where rowid = (?)",(id))
    
    conn.commit()
    conn.close

# Supprimer un contact
def delete_contact(id):   
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("delete from contacts where rowid = (?)",id)
    
    
    conn.commit()
    conn.close

# Afficher les contacts
def print_contact():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("select * from contacts")
    #Affichage de tout les contacts
    aff_contacts = cur.fetchall()
    for contact in aff_contacts:
        print(contact)

    #Affichage d'un contact par son numéro de téléphone
    print(contact[4])
    conn.commit()
    conn.close

def print_contact_par_nmb(number):
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute("select * from contacts where id = (?)",(number,))
    
    #Affichage d'un contact par son numéro de téléphone
    
    conn.commit()
    conn.close




#add_contact()
#update_contact('8')
#delete_contact()
#print_contact()
print_contact_par_nmb("774500000")

