import unittest
from unittest.mock import patch, mock_open, MagicMock
from BackEnd.data_manager import save_data, find_password


class MyTestCase(unittest.TestCase):
    @patch("json.load", return_value={"other.com": {"email": "other@example.com", "password": "otherpassword"}})
    @patch("tkinter.messagebox.showinfo")
    def test_find_password_not_found(self, mock_messagebox, mock_json_load):
        website = "example.com"
        find_password(website)
        mock_messagebox.assert_called_once_with(title="Error", message="No details for example.com exist.")


if __name__ == '__main__':
    unittest.main()
