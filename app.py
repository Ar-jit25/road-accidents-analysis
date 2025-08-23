from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load cleaned CSV
df = pd.read_csv('data/RTA Dataset.csv')

@app.route('/api/data')
def get_data():
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
