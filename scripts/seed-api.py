from flask import Flask, jsonify
import seed as core

app = Flask(__name__)

@app.route('/seed', methods=['POST'])
def seed():
    print(f"Adding users...")
    core.add_users()
    return jsonify({"message": "Seeding complete!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
