import sqlite3
with sqlite3.connect('contacts.db') as conn:
    cur=conn.cursor()


#conn = sqlite3.connect('contacts.db')
#cur = conn.cursor()

#création du tableau de contacts
'''cur.execute("""create table contacts 
                (id integer primary key autoincrement,
                name text not null,
                first_name text not null,
                Email text,
                number integer not null,
                adresse text)
            """)'''

#Ajouter un contact
def add_contact():
    #conn = sqlite3.connect('contacts.db')
    #cur = conn.cursor()
    print("___Ajouter un contact___")
    print("Remplir ces information suivants...")
    
    k_name = input("Entrer le nom ...?")
    k_firts_name = input("Entrer le prenom ...?")
    k_Email = input("Saisir ton E-mail ...?")
    k_number = int(input("Saisir le numero de tele...?"))
    k_adresse = input("Entrer l' adresse ...?")
    cur.execute(f"insert into contacts (name,first_name,Email,number,adresse) values ('{k_name}','{k_firts_name}','{k_Email}','{k_number}','{k_adresse}')")
    print("contact ajouter avec succées...")
    conn.commit()
    conn.close  

       
        

# Modifier un contact
def update_contact():
    #conn = sqlite3.connect('contacts.db')
    #cur = conn.cursor()
    print("___Modifier un contact___")
    id = int(input("Quel contact tu veut modifier..."))
    name = input("Saisir ton nouveau nom...")
    first_name = input("Saisir ton nouveau prénom...")
    Email = input("Saisir ton Email...")
    number = int(input("Entrer le nouveau numero..."))
    adresse = input("Saisir ton nouvelle adresse...")
    cur.execute("update contacts set (name,first_name,Email,number,adresse) = ((?),(?),(?),(?),(?)) where rowid = (?)",(name,first_name,Email,number,adresse,id))
    print("___Contact N:",id,"a été modifier avec succés...___")
    cur.execute("select * from contacts where id = (?)",(id,))
    contact_numb = cur.fetchone()
    print("___Voici ton nouveaux contact:",contact_numb)
    conn.commit()
    conn.close

# Supprimer un contact
def delete_contact():   
    #conn = sqlite3.connect('contacts.db')
    #cur = conn.cursor()
    print("___Supprimer un contact___")
    id = int(input("Quel contact tu veut supprimer..."))
    cur.execute("delete from contacts where rowid = (?)",(id,))
    print("contact N:",id,"a été supprimer navec succés")
    
    conn.commit()
    conn.close

#Afficher les contacts
def print_contact():
    #conn = sqlite3.connect('contacts.db')
    #cur = conn.cursor()
    print("___Affichage du tableau complet___")
    cur.execute("select * from contacts")
    #Affichage de tout les contacts
    aff_contacts = cur.fetchall()
    for contact in aff_contacts:
        print(contact)

    #conn.commit()
    #conn.close

#Affichage d'un contact par son numéro de téléphone
def print_contact_par_nmb():
    #conn = sqlite3.connect('contacts.db')
    #cur = conn.cursor()
    print("___Affichage d'un contact a travers son numéro___")
    print("__Tu veut afficher un contact a travers son numéro de téléphone___")
    number = int(input("Entrer le numero téléphone du contact..."))
    cur.execute("select * from contacts where number = (?)",(number,))
    contact_numb = cur.fetchone()
    print("Voici le contact complet de ce numéro téléphone :",contact_numb)
    
    #conn.commit()
    #conn.close



#add_contact()
#update_contact('5')
#delete_contact()
#print_contact()
#print_contact_par_nmb("774500000")

