from tkinter import Tk
from BackEnd.password_generator import generate_password
from BackEnd.data_manager import save_data, find_password
from FrontEnd.ui_setup import setup_ui
#
window = Tk()
setup_ui(window, find_password, generate_password, save_data)
window.mainloop()
