import unittest
from unittest.mock import patch, mock_open, MagicMock
from BackEnd.data_manager import save_data, find_password



class MyTestCase(unittest.TestCase):
    @patch("json.dump")
    @patch("json.load")
    @patch("builtins.open", new_callable=mock_open)
    @patch("tkinter.messagebox.showinfo")
    def test_save_data_new_file(self, mock_messagebox, mock_open, mock_json_load, mock_json_dump):
        mock_json_load.side_effect = FileNotFoundError  # Simulate no file found

        website = "example.com"
        email = "test@example.com"
        password = "password123"

        # Mock Entry widgets
        mock_website_entry = MagicMock()
        mock_password_entry = MagicMock()

        # Call the function
        save_data(website, email, password, mock_website_entry, mock_password_entry)

        # Verify JSON dump
        mock_json_dump.assert_called_once_with({website: {"email": email, "password": password}}, mock_open(), indent=4)
        # Verify messagebox
    # mock_messagebox.assert_called_once_with(title=website, message=f"Email: {email}\nPassword: {password}\nSaved")


if __name__ == '__main__':
    unittest.main()
