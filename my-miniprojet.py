import random
import json
compte = {}         
client = {}         
ClientCompte = {} 
fichier = open("stockage.json" , "r")
list = json.loads(fichier.read( ))
fichier.close()
print("list" ,list)
compte = list[0]
client = list[1]
ClientCompte = list[2]
print(type(compte))
print(type(client))
print(type(ClientCompte))
print("client  :   ",client)
print("compte :   ",compte)
print("clientcompte  :   ",ClientCompte)
# compte = {}         # numéro de compte :sold
# client = {}         # numéro de client :code secret
# ClientCompte = {}   # associe à chaque numéro de client son numéro de compte


def genererNumcompte(Numcl):
    return str(Numcl) + str(random.randint(0, 100))

def client_compte(Numc):
    k = list(ClientCompte.keys())
    t = list(ClientCompte.values())
    index = t.index(Numc)
    return k[index]


def ajouterclient(Numcl,MPC,Numc,soldc):
    client[Numcl] = MPC
    compte[Numc] = soldc
    ClientCompte[Numcl] = Numc    
    # with open("projet.txt","w") as bro:
    #     bro.write(Numc +"/" + soldc +"/"+ Numcl  +"/" + MPC)
    print("client ajouter avec NUMERO de compte : " , "{",Numc,"}")   

def supprimerclient(Numc):
    Numcl = client_compte(Numc)          #l'appele de fonction client_compte 
    if Numc in ClientCompte[Numcl] :
        del client[Numcl]
        del compte[Numc]
        del ClientCompte[Numcl]
        print("ce compte de client N°" , Numcl, "supprimer" )
    else:
        print("Le compte n'existe pas")

def modifier_MPC(Numcl,MPC,Nouveux_MPC): 
    if Numcl in client :
        client[Numcl] = Nouveux_MPC
        print("Mot de passe mofifie .")

    else:
        print("Client introvable .")

def deposer(Numc,montant_deposer):
    if Numc in compte:
        solde = compte[Numc]       
        solde = int(solde) + montant_deposer
        compte[Numc] = str(solde)
        print(montant_deposer,"DH deposes avec succes .")        
    else:
        print("client introuvable")
def retirer(Numc,montant_retirer):
    if Numc in compte :
        solde = compte[Numc] 
        if int(solde) >= montant_retirer:
            compte[Numc] = str(int(solde) - montant_retirer)
            print(montant_retirer,"DH retires avec succes .")          
        else:
            print("solde insuffisant .")          
    else:
        print("client introuvable")
        
def afficher_solde(Numc):
    if Numc in compte :
        print("solde",compte[Numc],"DH")
              
def premier_menu():
    print("         **************************MENU**********************************         ")
    print(" ---> Pour l'agent de banque entrer 1 : ")
    print(" ---> Pour le client entrer 2 : ")   
    print(" ---> Pour Quitter entrer 3 : ")
    premier_choix = input("Choisissez une option (1-3): ")
    return int(premier_choix)

def menu(premier_chiox):
    if premier_chiox == 1:
        print("      *************************MENU_AGENT****************************         ")
        print("1. Ajouter un Client")
        print("2. Supprimer un Client")
        choix = input("Choisissez une option (1-2): ")
    if premier_chiox == 2:
        print("        **************************MENU_CLIENT*************************         ")
        print("3. Modifier le mot de passe")
        print("4. Déposer de l'argent")
        print("5. Retirer de l'argent")
        print("6. afficher le solde")
        print("7. Quitter")
        choix = input("Choisissez une option (3-7): ")
    if premier_chiox == 3:
        choix = 8 
    return int(choix)
while True:
    premier_chiox=premier_menu()
    choix = menu(premier_chiox)
    if choix == 1: 
        Numcl = input("**Entrer Numero de client : ")
        soldc = input("**Entrer solde initiale : ")
        MPC = input("**Entrer mot de passe : ")
        Numc = genererNumcompte(Numcl)
        ajouterclient(Numcl,MPC,Numc,soldc)

    elif choix ==2: 
        Numc = input("**Entrer le Numero de compte : ")
        supprimerclient(Numc)
        print("hi")

    elif choix == 3:
        Numcl = input("**Entrer Numero de client : ")
        MPC = input("**Entrer mot de passe : ")
        Nouveux_MPC = input("**Entrer nouveux mot de passe : ")
        modifier_MPC(Numcl,MPC,Nouveux_MPC)

    elif choix == 4:
        Numc = input("**Entrer le Numero de compte : ")
        montant_deposer =int(input("**Entrer le montant deposer : "))
        deposer(Numc,montant_deposer)

    elif choix == 5:
        Numc = input("**Entrer le Numero de compte : ")
        montant_retirer= int(input("**Entrer le montant retirer : "))
        retirer(Numc,montant_retirer)

    elif choix == 6:
        Numc = input("**Entrer le Numero de compte : ")
        afficher_solde(Numc)

    elif choix == 8:
        fichier = open("stockage.json" , "w")
        fichier.write(json.dumps(list))
        fichier.close()
        break
    print("*********************************")
    print("pour tester :")
    print("client  :   ",client)
    print("compte :   ",compte)
    print("clientcompte  :   ",ClientCompte)

























































