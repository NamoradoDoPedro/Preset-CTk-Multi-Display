import string
from customtkinter import *
from tkinter import *

from os import system
from random import randint as r, choice as c, choices as cs
from datetime import datetime, date


class Generate:
    @staticmethod
    def generate_cpf():
        cpf = [r(0, 9) for _ in range(9)]

        for _ in range(2):
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
            cpf.append(11 - val if val > 1 else 0)

        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

    @staticmethod
    def generate_rg() -> None:
        rg = [r(0, 9) for _ in range(9)]
        return '%s%s.%s%s%s.%s%s%s-%s' % tuple(rg)

    @staticmethod
    def generate_name(project: str = None):
        now = datetime.now()
        day = now.strftime("%d")
        month = now.strftime("%m")
        hour = now.strftime("%H").zfill(2)
        minute = now.strftime("%M").zfill(2)
        if project is None:
            return f"PJ_{day}{month}{hour}{minute}"
        else:
            p = project.lower()
            if p == "sullivan":
                return f"PJ_SUV_{day}{month}{hour}{minute}"
            elif p == "hauwei":
                return f"TESTEHAUWEI_{day}{month}{hour}{minute}"
            elif p == "zhone":
                return f"TESTEZHONE_{day}{month}{hour}{minute}"

    @staticmethod
    def generate_number():
        valid_codes = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21',
                       '22', '24', '27', '28', '31', '32', '33', '34', '35', '37',
                       '38', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                       '51', '53', '54', '55', '61', '62', '63', '64', '65', '66',
                       '67', '68', '69', '71', '73', '74', '75', '77', '79', '81',
                       '82', '83', '84', '85', '86', '87', '88', '89', '91', '92',
                       '93', '94', '95', '96', '97', '98', '99']
        ddd = c(valid_codes)
        p1 = r(9000, 9999)
        p2 = r(1000, 9999)

        # return f"{ddd}9{p1}{p2}"
        return f"({ddd}) 9{p1}-{p2}"

    @staticmethod
    def generate_email():
        users = ['john', 'jane', 'mary', 'david',
                 'alice', 'bob', 'peter', 'emma', 'alex', 'olivia']
        domains = ['example.com', 'sample.net',
                   'test.org', 'fake.email', 'mydomain.com']
        user = c(users) + ''.join(cs(string.digits, k=3))
        domain = c(domains)
        return user + '@' + domain

    @classmethod
    def all(cls, project="sullivan"):
        if project == "hauwei":
            return {
                "CPF": cls.generate_cpf(),
                "CEP": 80510030,
                "n": 6002,
                "RG": cls.generate_rg(),
                "Nome": cls.generate_name(project),
                "E-mail": cls.generate_email(),
                "Número": cls.generate_number()
            }
        if project == "zhone":
            return {
                "CPF": cls.generate_cpf(),
                "CEP": 80020270,
                "n": 6003,
                "RG": cls.generate_rg(),
                "Nome": cls.generate_name(project),
                "E-mail": cls.generate_email(),
                "Número": cls.generate_number()
            }
        else:
            return {
                "CPF": cls.generate_cpf(),
                "RG": cls.generate_rg(),
                "Nome": cls.generate_name(project),
                "E-mail": cls.generate_email(),
                "Número": cls.generate_number()
            }

    @staticmethod
    def pro_rata(value: float, init: tuple[int], vcto: int, agg: int = 0):
        ASSESSMENT_PERIOD = {i: ((i+15) % 30, (i+14) % 30)
                             for i in [1, 5, 10, 15, 20, 25]}

        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        di, mi, yi = init
        v = ASSESSMENT_PERIOD[vcto]
        if v[0] >= di:
            if v[1] > di:
                m = ((v[0], mi-1, yi), (v[1], mi, yi))
            else:
                m = ((v[0], mi, yi), (v[1]-1, mi+1, yi))
        else:
            m = ((v[0], mi, yi), (v[1], mi+1, yi))

        ms = {i: 31 if i in [1, 3, 5, 7, 8, 10, 12] else 30 if i in [
            4, 6, 9, 11] else 29 if i == 2 and is_leap_year(m[0][2]) else 28 for i in range(1, 13)}

        d = date(m[1][2], m[1][1], m[1][0])-date(yi, mi, di)
        vs = value/ms[mi]
        vr = vs*(d.days+1)
        vr = round(vr, 2) + (value*agg)
        mai = (m[0][0], m[0][1], m[0][2])
        if int(m[1][1])+int(agg) <= 12:
            maf = (m[1][0], int(m[1][1])+int(agg), m[1][2])
        else:
            t = int((int(m[1][1])+agg)/12)
            md = ((int(m[1][1])+agg) % 12)
            maf = (m[1][0], md, int(m[1][2])+t)
        if agg == 0:
            return f"""
    Valor do plano R${value}
    Data de ativação: {'/'.join(map(str, init))}
    Período de apuração: {'/'.join(map(str, mai))} até {'/'.join(map(str, maf))}
    Dias totais: {d.days+1}
    Valor total do Pro Rata: {round(vr,2)}"""
        else:
            dt = date(maf[2], maf[1], maf[0])-date(mai[2], mai[1], mai[0])
            return f"""
    Valor do plano R${value}
    Data de ativação: {'/'.join(map(str, init))}
    Período de apuração: {'/'.join(map(str, mai))} até {'/'.join(map(str, maf))}
    Dias totais: {dt.days+1}
    Dias de Pro Rata: {d.days}
    Valor total da fatura: {round(vr,2)}
    Valor total do Pro Rata: {round(vs*(d.days+1), 2)}"""

    @staticmethod
    def mmc_days(n1: int, n2: int, m: int, y: int = 2023, showCalc: bool = True):
        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        ms = {i: 31 if i in [1, 3, 5, 7, 8, 10, 12] else 30 if i in [
            4, 6, 9, 11] else 29 if i == 2 and is_leap_year(y) else 28 for i in range(1, 13)}
        t = 1
        s = False
        days = [i+1 for i in range(0, ms[m])]
        for day in days:
            a = n1/day
            for d in days:
                b = n2/d
                print(
                    f"times:{t}\n{n1} / {day} = {round(a,2)}\n{n2} / {d} = {round(b,2)}\n")if showCalc else ...
                t += 1
                if b == a:
                    s = [f"{n1} / {day} = {round(a,2)} || {n2} / {d} = {round(b,2)}"] if not s else s.append(
                        f"{n1} / {day} = {round(a,2)} || {n2} / {d} = {round(b,2)}")
        return s


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        try:
            set_appearance_mode("dark")
            self.title('')
            self.geometry('800x510')
            self.resizable(width=True, height=True)
            self.active_elements = list()

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

            self.body = CTkFrame(
                master=self,
                width=600,
                height=450,
                fg_color="#4c4f56",
                corner_radius=0,
            )
            self.body.pack(fill="both", expand="True")

            self.title = CTkLabel(
                master=self.aside,
                text="BingLing",
                width=200,
                height=50,
                font=CTkFont(size=30, weight="bold"),
                text_color="white",
                fg_color="#292929",
                corner_radius=0
            )
            self.title.pack(side="top")

            for _, (string, function) in enumerate({
                "Gerar infos": self.generate_infos,
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
            print(f"Erro na hora de inciar os elementos básicos do App {e}")

    def generate_infos(self) -> None:
        def header_label():
            self.active_elements.append(
                CTkLabel(
                    master=self.header,
                    font=CTkFont(family="Arial", size=25),
                    text="Gerar infos para testes",
                    height=50,
                    width=50,
                    bg_color="#2E4053",
                )
            )
            self.active_elements[-1].pack()

        def generate_btn(master):
            self.active_elements.append(
                CTkButton(
                    master=master,
                    font=CTkFont(family="Arial", size=15),
                    text='Gerar',
                    bg_color="#4c4f56",
                    command=btn_command
                )
            )

        def btn_command():
            self.reload()
            header_label()
            self.active_elements.append(
                CTkFrame(
                    master=self.body,
                    bg_color="#4c4f56",
                    fg_color="#4c4f56",
                    corner_radius=0
                )
            )
            self.active_elements[-1].pack(pady=90)

            for i, (k, v) in enumerate(Generate.all().items()):
                entry_var = StringVar()
                entry_var.set(v)
                self.active_elements.append(
                    CTkLabel(
                        master=self.active_elements[1],
                        font=CTkFont(family="Arial", size=15),
                        text=k,
                        height=40,
                        width=70,
                        bg_color="#4c4f56",
                    )
                )
                self.active_elements[-1].grid(row=i,
                                              column=0, pady=5)

                self.active_elements.append(
                    CTkEntry(
                        master=self.active_elements[1],
                        textvariable=entry_var,
                        bg_color="#4c4f56",
                        width=350,
                        height=40
                    )
                )
                self.active_elements[-1].grid(row=i,
                                              column=1, pady=5)

            generate_btn(master=self.active_elements[1])
            self.active_elements[-1].grid(row=len(self.active_elements),
                                          column=0, columnspan=2)

        try:
            self.reload()
            btn_command()

        except Exception as e:
            print(f"Erro na geração de infos {e}")

    def reload(self) -> None:
        system('cls')
        try:
            list(i.destroy() for i in self.active_elements)
        except Exception as e:
            print(
                f"Erro na hora de recarregar elementos ou elementos carregados de forma errada {e}")
        finally:
            self.active_elements.clear()


if __name__ == '__main__':
    system('cls')
    app = App()
    app.mainloop()
