# coding: utf-8
from requet import Requet, Log
import re
import time
import sys

#Informations relatives au compte que l'on veut créer	 
titre = "mr" 
prenom = "John"
nom = "Doe"
mail = "soldout5@ageokfc.com"
mdp= "motdepasse92" 
tel = "" 
naissance = "16.11.2000"




 
print("\n -Test technique sold out\n")
print(" -Developed by Chahid Ouraghene\n")
print(" -Ce script python permet de créer un compte, se login puis ajouter un article dans le panier sur le site solebox\n")
	  

 
 

input("Appuyez sur une touche pour commencer")


reqAcc= Requet(True, 'www.solebox.com')

reqAcc.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'

# Desactive le mode debug
reqAcc.debug = False

   

print("Connexion au site réussie !")


print("Creation du compte...")

response_acc = reqAcc.requet('/en_FR/registration?rurl=1',
	headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Connection': 'close',
		'Referer': 'https://www.solebox.com/en_FR/login',
		'Upgrade-Insecure-Requests': '1',
		'TE': 'Trailers'
	}
)



csrf = re.search(r'(name=\"csrf_token\" value=\")(.+)(=\"/>)',response_acc).group(2) #Recherche du token csrf

#Initialisation d'une variable contenant les informations de l'utilisateur
requetbody_acc = "dwfrm_profile_register_title=" + titre + "&dwfrm_profile_register_firstName=" + prenom + "&dwfrm_profile_register_lastName=" + nom + "&dwfrm_profile_register_email=" + mail + "&dwfrm_profile_register_emailConfirm=" + mail + "&dwfrm_profile_register_password=" + mdp + "&dwfrm_profile_register_passwordConfirm=" + mdp+ "&dwfrm_profile_register_phone=" + tel+ "&dwfrm_profile_register_birthday=" + naissance + "&dwfrm_profile_register_acceptPolicy=true&csrf_token=" +csrf+"%3D"


#Envoi de la demande d'inscription au serveur avec les info user
post_register= reqAcc.requet('/on/demandware.store/Sites-solebox-Site/en_FR/Account-SubmitRegistration?rurl=1&format=ajax',
    method="post",
	headers={
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.5',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With': 'XMLHttpRequest',
		'Origin': 'https://www.solebox.com',
		'Connection':'close',
		'Referer': 'https://www.solebox.com/en_FR/registration?rurl=1',
		'TE': 'Trailers'
	},
    body=requetbody_acc
)

#Vérification de la demande d'inscription
if("errorMessage" in post_register):
        
	print("La création de compte a échouée. Le programme va se fermer")
       
else:
	print("Compte créé !");


print("Login au compte...")

time.sleep(5)


print("Recherche de l'article...")

#Recherche de l'article et récupération du PID
response = reqAcc.requet('/en_FR/p/carhartt_wip-s%2Fs_pocket_tee_-black-01713398.html ',
	headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection': 'close',
		'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers'
	}
)




print("Ajout de l'article au panier..")

#Ajout au panier
atc_post_response = reqAcc.requet('/en_FR/add-product?format=ajax',
    method="post",
	headers={
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With': 'XMLHttpRequest',
		'Origin': 'https://www.solebox.com',
		'Connection':'close',
		'Referer': 'https://www.solebox.com/en_FR/p/carhartt_wip-s%2Fs_pocket_tee_-black-01713398.html',#Lien du produit à modifier
		'TE': 'Trailers'
	},
    body="pid=0171339800000004&options=%5B%7B%22optionId%22%3A%225903%22%2C%22selectedValueId%22%3A%22L%22%7D%5D&quantity=1"#PID du produit récupéré dans la requête https
)

#Vérification de l'ajout au panier
if("added to cart" in atc_post_response):
    print("Votre article a été rajouté au panier !");
else:
    print("Ajout de l'article échoué.")

		
	
