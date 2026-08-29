import unittest
from unittest.mock import patch, MagicMock
import hmac
import hashlib
import json
import mailifica
from mailifica import Mailifica, Webhooks, AuthenticationError, InvalidRequestError

class TestMailificaPython(unittest.TestCase):
    def setUp(self):
        mailifica.api_key = "ma_test_123456789"
        self.client = Mailifica("ma_test_123456789")

    @patch("requests.request")
    def test_send_email_static(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "email_123", "status": "queued"}
        mock_request.return_value = mock_response

        response = mailifica.Emails.send({
            "from": "onboarding@empresa.ao",
            "to": "cliente@gmail.com",
            "subject": "Boas-vindas",
            "html": "<p>Olá!</p>"
        })

        self.assertEqual(response["id"], "email_123")
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(kwargs["json"]["from"], "onboarding@empresa.ao")
        self.assertEqual(kwargs["headers"]["Authorization"], "Bearer ma_test_123456789")

    @patch("requests.request")
    def test_send_email_instance(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "email_456", "status": "sent"}
        mock_request.return_value = mock_response

        response = self.client.emails.send({
            "from": "onboarding@empresa.ao",
            "to": ["cliente@gmail.com"],
            "subject": "Teste",
            "html": "<p>Teste</p>"
        })

        self.assertEqual(response["id"], "email_456")

    @patch("requests.request")
    def test_batch_send(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": [{"id": "1"}, {"id": "2"}]}
        mock_request.return_value = mock_response

        response = mailifica.Batch.send([
            {"from": "a@a.ao", "to": "b@b.com", "subject": "1", "html": "1"},
            {"from": "a@a.ao", "to": "c@c.com", "subject": "2", "html": "2"}
        ])

        self.assertEqual(len(response["data"]), 2)

    def test_webhook_verification(self):
        secret = "whsec_test_123"
        payload = json.dumps({"id": "evt_1", "type": "email.delivered"})
        signature = hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()

        is_valid = Webhooks.verify_signature(payload, signature, secret)
        self.assertTrue(is_valid)

        event = Webhooks.construct_event(payload, signature, secret)
        self.assertEqual(event["id"], "evt_1")

        is_invalid = Webhooks.verify_signature(payload, "bad_signature", secret)
        self.assertFalse(is_invalid)

    @patch("requests.request")
    def test_error_handling(self, mock_request):
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": {"message": "Invalid API Key", "code": "unauthorized"}}
        mock_request.return_value = mock_response

        with self.assertRaises(AuthenticationError):
            mailifica.Emails.send({"from": "a@a.ao", "to": "b@b.ao", "subject": "a", "html": "a"})

if __name__ == "__main__":
    unittest.main()
