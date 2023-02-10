import streamlit as st
import pandas as pd
import model
import inserting_data
import time



st.title("Smoking Status Detection")
st.subheader("An End-End Data Engineering Project by Siva Chandan")
df = pd.DataFrame()

with st.form("input_df"):

    Age = st.number_input("Age",min_value = 21, max_value =98 , \
    help = "Enter your age here(Patient have to be 21 to use this)")

    height = st.number_input("Height(cm)", min_value = 54, max_value = 280, \
    value = 165, help = "Enter the height in cm")

    weight = st.number_input("Weight(kg)",min_value = 30.0, max_value =700.00, \
    value = 65.00, step = 0.1, help = "Enter Weight in KG(Kilo Gram)")

    waist = st.number_input("waist(cm)",min_value = 51.000000, max_value =129.000000, \
    value = 82.000000, step = 0.1 , help = "")

    fasting_blood_sugar = st.number_input("fasting blood sugar", value = 96.00,\
    min_value=46.00, max_value=423.00, step=0.1, help = "Enter the Fasting Blood Sugar Values")

    cholesterol = st.number_input("cholesterol",min_value = 55.00 , max_value =445.00, \
    value = 195.000000	, step = 0.1, help = "Enter the Cholestrol value")

    hemoglobin = st.number_input("hemoglobin",min_value = 4.90, max_value =21.1, \
    value =14.8 , step = 0.1, help = "Enter hemoglobin levels")

    urine_protein = st.number_input("Urine protein",min_value = 1, max_value =6, \
    value = 1, step = 1, help = "Enter Urine Protein")

    serum_creatinine = st.number_input("serum creatinine",min_value = 0.1, max_value =1.0, \
    value = 0.9, step = 0.01, help = "Enter serum creatinine")

    submit_function = st.form_submit_button("Submit")

if submit_function:
    df = pd.DataFrame({
                'age':[int(Age)], 'height(cm)':[int(height)], 'weight(kg)':[int(weight)], 'waist(cm)':[float(waist)], 'fasting blood sugar':[int(fasting_blood_sugar)],
       'Cholesterol':[int(cholesterol)], 'hemoglobin':[int(hemoglobin)], 'Urine protein':[int(urine_protein)], 'serum creatinine':[float(serum_creatinine)]

    })
    st.dataframe(df)
    smoking_status = model.load_predict(df)
    if smoking_status == 1:
        st.write("Smoking Positive")
    elif smoking_status == 0:
        st.write("Smoking Negative")
with st.form("add_data"):
    answer = st.radio("Add the record to Data base", ("Yes", "No"))
    next_submit_function = st.form_submit_button("Submit")

if next_submit_function:
    if answer == 'Yes':
        with st.spinner('Creating Doc String:'):
            inserting_data.inserting_data(df,'smoking','public','accountadmin','compute_wh')
        st.success('Inserting the Data', icon="✅")
            
    elif answer == "No":
        with st.spinner('Reloading the webapp'):
            time.sleep(1.5)
        st.experimental_rerun()
          




