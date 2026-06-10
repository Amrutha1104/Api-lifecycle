from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ammu@1104",
        database="api_lifecycle"
    )

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return "Data saved successfully!"

    return render_template("index.html")



@app.route("/users", methods=["GET"])
def get_users():

    conn = get_db_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)