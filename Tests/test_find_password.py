
import unittest
from unittest.mock import patch, mock_open, MagicMock
from BackEnd.data_manager import save_data, find_password


class MyTestCase(unittest.TestCase):
    @patch("json.load", side_effect=FileNotFoundError)
    @patch("tkinter.messagebox.showinfo")
    def test_find_password_no_file(self, mock_messagebox, mock_json_load):
        website = "example.com"
        find_password(website)

        mock_messagebox.assert_called_once_with(title="Error", message="No Data File Found.")


@patch("json.load", return_value={"example.com": {"email": "test@example.com", "password": "password123"}})
@patch("tkinter.messagebox.showinfo")
def test_find_password_found(self, mock_messagebox, mock_json_load):
    website = "example.com"
    find_password(website)

    mock_messagebox.assert_called_once_with(title=website, message="Email: test@example.com\nPassword: password123")


if __name__ == '__main__':
    unittest.main()
