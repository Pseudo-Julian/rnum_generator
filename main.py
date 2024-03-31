import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import Password
import customtkinter as CTk
from PIL import Image


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Password generator")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("3.png"), size=(460, 150))
        self.logo_lablel = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_lablel.grid(row=0, column=0)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100,
                                          command=self.set_password)

        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cd_digits_var = tkinter.StringVar()
        self.cd_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cd_digits_var,
                                         onvalue=digits, offvalue="")
        self.cd_digits.grid(row=2, column=0, padx=10)

        self.cd_lower_var = tkinter.StringVar()
        self.cd_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cd_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cd_lower.grid(row=2, column=1)

        self.cd_upper_var = tkinter.StringVar()
        self.cd_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-z", variable=self.cd_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cd_upper.grid(row=2, column=2)

        self.cd_symbol_var = tkinter.StringVar()
        self.cd_symbol = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cd_symbol_var,
                                         onvalue=punctuation, offvalue="")
        self.cd_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=["Dark", "Light", "System"],
                                                             command=self.appearance_mode_option_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, 12)
        self.appearance_mode_option_menu.set("System")

    def appearance_mode_option_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        chars = "".join(self.cd_digits_var.get() + self.cd_lower_var.get() + self.cd_upper_var.get() +
                        self.cd_symbol_var.get())

        return chars

    def set_password(self):
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, Password.create_new(length=int(self.password_length_slider.get()),
                                                          characters=self.get_characters()))


if __name__ == "__main__":
    app = App()
    app.mainloop()
