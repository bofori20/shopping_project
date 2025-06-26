from django.shortcuts import render
import numpy as np
import os
import requests
from tensorflow.keras.models import load_model

# Load model
#MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'customer_shopping-intention_model.h5')
#model = load_model(MODEL_PATH)


MODEL_URL = "https://github.com/bofori20/shopping_project/releases/tag/v1.0"
MODEL_PATH = 'predictor/model/customer_shopping-intention_model.h5'

def download_model_if_needed():
    if not os.path.exists(MODEL_PATH):
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)

download_model_if_needed()
model = load_model(MODEL_PATH)

# --- Prediction View ---
def predict_view(request):
    if request.method == 'POST':
        try:
            # --- Extract Inputs ---
            admin_dur = float(request.POST.get('Administrative_Duration'))  # (0 - 300)
            info_dur = float(request.POST.get('Informational_Duration'))    # (0 - 300)
            product_related = float(request.POST.get('ProductRelated'))     # (0 - 1000)
            bounce = float(request.POST.get('BounceRates'))                 # (0.0 - 1.0)
            exit_rate = float(request.POST.get('ExitRates'))               # (0.0 - 1.0)
            page_val = float(request.POST.get('PageValues'))               # (0.0 - 400)
            special_day = float(request.POST.get('SpecialDay'))            # (0.0 - 1.0)

            os_val = int(request.POST.get('OperatingSystems'))             # (1 - 8)
            browser = int(request.POST.get('Browser'))                     # (1 - 13)
            region = int(request.POST.get('Region'))                       # (1 - 9)
            traffic = int(request.POST.get('TrafficType'))                 # (1 - 20)

            weekend = request.POST.get('Weekend') == 'True'               # True/False dropdown
            visitor_type = request.POST.get('VisitorType')               # Multi-hot encoded below

            # --- Encode Weekend ---
            weekend_encoded = 1 if weekend else 0

            # --- Multi-hot encode visitor types ---
            new_visitor = 1 if visitor_type == 'New_Visitor' else 0
            returning_visitor = 1 if visitor_type == 'Returning_Visitor' else 0
            other_visitor = 1 if visitor_type == 'Other' else 0

            # --- Assemble Input Features (17 total) ---
            features = [
                admin_dur, info_dur, product_related, bounce, exit_rate, page_val,
                special_day, os_val, browser, region, traffic, weekend_encoded,
                new_visitor, other_visitor, returning_visitor
            ]

            input_array = np.array([features])  # 2D input for Keras

            # --- Predict ---
            result = model.predict(input_array)[0][0]
            prediction = '🛍️ Will Purchase' if result > 0.5 else '❌ Will Not Purchase'

            return render(request, 'predictor/result.html', {
                'prediction': prediction
            })

        except Exception as e:
            return render(request, 'predictor/form.html', {
                'error': f"Prediction failed: {e}"
            })

    # Preloaded example values and field descriptions
    field_info = {
        'Administrative_Duration': {'value': 10.0, 'desc': 'Time spent on administrative pages (0–300)'},
        'Informational_Duration': {'value': 5.0, 'desc': 'Time on informational pages (0–300)'},
        'ProductRelated': {'value': 25.0, 'desc': 'Number of product-related pages visited (0–1000)'},
        'BounceRates': {'value': 0.2, 'desc': 'Proportion of single-page sessions (0.0–1.0)'},
        'ExitRates': {'value': 0.3, 'desc': 'Proportion of exits from this page (0.0–1.0)'},
        'PageValues': {'value': 50.0, 'desc': 'Estimated revenue from pages (0.0–400)'},
        'SpecialDay': {'value': 0.0, 'desc': 'Closeness to a special day (0.0–1.0)'},

        'OperatingSystems': {'value': 2, 'desc': '1=Windows, 2=Mac, 3=Linux, etc.'},
        'Browser': {'value': 1, 'desc': '1=Chrome, 2=Firefox, 3=Edge, etc.'},
        'Region': {'value': 3, 'desc': 'Geographical region (1–9)'},
        'TrafficType': {'value': 1, 'desc': 'Traffic source type (1–20)'},

        'Weekend': {'value': 'False', 'desc': 'Is the visit during the weekend?'},
        'VisitorType': {'value': 'Returning_Visitor', 'desc': 'Returning, New, or Other visitor'}
    }

    return render(request, 'predictor/form.html', {'field_info': field_info})


# --- Project Info Page ---
def project_info(request):
    return render(request, 'predictor/project_info.html')







