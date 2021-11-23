import json

class TestAPIcase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Welcome to our cars API'

    def test_get_cars(self, api):
        res = api.get('/cars')
        assert res.status == '200 OK'
        assert len(res.json) == 4

    def test_get_car(self, api):
        res = api.get('/cars/2')
        assert res.status == '200 OK'
        assert res.json['make'] == 'Test Car 2'

    def test_get_cats_error(self, api):
        res = api.get('/api/cats/4')
        assert res.status == '400 BAD REQUEST'
        assert "car with id 4" in res.json['message']

    def test_post_cats(self, api):
        mock_data = json.dumps({'make': 'ferrari'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/cars', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 6
