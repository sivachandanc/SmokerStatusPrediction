import streamlit as st
import pandas as pd
import model
import inserting_data
import time

st.set_page_config(page_title="Smoking Prediction",
                   page_icon=":guardsman:")


st.title("Smoking Status Detection")
st.subheader("An End-End Data Engineering Project by Siva Chandan")
df_main = pd.DataFrame()

with st.form("input_df"):
    

    Age = st.number_input("Age",min_value = 21, max_value =98 , \
    help = "Enter your age here(subject have to be 21 to use this)")

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

    answer = st.radio("Add the record to Data base", ("Yes", "No"))

    submit_function = st.form_submit_button("Submit")

if submit_function:
    df = pd.DataFrame({
                'age':[int(Age)], 'height(cm)':[int(height)], 'weight(kg)':[int(weight)], 'waist(cm)':[float(waist)], 'fasting blood sugar':[int(fasting_blood_sugar)],
       'Cholesterol':[int(cholesterol)], 'hemoglobin':[int(hemoglobin)], 'Urine protein':[int(urine_protein)], 'serum creatinine':[float(serum_creatinine)]
    })
    st.dataframe(df)
    smoking_status = model.load_predict(df)
    st.markdown("<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.14.0/css/all.css' integrity='sha384-HzLeBuhoNPvSl5KYnjx0BT+WB0QEEqLprO+NBkkk5gbc67FTaL7XIGa2w1L0Xbgc' crossorigin='anonymous'>", unsafe_allow_html=True)
    if smoking_status == 1:
        # Display the icon
        st.markdown("<p><strong>The Subject is Smoking <i class='fas fa-smoking'></i></strong></p>", unsafe_allow_html=True)
    elif smoking_status == 0:
        # Display the icon
        st.markdown("<p><strong>The Subject is Not Smoking <i class='fas fa-smoking-ban'></i></strong></p>", unsafe_allow_html=True)
    



    if answer == 'Yes':
        with st.spinner('Adding Data'):
            st.dataframe(df)
            inserting_data.inserting_data(df)
            st.success('Record Appended', icon="✅")
                
    elif answer == "No":
        with st.spinner('Reloading the webapp'):
            time.sleep(1.5)
            st.experimental_rerun()
            




