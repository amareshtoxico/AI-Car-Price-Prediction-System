from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# ---------- Load trained objects ----------
model = joblib.load("reg_model.pkl")
scaler = joblib.load("scaler.pkl")
te = joblib.load("target_encode.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        try:
            # ---------- Numeric Inputs ----------
            Year = int(request.form.get("Year"))
            Present_Price = float(request.form.get("Present_Price"))
            Kms_Driven = int(request.form.get("Kms_Driven"))
            Owner = int(request.form.get("Owner"))

            # ---------- Categorical Inputs ----------
            Fuel_Type = request.form.get("Fuel_Type")
            Seller_Type = request.form.get("Seller_Type")
            Transmission = request.form.get("Transmission")
            Brand = request.form.get("Brand").strip().title()

            # ---------- Encoding ----------
            Fuel_Type = {"Petrol": 0, "Diesel": 1, "CNG": 2}[Fuel_Type]
            Seller_Type = {"Individual": 0, "Dealer": 1}[Seller_Type]
            Transmission = {"Manual": 0, "Automatic": 1}[Transmission]

            # ---------- DataFrame ----------
            input_df = pd.DataFrame({
                "Year": [Year],
                "Present_Price": [Present_Price],
                "Kms_Driven": [Kms_Driven],
                "Owner": [Owner],
                "Fuel_Type": [Fuel_Type],
                "Seller_Type": [Seller_Type],
                "Transmission": [Transmission],
                "Brand": [Brand]
            })

            # ---------- Target Encoding ----------
            input_df["Brand"] = te.transform(input_df[["Brand"]])

            # ---------- Column Order (CRITICAL) ----------
            final_cols = [
                "Year",
                "Present_Price",
                "Kms_Driven",
                "Owner",
                "Fuel_Type",
                "Seller_Type",
                "Transmission",
                "Brand"
            ]
            input_df = input_df[final_cols]

            # ---------- Scaling ----------
            scale_cols = ["Year", "Present_Price", "Kms_Driven", "Brand"]
            input_df[scale_cols] = scaler.transform(input_df[scale_cols])

            # ---------- Raw Prediction ----------
            raw_pred = model.predict(input_df)[0]

            # ---------- Post-processing (CRITICAL) ----------
            # Clamp prediction to realistic range
            MIN_PRICE = 0.5  # 50,000 INR
            MAX_PRICE = 50.0  # 50 Lakhs (upper safety cap)

            prediction = max(MIN_PRICE, raw_pred)
            prediction = min(prediction, MAX_PRICE)
            prediction = round(prediction, 2)

            # ---------- Confidence Score (AFTER CLAMPING) ----------
            deviation = abs(Present_Price - prediction)

            if prediction <= 1:
                confidence = 70
            elif deviation < 1:
                confidence = 92
            elif deviation < 2:
                confidence = 85
            elif deviation < 3:
                confidence = 75
            else:
                confidence = 65


        except Exception as e:
            print("Error:", e)
            prediction = "Invalid Input"
            confidence = 0

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
