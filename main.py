import streamlit as st
import math

def calculate_meld_na(creatinine, bilirubin, inr, na):
    # Calculate MELD score
    meld = 9.57 * math.log(creatinine) + 3.78 * math.log(bilirubin) + 11.2 * math.log(inr) + 6.43
    # Calculate MELD Na score
    meld_na = meld + 1.32 * (137 - na) - 0.033 * meld * (137 - na)
    # Cap MELD Na score between 6 and 40
    meld_na = max(6, min(40, meld_na))
    return meld_na

st.title('MELD Na Calculator')
st.write('Calculate the MELD Na score to assess the severity of chronic liver disease.')

# Input fields for laboratory values
creatinine = st.number_input('Creatinine (mg/dL)', min_value=0.0, value=1.0, step=0.1)
bilirubin = st.number_input('Bilirubin (mg/dL)', min_value=0.0, value=1.0, step=0.1)
inr = st.number_input('INR', min_value=0.0, value=1.0, step=0.1)
na = st.number_input('Sodium (mEq/L)', min_value=0, max_value=200, value=137, step=1)

if st.button('Calculate MELD Na Score'):
    # Calculate MELD Na score based on input values
    meld_na = calculate_meld_na(creatinine, bilirubin, inr, na)
    st.write('MELD Na Score:', meld_na)
