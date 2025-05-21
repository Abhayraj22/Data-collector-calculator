from flask import jsonify
import mysql.connector

def get_user_data():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='prjAI@25',
        database='userdata'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def generate_insights(data):
    total_users = len(data)
    average_age = sum(user['age'] for user in data) / total_users if total_users > 0 else 0
    insights = {
        'total_users': total_users,
        'average_age': average_age
    }
    return insights

def get_analytics(data):
    user_data = get_user_data(data)
    print(user_data)  # Debug: See what data is returned
    insights = generate_insights(user_data)
    return jsonify(insights)