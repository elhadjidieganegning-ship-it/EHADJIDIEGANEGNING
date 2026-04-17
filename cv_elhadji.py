import streamlit as st

#configuration de la page
st.set_page_config(page_title="cv - Elhadji Diegane Gning",page_icon="photo.pjg",layout="centered")

# titre
st.title("ELHADJI DIEGANE GNING")


st.markdown("---")

# profils
st.write("Etudiant motive en Lience 2 Geographie et en premiere annee de BTS en Geomatique, "
         "passionne par les systemes information geographique (SIG), la cartographie "
         " analyse spatiale dessin plan et programmation debutant.")

# formations
st.header(" formation et diplomes")
st.write("**2025/2026 LIENCE EN GEOGRAPHIE A UNIVERSITE CHEIKH ANTA DIOP**")

st.write("**2025/2026 BREVRET TECHNICIEN SUPERIEUR EN GEOMATIQUE AU CENTRE D'ENTREPRENEURIAT ET DE DEVELOPPEMENT TECHNIQUE LE G15**")

st.write("**2022/2023 BACCALAUREAT A UNIVERSITE CHEIKH ANTA DIOP**")

# competences
st.header(" competences")
st.markdown(""" 
- Outils informatique( suite Office )
- Cartographie (QGIS)
- SIG (QGIS, notions ARCGIS)
- Analyse Sptiale
- Python
- lecture et interpretation de carte
- dessin plan (AUTOCAD ET SKETCHUP)
- topographies
- collectes de donnees
- teledections
- analyses documentaires
- pilote de drone 
""")

with st.sidebar:    
    # Information personnelles
    st.write("ELHADJI DIEGANE GNING")
    st. write("**TECHNICIEN SUPERIEUR EN GEOMATIQUE ET GEOGRAPHE**")
    st.write(" EMAIL:elhadjidieganegning@gmail.com")
    st.write(" Adersse : Fatick;SENEGAL")
        
    
# Pied de page
st.markdown("---")
st.write(" 2026 - ELHADJI DIEGANE GNING")
