# coding: utf-8
from requet import Requet, Log
import re
import time

#Information relative au compte que l'on veut créer	 
titre = "mr" #
prenom = "tifouk"
nom = "hoos"
mail = "bg92@gmail.com"
mdp= "password1234" 
tel = "" 
naissance = "16.11.2000"




print(r'''   
-Test technique sold out
-Developed by Chahid Ouraghene
-Ce script python permet de créer un compte, se login puis ajouter un article dans le panier sur le site solebox
	  

 
 ''')

input("Appuyez sur une touche pour commencer")


reqAcc= Requet(True, 'www.solebox.com')

reqAcc.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'

# Desactive le mode debug
reqAcc.debug = False

   

print("Connexion au site réussie !")

reqAcc.requet('/en_FR/login',
	headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Connection': 'close',
		'Referer': 'https://www.solebox.com/en_FR',
		'Upgrade-Insecure-Requests': '1'
	}

)




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



csrf = re.search(r'(name=\"csrf_token\" value=\")(.+)(=\"/>)',response_acc).group(2)


requetbody_acc = "dwfrm_profile_register_title=" + titre + "&dwfrm_profile_register_firstName=" + prenom + "&dwfrm_profile_register_lastName=" + nom + "&dwfrm_profile_register_email=" + mail + "&dwfrm_profile_register_emailConfirm=" + mail + "&dwfrm_profile_register_password=" + mdp + "&dwfrm_profile_register_passwordConfirm=" + mdp+ "&dwfrm_profile_register_phone=" + tel+ "&dwfrm_profile_register_birthday=" + naissance + "&dwfrm_profile_register_acceptPolicy=true&csrf_token=" +csrf+"%3D"



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

if("error" in post_register):
	print("La creation du compte a echoué. Vérifiez les informations")
else:
	print("Compte créé ! Verifiez vos e-mails");

print("Login au compte...")

time.sleep(5)


print('\033[94m' + "\n\nRecherche de l'article...")


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


atc_post_response = reqAcc.requet('/en_FR/add-product?format=ajax',
    method="post",
	headers={
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With': 'XMLHttpRequest',
		'Origin': 'https://www.solebox.com',
		'Connection':'close',
		'Referer': 'https://www.solebox.com/en_FR/p/carhartt_wip-s%2Fs_pocket_tee_-black-01713398.html',#Lien du produit 
		'TE': 'Trailers'
	},
    body="pid=0171339800000004&options=%5B%7B%22optionId%22%3A%225903%22%2C%22selectedValueId%22%3A%22L%22%7D%5D&quantity=1"#PID du produit récupéré dans la requête https
)

if("Error" in atc_post_response):
    print("Produit ajouté au panier !");
else:
    print("Impossible d'ajouter le produit au panier. Vérifiez le pid.")

		
	
