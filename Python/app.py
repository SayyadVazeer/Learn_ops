import os

from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    tasks = []
    next_task_id = 1

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/tasks")
    def list_tasks():
        return jsonify(tasks)

    @app.post("/tasks")
    def create_task():
        nonlocal next_task_id

        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Request body must be a JSON object"}), 400

        title = payload.get("title")
        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "A non-empty title is required"}), 400

        task = {
            "id": next_task_id,
            "title": title.strip(),
            "completed": False,
        }
        tasks.append(task)
        next_task_id += 1
        return jsonify(task), 201

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id):
        task = next((item for item in tasks if item["id"] == task_id), None)
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        tasks.remove(task)
        return "", 204

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
