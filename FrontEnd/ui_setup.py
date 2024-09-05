from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage


def setup_ui(window, find_password, generate_password, save_data):
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="FrontEnd/logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0)
    email_label = Label(text="Email/Username:")
    email_label.grid(row=2, column=0)
    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

    website_entry = Entry(width=21)
    website_entry.grid(row=1, column=1)
    website_entry.focus()

    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.insert(0, "hsen8.hsnen@gmail.com")

    password_entry = Entry(width=21)
    password_entry.grid(row=3, column=1)

    search_button = Button(text="Search", width=13, command=lambda: find_password(website_entry.get()))
    search_button.grid(row=1, column=2)

    generate_password_button = Button(text="Generate Password", command=lambda: generate_password(password_entry))
    generate_password_button.grid(row=3, column=2)

    add_button = Button(text="Add", width=36,
                        command=lambda: save_data(website_entry.get(), email_entry.get(), password_entry.get(),
                                                  website_entry, password_entry))
    add_button.grid(row=4, column=1, columnspan=2)

    # Ensure the image variable is kept alive by referencing it
    canvas.image = logo_img
