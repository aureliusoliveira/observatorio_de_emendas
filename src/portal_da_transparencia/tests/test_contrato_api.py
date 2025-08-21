import pytest
import requests
from unittest.mock import patch, MagicMock
from ..contrato_api import PortalDaTransparenciaAPI

@pytest.fixture
def fake_env(monkeypatch):
    monkeypatch.setenv("chave-api-dados", "mocked-chave-api-dados")

@pytest.fixture()
@patch("portal_da_transparencia.contrato_api.PortalDaTransparenciaAPI.__abstractmethods__", set())
def fixture_portal_da_transparencia_api(fake_env):
    return PortalDaTransparenciaAPI()


def mocked_requests_get(**kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self) -> None:
            if self.status_code != 200:
                raise Exception

    if kwargs['url'] == "valid_endpoint":
        return MockResponse(json_data={"foo": "bar"}, status_code=200)
    else:
        return MockResponse(json_data=None, status_code=404)

class TestPortalDaTransparenciaAPI:

    @patch("portal_da_transparencia.contrato_api.requests.get")
    def test_get_data_ok(self, mock_get, fixture_portal_da_transparencia_api):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"ok": True}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        resp = fixture_portal_da_transparencia_api.get_data()
        mock_get.assert_called_once()
        _, kwargs = mock_get.call_args
        assert kwargs["headers"] == {"chave-api-dados": "mocked-chave-api-dados"}
        assert resp == {"ok": True}


    @patch("portal_da_transparencia.contrato_api.requests.get", side_effect=mocked_requests_get)
    @patch("portal_da_transparencia.contrato_api.PortalDaTransparenciaAPI._build_url", return_value='valid_endpoint')
    def test_get_data_with_valid_endpoint(self, mock_build_url, mock_requests, fixture_portal_da_transparencia_api):
       assert fixture_portal_da_transparencia_api.get_data() == {"foo": "bar"}

    @patch("portal_da_transparencia.contrato_api.requests.get", side_effect=mocked_requests_get)
    @patch("portal_da_transparencia.contrato_api.PortalDaTransparenciaAPI._build_url", return_value="invalid_endpoint")
    def test_get_data_with_invalid_endpoint(self, mock_build_url, mock_requests, fixture_portal_da_transparencia_api):
       with pytest.raises(Exception):
           fixture_portal_da_transparencia_api.get_data()
