import unittest

from app import create_app


class TaskApiTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_home_documents_all_endpoints(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task API", response.data)
        for endpoint in ("/health", "/tasks", "/tasks/&lt;id&gt;"):
            self.assertIn(endpoint.encode(), response.data)
        for method in (b"GET", b"POST", b"DELETE"):
            self.assertIn(method, response.data)

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_create_and_list_task(self):
        created = self.client.post("/tasks", json={"title": "Learn Docker"})

        self.assertEqual(created.status_code, 201)
        task = created.get_json()
        self.assertEqual(task["title"], "Learn Docker")
        self.assertEqual(task["completed"], False)

        listed = self.client.get("/tasks")
        self.assertEqual(listed.get_json(), [task])

    def test_create_task_requires_non_empty_title(self):
        response = self.client.post("/tasks", json={"title": "  "})

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_delete_task(self):
        created = self.client.post("/tasks", json={"title": "Practice"})
        task_id = created.get_json()["id"]

        deleted = self.client.delete(f"/tasks/{task_id}")

        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.client.get("/tasks").get_json(), [])

    def test_delete_missing_task_returns_not_found(self):
        response = self.client.delete("/tasks/999")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
