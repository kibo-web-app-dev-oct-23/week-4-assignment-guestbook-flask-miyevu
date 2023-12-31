##### DO NOT EDIT THIS FILE
import unittest
import sqlite3
from app import app, get_db

class GuestbookTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DATABASE'] = 'test_guestbook.db'
        self.client = app.test_client()
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS guests (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    message TEXT NOT NULL
                )
            """)

    def tearDown(self):
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE guests")

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_guest_entry(self):
        response = self.client.post('/', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, Guestbook!'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM guests WHERE email='john@example.com'")
            entry = cur.fetchone()
            self.assertIsNotNone(entry)
            self.assertEqual(entry[1], 'John Doe')
            self.assertEqual(entry[2], 'john@example.com')
            self.assertEqual(entry[3], 'Hello, Guestbook!')

if __name__ == '__main__':
    unittest.main()
