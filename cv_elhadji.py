import streamlit as st

#configuration de la page
st.set_page_config(page_title="cv - Elhadji Diegane Gning",page_icon="photo.pjg",layout="centered")

# titre
st.title("ELHADJI DIEGANE GNING")


st.markdown("---")

# profils
st.write("Technicien Superieur en Geomatique et Geographe , "
         "spécialisée dans les systemes information geographique (SIG), la cartographie "
         " analyse spatiale dessin plan programmation pilotage de drone la teledection la numerisation la realisation de" 
         "carte la topographique et les suites bureautiques.")

# diplomes
st.header("diplômes")
st.write("**LICENCE EN GEOGRAPHIE A UNIVERSITE CHEIKH ANTA DIOP**")

st.write("**BREVRET TECHNICIEN SUPERIEUR EN GEOMATIQUE AU CENTRE D'ENTREPRENEURIAT ET DE DEVELOPPEMENT TECHNIQUE LE G15**")

st.write("**BACCALAUREAT A UNIVERSITE CHEIKH ANTA DIOP**")

# competences
st.header(" competences")
st.markdown(""" 
- Outils informatique( suites Offices )
- Cartographie (QGIS)
- SIG (QGIS,ARCGIS)
- Analyse Sptiale
- Python
- lecture et interpretation de carte
- dessin plan (AUTOCAD ET SKETCHUP)
- topographie
- collectes de donnees (Mobile Topographer)
- teledections
- analyses documentaires
- pilotage de drone 
""")

with st.sidebar:    
    # Information personnelles
    st.title("ELHADJI DIEGANE GNING")
    st.write("**TECHNICIEN SUPERIEUR EN GEOMATIQUE ET GEOGRAPHE**")
    st.write(" EMAIL:elhadjidieganegning@gmail.com")
    st.write(" Adersse : DAKAR/SENEGAL")
        
    
# Pied de page
st.markdown("---")
