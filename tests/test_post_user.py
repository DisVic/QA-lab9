import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestPostUser:
    """Тесты для POST запроса - создание пользователя"""
    
    user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com",
        "phone": "1-770-736-8031 x56442",
        "website": "johndoe.org",
        "company": {
            "name": "Example Corp",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }

    def test_post_user_status_code(self):
        """Проверка статус кода"""
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        print("✓ Status code is 201")

    def test_post_user_json_structure(self):
        """Проверка структуры JSON"""
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        data = response.json()
        
        expected_fields = ["id", "name", "username", "email"]
        for field in expected_fields:
            assert field in data, f"Field '{field}' is missing in response"
        print("✓ JSON structure is correct")

    def test_post_user_created_id_is_int(self):
        """Проверка что id созданного пользователя — целое число (устойчивее, чем фиксированное значение)"""
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        data = response.json()
        assert isinstance(data.get("id"), int), f"Expected integer id, got {data.get('id')!r}"
        print("✓ Created user has integer ID")

    def test_post_user_data_matches(self):
        """Проверка соответствия отправленных и полученных данных"""
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        response_data = response.json()
        
        assert response_data["name"] == self.user_data["name"]
        assert response_data["username"] == self.user_data["username"]
        assert response_data["email"] == self.user_data["email"]
        print("✓ Response data matches request data")

    def test_post_user_content_type(self):
        """Проверка заголовка Content-Type"""
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Expected application/json, got {content_type}"
        print("✓ Content-Type is application/json")
