import unittest
import unittest
from unittest.mock import patch, mock_open, MagicMock
from BackEnd.data_manager import save_data, find_password


class MyTestCase(unittest.TestCase):
    @patch("json.dump")
    @patch("json.load")
    @patch("builtins.open", new_callable=mock_open,
           read_data='{"example.com": {"email": "old@example.com", "password": "oldpassword"}}')
    @patch("tkinter.messagebox.showinfo")
    def test_save_data_existing_file(self, mock_messagebox, mock_open, mock_json_load, mock_json_dump):
        website = "newsite.com"
        email = "new@example.com"
        password = "newpassword123"

        # Mock Entry widgets
        mock_website_entry = MagicMock()
        mock_password_entry = MagicMock()

        # Call the function
        save_data(website, email, password, mock_website_entry, mock_password_entry)

        # Verify messagebox
        mock_messagebox.assert_called_once_with(title=website, message=f"Email: {email}\nPassword: {password}\nSaved")
        # Verify that delete method is called on both entries
        mock_website_entry.delete.assert_called_once_with(0, "end")
        # mock_password_entry.delete.assert_called_once_with(0, "end")

if __name__ == '__main__':
    unittest.main()
