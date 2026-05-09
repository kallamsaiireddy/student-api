from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Sai", "course": "DevOps", "grade": "A"},
    {"id": 2, "name": "Ravi", "course": "Cloud Computing", "grade": "B"},
    {"id": 3, "name": "Priya", "course": "Kubernetes", "grade": "A+"},
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)