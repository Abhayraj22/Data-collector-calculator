from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from analytics.analytics import get_user_data, generate_insights

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'prjAI@25'
app.config['MYSQL_DB'] = 'userdata'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/submit-data', methods=['POST'])
def submit_data():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, age) VALUES (%s, %s, %s)",
        (data['name'], data['email'], data['age'])
    )
    mysql.connection.commit()
    cursor.close()
    # Get all user data and generate insights
    users = get_user_data()
    insights = generate_insights(users)
    return jsonify({'message': 'Data submitted successfully!', 'insights': insights}), 201

@app.route('/analytics', methods=['GET'])
def get_analytics():
    users = get_user_data()
    print("Users:", users)  # This will print the user data to your terminal
    insights = generate_insights(users)
    print("Insights:", insights)  # This will print the insights to your terminal
    return jsonify(insights)

if __name__ == '__main__':
    app.run(debug=True)

# (HTML code removed; place it in your index.html template file)