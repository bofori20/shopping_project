🛒 Customer Shopping Intention Prediction
This project predicts whether a user will complete a purchase during an online shopping session based on their behavior. By leveraging TensorFlow and a neural network model, the app identifies patterns from session metrics like bounce rates, product-related duration, exit rates, and more.

🔍 Project Highlights
Built a classification model using Keras (TensorFlow backend)

Deployed using Django with a clean web interface

Input features include session durations, traffic types, visitor types, bounce and exit rates, etc.

Visualizations show how key metrics affect purchase behavior

📁 Dataset
Name: online_shoppers_intention.csv
Source: UCI Machine Learning Repository
Size: ~12,330 records

📊 Features Used
Administrative_Duration

Informational_Duration

ProductRelated

BounceRates

ExitRates

PageValues

SpecialDay

OperatingSystems

Browser

Region

TrafficType

Weekend

VisitorType (One-hot encoded)

📌 Model
Type: Neural Network (.h5 file)

Preprocessing: StandardScaler (optional)

Output: Binary classification — Will Purchase or Will Not Purchase

🖥️ Django Deployment
Run locally:
bash
Copy
Edit
git clone https://github.com/your-username/shopping-intention-predictor.git
cd shopping-intention-predictor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Then navigate to: http://127.0.0.1:8000/

📷 Sample Visualizations
Revenue distribution

Bounce vs Revenue

Exit rate correlation

Page value insights

Feature correlation heatmap

💡 Business Impact
This model helps businesses:

Target high-converting visitors

Understand dropout patterns

Optimize content and promotions

Enhance personalized shopping experiences

shopping_project/
├── predictor/
│   ├── templates/
│   ├── static/
│   ├── model/
│   ├── views.py
│   ├── urls.py
├── shopping_site/
├── manage.py
├── requirements.txt
├── README.md

🤝 Contributions
Pull requests are welcome! For major changes, open an issue first.
