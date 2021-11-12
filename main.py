import streamlit as st
import random
from datetime import datetime
from datetime import date

st.title("Etude sur le provisionnement en assurance non-vie")

import time
#my_bar = st.progress(0)
#for percent_complete in range(100):
#    time.sleep(0.001)
#    my_bar.progress(percent_complete + 1)

if 'user_data' not in st.session_state:
    st.session_state.user_data = []
    date_deb = date.today()
    date_deb2 = date_deb.strftime("%d/%m/%Y")
    st.session_state.user_data.append(date_deb2)
    now = datetime.now()
    temps_debut = now.strftime("%H:%M:%S")
    st.session_state.user_data.append(temps_debut)

if 'page' not in st.session_state:

    st.session_state.page = 1
    st.write("Ce bref questionnaire vise à obtenir une meilleure connaissance des pratiques actuarielles dans le domaine du provisionnement non-vie. "
             "Actuaires, chargés d’études actuarielles et étudiants en actuariat sont invités à y participer.")
    st.write("Les résultats sont anonymes, les informations personnelles servant uniquement à des fins de statistiques descriptives.")
    st.write("Merci d’avance pour votre participation,")
    st.button("Commencer l'étude")

elif st.session_state.page==1:

    st.header("Informations générales")
    st.write("Ce premier groupe de question vise à préciser votre profil")

    with st.form(key='bloc_1'):
        sexe = st.selectbox('Sexe', ["-", "Homme", "Femme", "Non précisé"])
        age = st.selectbox('Âge', ["-","18-25", "26-35", "35-50", "51 et plus"])
        type_entreprise = st.selectbox("Type d'entreprise",["-", "Etudiant", "Compagnie d'assurance", "Mutuelle","Bancassureur","Cabinet de conseil","Autre"])
        seniorite = st.selectbox("Séniorité en actuariat",["-","Etudiant","0-2 ans","2-5 ans","5-8 ans","8-15 ans","15 ans et plus"])
        methode_connue = st.multiselect("De quelles méthodes de provisionnement avez déjà entendu parler ? (plusieurs réponses possibles)",["Chain Ladder","London Chain","Loss ratio","Mack","GLM","Bornhuetter Ferguson"])
        submit_button_1 = st.form_submit_button(label='Page suivante')

    if submit_button_1:
        st.session_state.page += 1
        st.session_state.user_data.append(sexe)
        st.session_state.user_data.append(age)
        st.session_state.user_data.append(type_entreprise)
        st.session_state.user_data.append(seniorite)
        st.session_state.user_data.extend(methode_connue)
        st.session_state.user_data.append("FIN PAGE UN")
        st.session_state.alea = random.uniform(0, 1)
        if st.session_state.alea < 0.5:
            st.session_state.user_data.append("Framing positif")
        else:
            st.session_state.user_data.append("Framing négatif")
        st.experimental_rerun()

elif st.session_state.page==2:

    st.header("Approche du risque")
    st.write("Ce deuxième groupe de questions vise à étudier votre appréhension du risque")

    if st.session_state.alea < 0.5:
        with st.form(key="test_alea_kahneman_1"):
            st.write("La France s'attend à l'arrivée d'une maladie infectieurse, supposée tuer 600 personnes. Deux programmes de traitement sont disponibles pour endiguer la maladie :")
            st.write("Si le programme A est adopté, 200 personnes seront sauvées")
            st.write("Si le programme B est adopté, il y a 1/3 de chances que 600 personnes soient sauvées et 2/3 de chances que personne ne soit sauvé")
            programme = st.selectbox("Quel programme vous semble préférable ?",["-", "Programme A", "Programme B"])
            submit_button_2 = st.form_submit_button(label="Page suivante")
    else:
        with st.form(key="test_alea_kahneman_1"):
            st.write(
                "La France s'attend à l'arrivée d'une maladie infectieurse, supposée tuer 600 personnes. Deux programmes de traitement sont disponibles pour endiguer la maladie :")
            st.write("Si le programme A est adopté, 400 personnes mourront")
            st.write(" - Si le programme B est adopté, il y a 1/3 de chances que personne ne meure et 2/3 de chances que 600 personnes meurent")
            programme = st.selectbox("Quel programme vous semble préférable ?", ["-", "Programme A", "Programme B"])
            submit_button_2 = st.form_submit_button(label="Page suivante")

    if submit_button_2:
        st.session_state.page += 1
        st.session_state.user_data.append(programme)
        st.experimental_rerun()

elif st.session_state.page == 3:

    st.session_state.page = 999

    with st.form(key='my_form_end'):
        text_input = st.text_input(label='Vous pouvez noter ici des remarques éventuelles si vous le souhaitez')
        submit_button_end = st.form_submit_button(label="Terminer l'étude")

