import streamlit as st
st.title("Smoking Status Detection")
st.subheader("An End-End Data Engineering Project by Siva Chandan")


with st.form("input_df"):

    Age = st.number_input("Age",min_value = 21, max_value =98 , \
    help = "Enter your age here(Patient have to be 21 to use this)")

    height = st.number_input("Height(cm)", min_value = 54, max_value = 280, \
    value = 165, help = "Enter the height in cm")

    weight = st.number_input("Weight(kg)",min_value = 30.0, max_value =700.00, \
    value = 65.00, step = 0.01, help = "Enter Weight in KG(Kilo Gram)")

    waist = st.number_input("waist(cm)",min_value = 51.000000, max_value =129.000000, \
    value = 82.000000, step = 0.01 , help = "")

    eyesight = st.number_input("eyesight(left)", value = 1.00,\
    min_value=0.0, max_value=10.00, step=0.01, help = "Enter the left Eyesight value")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")

    # st.number_input("Weight(kg)",min_value = , max_value =, \
    # value = , step = , help = "")


