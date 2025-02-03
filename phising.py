from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pre-trained phishing detection model from the .pkl file
with open("C:/Users/vtu24/Downloads/phisning_dection/phisning_dection[1]/phisning_dection/phisning/phisning/phishing (2).pkl", 'rb') as model_file:
    phishing_model = pickle.load(model_file)

def is_phishing(url):
    # Replace this with your actual prediction logic
    # Example: You might need to preprocess the URL before making predictions
    # prediction = phishing_model.predict(preprocess(url))
    prediction = phishing_model.predict([url])  # Assuming the model expects a list of URLs
    return prediction[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url = request.form['url']
        result = is_phishing(url)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
