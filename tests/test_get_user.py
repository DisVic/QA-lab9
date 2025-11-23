import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestGetUser:
    """Тесты для GET запроса - получение пользователя"""
    
    def test_get_user_status_code(self):
        """Проверка статус кода"""
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        print("✓ Status code is 200")

    def test_get_user_json_structure(self):
        """Проверка структуры JSON"""
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()
        
        expected_fields = ["id", "name", "username", "email", "address", "phone", "website", "company"]
        for field in expected_fields:
            assert field in data, f"Field '{field}' is missing in response"
        print("✓ JSON structure is correct")

    def test_get_user_field_values(self):
        """Проверка значений полей"""
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()
        
        assert data["id"] == 1
        assert isinstance(data["name"], str) and len(data["name"]) > 0
        assert isinstance(data["username"], str) and len(data["username"]) > 0
        assert "@" in data["email"]
        print("✓ Field values are correct")

    def test_get_user_response_time(self):
        """Проверка времени ответа"""
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.elapsed.total_seconds() < 2, "Response time is too long"
        print(f"✓ Response time is acceptable: {response.elapsed.total_seconds()}s")
