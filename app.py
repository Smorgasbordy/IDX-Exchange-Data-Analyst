

import streamlit as st
import joblib
import numpy as np
from pathlib import Path
import pandas as pd

model_path = Path(__file__).parent / "model.joblib"
encoder_path = Path(__file__).parent / 'city_encoder.joblib'
encoder = joblib.load(encoder_path)
model = joblib.load(model_path)

st.title("Interactive Property Price Prediction")

"""This app accompanies my internship project for IDX Echange, 
in which I built a model to predict housing prices in California.
Users input a city in California, as well as a living area amount,
lot size, and bedroom/bathroom amounts,
and then the app outputs a prediction for the close price of that hypothetical property. 
 
Note that the model used for this app is a simplified form of the one used in 
the project proper, trained only on the five features listed above. 
These features were chosen for this app because
they are the ones that most commonly accompany online listings, making them easy to input 
and compare against real prices.
Though these features have strong predictive
power, they are limited in comparison to my full model. For a better understaing of its accuracy,
the model used in this app performs with
a test $r^2$ score of roughly 0.82, while the full model's is 0.92. 

Have fun!"""

"#### Choose Property Features"

LivingArea = st.slider("Living Area (sqft):", 250, 5000, step=50)
LotSize = st.slider("Lot Size (sqft):", 500, 10000, step=50)
Beds = st.slider("Number of Bedrooms:", 1, 10)
Baths = st.slider("Number of Bathrooms:", 1, 10)

"    "

"If no city is inputted, Sacramento will be used as the default"
city = st.text_input("City in California:", placeholder="Sacramento")


input_data = pd.DataFrame(
    [[LivingArea, LotSize, Baths, Beds, city]],
    columns=["LivingArea", "LotSizeSquareFeet", "BathroomsTotalInteger", "BedroomsTotal", "City"]
)

"#### Prediction"

if st.button("Predict Price"):
  encoded_city = encoder.transform(input_data[["City"]])[0][0]

  input_data_2 = pd.DataFrame(
    [[LivingArea, LotSize, Baths, Beds, encoded_city]],
    columns=["LivingArea", "LotSizeSquareFeet", "BathroomsTotalInteger", "BedroomsTotal", "city_enc"]
)
  
  prediction = model.predict(input_data_2)[0]
  st.success(f"Estimated Price: ${prediction:,.2f}")

st.write("")