import streamlit as st
from datetime import datetime, timedelta

# Define diseases and their information
diseases = {
    "Type 1 Diabetes": {
        "english_name": "Type 1 Diabetes",
        "arabic_name": "سكري النوع 1",
        "symptoms": "Increased thirst, frequent urination, extreme hunger, unexplained weight loss.",
        "causes": "Immune system attacks insulin-producing cells in the pancreas.",
        "first_aid": "Insulin therapy, monitoring blood glucose levels.",
        "type_of_disorder": "Autoimmune disorder",
        "gene_info": "Genetic predisposition along with environmental factors.",
        "recommendations": "Maintain regular insulin levels, follow a healthy diet, exercise regularly.",
    },
    "Cystic Fibrosis": {
        "english_name": "Cystic Fibrosis",
        "arabic_name": "التليف الكيسي",
        "symptoms": "Persistent cough, lung infections, difficulty breathing, poor growth.",
        "causes": "Mutation in the CFTR gene, inherited in an autosomal recessive manner.",
        "first_aid": "Oxygen therapy, chest physiotherapy, and enzyme replacement therapy.",
        "type_of_disorder": "Genetic disorder",
        "gene_info": "Mutation in the CFTR gene that affects chloride transport in cells.",
        "recommendations": "Regular physiotherapy, antibiotics, and a high-calorie diet.",
    },
    "Sickle Cell Anemia": {
        "english_name": "Sickle Cell Anemia",
        "arabic_name": "الأنيميا المنجلية",
        "symptoms": "Fatigue, pain episodes, swelling in hands and feet, frequent infections.",
        "causes": "Mutation in the hemoglobin gene (HBB), inherited in an autosomal recessive manner.",
        "first_aid": "Pain relief, oxygen, hydration, and blood transfusions if needed.",
        "type_of_disorder": "Genetic disorder",
        "gene_info": "Mutation in the HBB gene causing abnormal hemoglobin (HbS).",
        "recommendations": "Maintain hydration, avoid extreme temperatures, and regular checkups.",
    },
    "Hereditary Cancer": {
        "english_name": "Hereditary Cancer",
        "arabic_name": "السرطان الوراثي",
        "symptoms": "Symptoms vary based on cancer type, but may include lumps, bleeding, fatigue.",
        "causes": "Inherited mutations in cancer-suppressing genes (e.g., BRCA1, BRCA2).",
        "first_aid": "Seek immediate medical consultation, may involve chemotherapy or surgery.",
        "type_of_disorder": "Genetic disorder",
        "gene_info": "BRCA1/BRCA2 mutations lead to increased cancer risk.",
        "recommendations": "Regular screenings, genetic counseling, and preventive measures.",
    },
    "Down Syndrome": {
        "english_name": "Down Syndrome",
        "arabic_name": "متلازمة داون",
        "symptoms": "Developmental delays, intellectual disability, characteristic facial features.",
        "causes": "Extra copy of chromosome 21 (trisomy 21).",
        "first_aid": "Early intervention programs, speech and occupational therapy.",
        "type_of_disorder": "Genetic disorder",
        "gene_info": "Trisomy 21 causes physical and intellectual disabilities.",
        "recommendations": "Speech therapy, physical therapy, and early learning programs.",
    },
    "Aplastic Anemia": {
        "english_name": "Aplastic Anemia",
        "arabic_name": "فقر الدم اللاتنسجي",
        "symptoms": "Fatigue, frequent infections, easy bruising, nosebleeds.",
        "causes": "Damage to bone marrow, which fails to produce sufficient blood cells.",
        "first_aid": "Blood transfusions, immunosuppressive therapy, bone marrow transplant.",
        "type_of_disorder": "Blood disorder",
        "gene_info": "Possible genetic mutations, but more commonly due to environmental factors.",
        "recommendations": "Bone marrow transplant, avoiding infections.",
    },
    "Hereditary Blindness": {
        "english_name": "Hereditary Blindness",
        "arabic_name": "العمي الوراثي",
        "symptoms": "Progressive vision loss, difficulty seeing at night, light sensitivity.",
        "causes": "Inherited mutations in genes that affect the retina or optic nerve.",
        "first_aid": "Supportive therapy, low vision aids, and genetic counseling.",
        "type_of_disorder": "Genetic disorder",
        "gene_info": "Mutations in various genes such as RP1, RHO, and others.",
        "recommendations": "Regular eye checkups, adaptive techniques for vision loss.",
    },
    "Wilson's Disease": {
        "english_name": "Wilson's Disease",
        "arabic_name": "مرض ويلسون",
        "symptoms": "Fatigue, jaundice, tremors, difficulty walking.",
        "causes": "Defective copper metabolism leading to copper buildup in organs.",
        "first_aid": "Chelation therapy, copper-restricted diet.",
        "type_of_disorder": "Genetic disorder",
        "gene_info": "Mutation in the ATP7B gene affects copper transport.",
        "recommendations": "Copper chelation therapy, regular liver function tests.",
    },
    "Multiple Sclerosis": {
        "english_name": "Multiple Sclerosis",
        "arabic_name": "التصلب المتعدد",
        "symptoms": "Numbness, weakness, coordination issues, blurred vision.",
        "causes": "Autoimmune response attacking the nervous system.",
        "first_aid": "Disease-modifying therapies, steroids for flare-ups.",
        "type_of_disorder": "Autoimmune disorder",
        "gene_info": "Genetic predisposition along with environmental triggers.",
        "recommendations": "Physical therapy, symptom management with medication.",
    },
    "Lupus": {
        "english_name": "Lupus",
        "arabic_name": "الذئبة الحمراء",
        "symptoms": "Fatigue, joint pain, skin rashes, kidney problems.",
        "causes": "Autoimmune disease where the immune system attacks healthy tissue.",
        "first_aid": "Anti-inflammatory drugs, immunosuppressants.",
        "type_of_disorder": "Autoimmune disorder",
        "gene_info": "Genetic factors play a role in predisposition.",
        "recommendations": "Manage flares with medication, sun protection.",
    },
    "Rheumatoid Arthritis": {
        "english_name": "Rheumatoid Arthritis",
        "arabic_name": "الروماتويد",
        "symptoms": "Joint pain, swelling, stiffness, fatigue.",
        "causes": "Autoimmune response causing inflammation in joints.",
        "first_aid": "Pain relief, anti-inflammatory drugs, physical therapy.",
        "type_of_disorder": "Autoimmune disorder",
        "gene_info": "Genetic predisposition with environmental triggers.",
        "recommendations": "Medication to reduce inflammation, joint protection strategies.",
    },
    "Hypertension": {
        "english_name": "Hypertension",
        "arabic_name": "الضغط العالي",
        "symptoms": "Often asymptomatic but may cause headaches, dizziness.",
        "causes": "Genetic factors, high salt intake, obesity, and lack of exercise.",
        "first_aid": "Monitor blood pressure, medication, lifestyle changes.",
        "type_of_disorder": "Chronic condition",
        "gene_info": "Genetic predisposition along with environmental factors.",
        "recommendations": "Regular blood pressure monitoring, healthy diet, exercise.",
    },
    "Asthma": {
        "english_name": "Asthma",
        "arabic_name": "الربو",
        "symptoms": "Wheezing, shortness of breath, chest tightness, coughing.",
        "causes": "Genetic factors and environmental triggers (allergens, pollution).",
        "first_aid": "Inhalers (bronchodilators), corticosteroids.",
        "type_of_disorder": "Chronic respiratory condition",
        "gene_info": "Genetic predisposition, family history.",
        "recommendations": "Avoid triggers, use inhalers as prescribed.",
    },
    "Type 2 Diabetes": {
        "english_name": "Type 2 Diabetes",
        "arabic_name": "السكري النوع 2",
        "symptoms": "Increased thirst, frequent urination, fatigue, blurred vision.",
        "causes": "Insulin resistance and eventual pancreatic beta-cell dysfunction.",
        "first_aid": "Blood sugar monitoring, insulin or oral medications.",
        "type_of_disorder": "Chronic metabolic disorder",
        "gene_info": "Genetic factors along with lifestyle factors (diet, inactivity).",
        "recommendations": "Healthy diet, regular exercise, weight management.",
    },
    "Autism": {
        "english_name": "Autism",
        "arabic_name": "التوحد",
        "symptoms": "Difficulty with social interactions, repetitive behaviors, communication challenges.",
        "causes": "Genetic mutations and environmental factors.",
        "first_aid": "Behavioral therapy, speech therapy.",
        "type_of_disorder": "Neurodevelopmental disorder",
        "gene",
                "gene_info": "Genetic mutations in various genes like SHANK3, CNTNAP2.",
        "recommendations": "Early intervention programs, speech and occupational therapy.",
    },
    "Schizophrenia": {
        "english_name": "Schizophrenia",
        "arabic_name": "الشيزوفرينيا",
        "symptoms": "Hallucinations, delusions, disorganized thinking, lack of motivation.",
        "causes": "Genetic factors combined with environmental stressors.",
        "first_aid": "Antipsychotic medications, psychiatric care.",
        "type_of_disorder": "Mental disorder",
        "gene_info": "Genetic predisposition with many risk genes involved.",
        "recommendations": "Medication adherence, therapy, support groups.",
    },
    "Breast Cancer": {
        "english_name": "Breast Cancer",
        "arabic_name": "سرطان الثدي",
        "symptoms": "Lumps in the breast, changes in skin or nipple appearance, unexplained pain.",
        "causes": "Genetic mutations (BRCA1, BRCA2), hormone exposure.",
        "first_aid": "Seek medical advice immediately for diagnosis, surgery, and chemotherapy.",
        "type_of_disorder": "Cancer",
        "gene_info": "BRCA1/BRCA2 mutations increase the risk.",
        "recommendations": "Regular screening, genetic testing, early intervention if needed.",
    },
    "Alzheimer's Disease": {
        "english_name": "Alzheimer's Disease",
        "arabic_name": "الزهايمر",
        "symptoms": "Memory loss, confusion, difficulty with familiar tasks, personality changes.",
        "causes": "Genetic mutations, aging, and environmental factors.",
        "first_aid": "Cognitive therapy, medications to manage symptoms.",
        "type_of_disorder": "Neurodegenerative disorder",
        "gene_info": "APOE gene mutations increase risk, especially APOE4.",
        "recommendations": "Cognitive training, healthy diet, managing risk factors.",
    },
    "Amyotrophic Lateral Sclerosis (ALS)": {
        "english_name": "Amyotrophic Lateral Sclerosis (ALS)",
        "arabic_name": "التصلب الجانبي الضموري",
        "symptoms": "Muscle weakness, difficulty speaking, swallowing, and breathing.",
        "causes": "Motor neurons degeneration, often genetic.",
        "first_aid": "Respiratory support, physical therapy, medication.",
        "type_of_disorder": "Neurodegenerative disorder",
        "gene_info": "Mutations in SOD1, C9orf72, and other genes.",
        "recommendations": "Physical therapy, speech therapy, and palliative care.",
    },
}

