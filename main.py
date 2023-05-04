from customtkinter import *
from os import system

from log import log


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        try:
            self.service_options = ["Create cards", "Create new user"]
            self.function = [self.create_card, self.create_user]

            set_appearance_mode("dark")
            self.title('')
            self.geometry('800x500')
            self.resizable(width=True, height=True)
            self.current_elements = list()

            self.aside = CTkFrame(
                master=self,
                width=200,
                fg_color="#292929",
                bg_color="#1A1A1A",
                corner_radius=0
            )
            self.aside.pack(side="left", fill="y")

            self.header = CTkFrame(
                master=self,
                fg_color="#2E4053",
                corner_radius=0,
            )
            self.header.pack(side="top", fill="x")

            self.main = CTkFrame(
                master=self,
                width=600,
                height=450,
                fg_color="#4c4f56",
                corner_radius=0,
            )
            self.main.pack(side="bottom", fill="both", expand="True")

            self.tittle = CTkLabel(
                master=self.aside,
                text="BingLing",
                width=200,
                height=50,
                font=CTkFont(size=30, weight="bold"),
                text_color="white",
                fg_color="#292929",
                corner_radius=0
            )
            self.tittle.pack(side="top")

            self.menu_btn = list()
            for element in range(len(self.service_options)):
                self.menu_btn.append(CTkButton(
                    master=self.aside,
                    text=self.service_options[element],
                    fg_color="#292929",
                    width=200,
                    height=50,
                    corner_radius=0,
                    command=self.function[
                        element - (len(self.service_options) - len(self.function))],
                ))
                self.menu_btn[element].pack(side="top")

        except Exception as e:
            log(error=e, message="Erro na hora de inciar os elementos básicos do App")

    def create_card(self):
        self.reload()
        self.systems = ["WVT", "BPMS", "CIS", "PSW"]

        def btn_command():
            if self.current_elements[1].get() in self.systems:
                log(message='Execute', end="\n")
        try:
            self.current_elements.append(
                CTkLabel(
                    master=self.header,
                    font=CTkFont(family="Arial", size=25),
                    text="Create Cards",
                    height=50,
                    width=50,
                    bg_color="#2E4053",
                )
            )

            self.current_elements.append(
                CTkComboBox(
                    master=self.main,
                    font=CTkFont(family="Arial Rounded MT", size=15),
                    values=self.systems,
                    width=350,
                    height=40,
                    bg_color="#4c4f56",
                )
            )

            self.current_elements.append(
                CTkButton(
                    master=self.main,
                    font=CTkFont(family="Arial", size=15),
                    text='Confirm',
                    bg_color="#4c4f56",
                    command=btn_command
                )
            )

            self.current_elements[0].pack()
            self.current_elements[1].pack(side="left", expand="True")
            self.current_elements[1].set("Choose a system")
            self.current_elements[2].pack(side="right", expand="True")

        except Exception as e:
            log(error=e, message="Erro no create_card")

    def create_user(self) -> None:
        self.reload()

        def btn_command():
            user_info = [
                self.current_elements[0+1].get(),
                self.current_elements[1+1].get(),
                self.current_elements[2+1].get(),
                self.current_elements[3+1].get(),
                self.current_elements[4+1].get(),
                self.current_elements[5+1].get()
            ]
            for i in user_info:
                if not i:
                    return
            log(message="Execute", end="\n")

        try:
            self.current_elements.append(
                CTkLabel(
                    master=self.header,
                    font=CTkFont(family="Arial", size=25),
                    text="Create User",
                    height=50,
                    width=50,
                    bg_color="#2E4053",
                )
            )

            self.current_elements.append(
                CTkEntry(
                    master=self.main,
                    placeholder_text="Name",
                    width=350,
                    height=40
                )
            )

            self.current_elements.append(
                CTkEntry(
                    master=self.main,
                    placeholder_text="Username",
                    width=350,
                    height=40
                )
            )

            self.current_elements.append(
                CTkEntry(
                    master=self.main,
                    placeholder_text="ID",
                    width=350,
                    height=40
                )
            )

            self.current_elements.append(
                CTkEntry(
                    master=self.main,
                    placeholder_text="E-mail",
                    width=350,
                    height=40
                )
            )

            self.current_elements.append(
                CTkEntry(
                    master=self.main,
                    placeholder_text="Phone",
                    width=350,
                    height=40,
                )
            )

            self.current_elements.append(
                CTkEntry(
                    master=self.main,
                    placeholder_text="ID Reference",
                    width=350,
                    height=40
                )
            )

            self.current_elements.append(
                CTkButton(
                    master=self.main,
                    font=CTkFont(family="Arial", size=15),
                    text='Confirm',
                    bg_color="#4c4f56",
                    command=btn_command,
                )
            )
            self.current_elements[0].pack()

            for i in range(1, 8):
                self.current_elements[i].pack(expand="True")

        except Exception as e:
            log(error=e, message="Erro na criação dos elementos do create_user")

    def reload(self) -> None:
        try:
            system('cls')
            for i in range(len(self.current_elements)):
                self.current_elements[i].destroy()
            self.current_elements.clear()

        except Exception as e:
            log(error=e, message="Erro na hora de recarregar elementos")


if __name__ == '__main__':
    system('cls')
    app = App()
    app.mainloop()