elif st.session_state.page == 999:

    end = datetime.now()
    temps_fin = end.strftime("%H:%M:%S")
    st.session_state.user_data.append(temps_fin)

    import gspread

    credentials = {
        "type": "service_account",
        "project_id": "acoustic-mix-331213",
        "private_key_id": "28bf926ad27ea160b487b68d615b6a8c87659cfa",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQC5enym8sKaQvSb\nLBPjfRg0fZVL6ToQNMvUBTJdMqDHRzBF1d83XwdCoyu/LfOjuGa08SF56Lf5X9K+\nNGzgU/g0tir8GjI+Y0cGl9GYmOjVhN60F669jhvyhDTpDSE1dvoHhrwuRT+tbk5X\nvHR6irx0W/+0y87Qc0SnQBlLwm4HpRWTe8aSwY1huc/Y8Drj9akOh5Z8FJJC2imk\nQrzDu4lFeiAjUgyV2lhuWymNIlVeSd7E4vEMOjtpYH7NakFhgNyklDqobZYCZpFZ\nm23v5HU8llg17mOLpopAWGMHBeHsqhYibk3G6AYPhIk/By3Zl0U/F005nGNrduJJ\nv2rd67lZAgMBAAECgf9KDSfMql9yTLPGwB0GAOEJE+/naYD6YhnULGmki/IPndHI\nD/tulUzGGMn+f3omg24oukeDRJvZvvLaEv7lEUv8v5Op00umsjxJMD6eOMO80QTu\nd1tskrArGF2Hg5Zz92xw/3oM1IOihR0CKluBZqKW/PllACSHVNNeyFimcUSSCB01\nACIFb57ubd9jmfYCHXnDSQdZRT8kuXaOboZ54OcVYhZfaiU2uj3vj8ZyS2PG39jm\nOmeRpDZGf+YWHB41SvvFQwWR1irzQ1G4awCwBHdoa4W8dlh+tcwHPJqaVMb3HCk8\nWlbmMZMQhRaSE4CeUel2WXt3Zu1E9uhNKYmPpYECgYEA86c8ZKsoDoO0MUwLrYNa\nGhFQDv1VoWlif3Ljn7ki4PhdhgUzhh0MTxH0yTZtgubUBN/yhoVxhwBXwuKCLEQx\nqt3Kbxpe65LXSqxVr6gkJn57DZvQqc1F28YWrMONGYGxvBr6ZMIQngRkXy8W3f+2\njF4aPuaoS8u8HqtwSvFSw4ECgYEAwuCVxxTTD4g3KROVt5P4y02MYDuEkoNWNfXw\nmSZjhxrS6WsHan6M0R5GVKFBSUK42pC9JMyXXk+qefRHD9SVXhNm27xU1BabpXqw\nXUW3yBgJuXXw2oQbspOi9Zh7EPAAR6FaDH8s1ysjHxYaFSEvOwq0WZzRgLRaNC9o\nDbpAgdkCgYBqsnJc9yKccIpJCC8Y9atQPQKc/c0w2PBcNVh+ilk+wSRbWw28Dh5k\nxc03C9GbADAaTmNrCyay4rCL1BsC/X3ugB901cx5Rp1mwt7nBC+Id9y1EeWnZg/Q\ndQda8mtonwXRBNNfqigSuoOltv5BiwhKoa7GmsVaI8ame5a6CsGegQKBgD8dD0UH\nmId6PSsffaiT0sq9Fc6A2CG/SWd2fHKNPUSfSllwYVl7HM4JOQvlochBRK78m1VU\nsV1I/dQ7adxVo/5w2CooJ2z82XHRd1bt4mR6bIPVD6klifbe27MgrBLDN8P7HLfZ\nZENXZCuIM/BN7Ab6I4i2Qh+lyWUHSXLQtF2ZAoGAPzJtUNV0j0gAiKv0T6Zl9tzf\nebQn3FwhC1JCWuZj3i2YKboSWW/P67HZTHU0pUVWkdL1TFyFXeshI807ah5980G6\nYfmFSXIB1hDHv60WEDvyMU/zA4y64mCOPht0genVN5RLVRkfEhdAVVu+WfN3YTFf\nrH2CeEEMikMTvo/jHKU=\n-----END PRIVATE KEY-----\n",
        "client_email": "testteam@acoustic-mix-331213.iam.gserviceaccount.com",
        "client_id": "103380036233115407551",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/testteam%40acoustic-mix-331213.iam.gserviceaccount.com"
    }

    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open("test_beta")
    worksheet = sh.sheet1
    worksheet.insert_row(st.session_state.user_data, 1)

    st.write("Vos résultats ont bien été pris en compte")
    st.write("Merci pour votre participation")

#my_bar.empty()