# Main function to display disease information and manage user input
def main():
    st.title("Genetic and Chronic Disease Information")
    
    # Dropdown menu for disease selection
    disease = st.selectbox("Select a disease", list(diseases.keys()))
    
    # Display selected disease information
    st.header(f"Medical Information about {diseases[disease]['english_name']} ({diseases[disease]['arabic_name']})")
    st.subheader("Symptoms / الأعراض")
    st.write(diseases[disease]["symptoms"])
    
    st.subheader("Causes / الأسباب")
    st.write(diseases[disease]["causes"])
    
    st.subheader("First Aid / الإسعافات الأولية")
    st.write(diseases[disease]["first_aid"])
    
    st.subheader("Type of Disorder / نوع الخلل")
    st.write(diseases[disease]["type_of_disorder"])
    
    st.subheader("Gene Information / شرح الجين المتسبب")
    st.write(diseases[disease]["gene_info"])
    
    st.subheader("Recommendations / التوصيات")
    st.write(diseases[disease]["recommendations"])
    
    # Symptom analysis feature
    st.subheader("Enter your symptoms for analysis / أدخل الأعراض لتحليلها")
    user_symptoms = st.text_area("Symptoms: (e.g., fever, pain, fatigue)", "")
    if user_symptoms:
        st.write(f"Analyzing symptoms: {user_symptoms}")
        # Basic analysis based on symptoms (simplified)
        if "pain" in user_symptoms.lower():
            st.write("Possible symptom of inflammation or muscle issues.")
        if "fever" in user_symptoms.lower():
            st.write("Possible infection or inflammatory condition.")
        else:
            st.write("No specific analysis available.")
    
    # Notification for user reminder
    st.subheader("Set a reminder / تعيين تذكير")
    reminder_time = st.time_input("Set reminder time", datetime.now().time())
    reminder_message = st.text_input("Enter reminder message", "Take medication.")
    
    if st.button("Set reminder / تعيين التذكير"):
        st.write(f"Reminder set for {reminder_time}. Message: {reminder_message}")
    
    st.write("This app helps you get detailed information about various diseases and set reminders for treatments or medication.")

# Run the app
if __name__ == "__main__":
    main()
