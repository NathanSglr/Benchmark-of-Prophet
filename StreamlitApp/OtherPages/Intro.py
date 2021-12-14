import streamlit as st
from PIL import Image
import urllib.request
import io
from urllib.request import urlretrieve
import plotly.graph_objects as go


def app():
    st.markdown('<h1><center><span style="color:#00BFFF">Projet: Benchmark des bibliothèques Prophet & Kats</center></h1>', unsafe_allow_html=True)
    st.write('- **_Auteurs_**: Sofiane Bouibeb, Ugo Broqua, Baptiste Chacun, Tancrède Donnais, Lucas Fourest, Jason Maureille, Nathan Sanglier')
    st.write('- **_Tuteur Entreprise_**: Hervé Mignot')
    st.write('------------------------------------------------------------------------------------------------------------------------')
    c1, c2 = st.columns(2)
    URL = 'https://github.com/NathanSglr/test/blob/e8d458b4c31d9fa77fff54eb44d86bcdd801b95c/StreamlitApp/Pictures/Equancy_logo.png'
    urlretrieve(URL, 'pic.png')
    img = Image.open('pic.jpg')
    c1.image(img)

    c2.image('https://github.com/NathanSglr/test/blob/e8d458b4c31d9fa77fff54eb44d86bcdd801b95c/StreamlitApp/Pictures/IMTA_logo.png')
    st.write('------------------------------------------------------------------------------------------------------------------------')
    st.markdown("Cette application permet de prévoir les ventes d'un produit par semaine dans un magasin d'une enseigne alimentaire. L'utilisateur a à sa disposition plusieurs modèles de Statistiques, Machine Learning ou Deep Learning, et a la possibilité de modifier certains paramètres pour certains modèles. Les prévisions sont affichées, ainsi que les performances du modèle sur le dataset de test. Une comparaison globale des modèles implémentés est accessible en cliquant sur le bouton 'View Benchmark Results'." )
    st.write('------------------------------------------------------------------------------------------------------------------------')
    with st.expander("Qui sommes-nous?"):
        st.write("""
            Nous somme actuellement étudiants en 2ème année (Bac +4) de la formation Ingénieur Généraliste IMT Atlantique. Dans le cadre
            de l'Unité d'Enseignement "Projet Commande Entreprise", nous avons choisi le sujet suivant, proposé et suivi par le cabinet de
             conseil Equancy: 'Benchmark des bibliothèques Prophet & Kats'. Cela nous a permis de développer nos compétences sur l'analyse et
             la prévision de séries temporelles (domaine nouveau pour nous) et sur l'utilisation des librairies associées sur Python. 
         """)
    st.write('------------------------------------------------------------------------------------------------------------------------')
    c3, c4, c5 = st.columns(3)
    c4.image('https://github.com/NathanSglr/test/blob/e8d458b4c31d9fa77fff54eb44d86bcdd801b95c/StreamlitApp/Pictures/logos_all.png')
    st.write('------------------------------------------------------------------------------------------------------------------------')
    st.markdown('<span style="color: #26B260">Dernière mise à jour: 09/12/2021</span>', unsafe_allow_html=True)
    st.markdown('Site IMT Atlantique : https://www.imt-atlantique.fr/fr</a>', unsafe_allow_html=True)
    st.markdown('Site Equancy : https://www.equancy.fr/fr/</a>', unsafe_allow_html=True)
    st.markdown('Contact : lucas.fourest@imt-atlantique.net')



