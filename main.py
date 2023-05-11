from customtkinter import *
from os import system

from log import log


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        try:
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
                height=50,
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

            for index, (string, function) in enumerate({
                "Open Website": self.open_web,
                "Create new user": self.create_user
            }.items()):
                CTkButton(
                    master=self.aside,
                    text=string,
                    fg_color="#292929",
                    width=200,
                    height=50,
                    corner_radius=0,
                    command=function
                ).pack(side="top")

        except Exception as e:
            log(error=e, message="Erro na hora de inciar os elementos básicos do App")

    def open_web(self):
        self.reload()
        self.systems = ["Google", "Facebook", "YouTube", "Instagram",]

        def btn_command():
            if self.current_elements[1].get() in self.systems:
                log(message='Execute', end="\n")
        try:
            self.current_elements.append(
                CTkLabel(
                    master=self.header,
                    font=CTkFont(family="Arial", size=25),
                    text="Open Website",
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
            self.current_elements[1].set("Choose a website")
            self.current_elements[2].pack(side="right", expand="True")

        except Exception as e:
            log(error=e, message="Erro no create_card")

    def create_user(self) -> None:
        self.reload()

        def btn_command():
            self.user_info = {
                "name": self.current_elements[1].get(),
                "username": self.current_elements[2].get(),
                "id": self.current_elements[3].get(),
                "email": self.current_elements[4].get(),
                "phone": self.current_elements[5].get(),
            }
            for i in self.user_info.values():
                if not i:
                    return
            log(message=f"Execute\n{self.user_info}", end="\n")

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

            for i in ["Name", "Username", "ID", "E-mail", "Phone"]:
                self.current_elements.append(
                    CTkEntry(
                        master=self.main,
                        placeholder_text=i,
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

            list(i.pack(expand="True") for i in self.current_elements)

        except Exception as e:
            log(error=e, message="Erro na criação dos elementos do create_user")

    def reload(self) -> None:
        system('cls')
        try:
            list(i.destroy() for i in self.current_elements)
        except Exception as e:
            log(error=e, message="Erro na hora de recarregar elementos ou elementos carregados de forma errada")
        finally:
            self.current_elements.clear()


if __name__ == '__main__':
    system('cls')
    app = App()
    app.mainloop()
