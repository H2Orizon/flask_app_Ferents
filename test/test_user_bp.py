import unittest
from app import create_app,db
from app.user.models import User

class FlaskAppTestCase(unittest.TestCase):
    # def setUp(self):
    #     """Налаштування клієнта тестування перед кожним тестом."""
    #     app.config["TESTING"] = True
    #     self.client = app.test_client()
    # def test_greetings_page(self):
    #     """Тест маршруту /user/<name>."""
    #     response = self.client.get("user/Someone?age=30")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b"Someone", response.data)
    #     self.assertIn(b"30", response.data)
    # def test_admin_page(self):
    #     """Тест маршруту /admin, який перенаправляє."""
    #     response = self.client.get("user/admin", follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b"Administrator", response.data)
    #     self.assertIn(b"19", response.data)
    def setUp(self):
        self.app = create_app(config_name = "test_conf")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    def test_register_page_loads(self):
        response = self.client.get('/user/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'register', response.data)

    def test_login_page_loads(self):
        response = self.client.get('/user/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'login', response.data)

    def test_user_registration(self):
        response = self.client.post('/user/register', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'testuser@example.com')

    def test_user_login(self):
        with self.app.app_context():
            user = User(username='testuser', email='testuser@example.com', password='testpassword')
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/user/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_user_logout(self):
        with self.app.app_context():
            user = User(username='testuser', email='testuser@example.com', password='testpassword')
            db.session.add(user)
            db.session.commit()

        self.client.post('/user/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.get('/user/logout')
        self.assertEqual(response.status_code, 302)

    if __name__ == "__main__":
        unittest.main()