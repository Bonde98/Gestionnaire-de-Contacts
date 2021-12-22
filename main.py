import contactsgestion
#contactsgestion.add_contact()
#contactsgestion.update_contact()
#contactsgestion.delete_contact()
#contactsgestion.print_contact()
#contactsgestion.print_contact_par_nmb()

choix = ''
def menu():
    global choix
    print("___Bienvenue dans le page de gestion contact___ Faite ton choix...")
    print("1___Ajouter un contact___")
    print("2___Modifier un contact___")
    print("3___Supprimer un contact___")
    print("4___Afficher la liste des contacts___")
    print("5___Afficher un contact par son numéro de Téléphone___")
    choix = input("Faites ton choix entre ces 5 options...?")



def reponse():
    if choix == '' :
        print("___choix non reconnue!___")
        #Ajouter un contact
    elif choix == "1":
        contactsgestion.add_contact()
        menu()
        #Modification d'un contact
    elif choix == "2":
        contactsgestion.update_contact()
        menu()
        #Supprimer un contact
    elif choix == "3":
        contactsgestion.delete_contact()
        menu()
        #Afficher les contacts
    elif choix == "4":
        contactsgestion.print_contact()
        menu()
        #Afficher un contact par son numéro
    elif choix == "5":
        contactsgestion.print_contact_par_nmb()
        menu()
    else:
        print("choix non reconnue,Essayer de nouveaux...!")


menu()
reponse()