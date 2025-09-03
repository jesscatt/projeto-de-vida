class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome   # encapsulamento
        self._idade = idade

    def viver(self):
        print(f"🌱 {self._nome}, com {self._idade} aninhos, está começando a viver sua jornada...")

    def estudar(self):
        print(f"📚 {self._nome} está aprendendo coisas novas!")

    def trabalhar(self):
        print(f"💼 {self._nome} ainda não trabalha.")

    def hobby(self):
        print(f"🎨 {self._nome} tem seus passatempos preferidos.")


# ======= Fases =======

class Crianca(Pessoa):
    def estudar(self):
        print(f"✏️ {self._nome} está aprendendo a ler e escrever na escola.")

    def hobby(self):
        print(f"🐴 {self._nome} adora brincar e ama cavalos!")

    def trabalhar(self):
        print(f"😴 {self._nome} seu maior trabalho é brincar e sonhar.")


class Adolescente(Pessoa):
    def estudar(self):
        print(f"🏀 {self._nome} estuda no ensino médio e joga basquete.")

    def hobby(self):
        print(f"🎶 {self._nome} gosta de sair com os amigos, olhar series e filmes.")

    def trabalhar(self):
        print(f"🌟 {self._nome} começa a ter responsabilidades e pensar no futuro, em quais escolhar tomar em sua carreira profissional.")


class Adulto(Pessoa):
    def estudar(self):
        print(f"🎓 {self._nome} está iniciando sua faculdade e se dedicando muito a conseguir seu primeiro emprego.")

    def hobby(self):
        print(f"⚡ {self._nome} gosta de esportes, família, amigos e planejar o futuro.")

    def trabalhar(self):
        print(f"💼 {self._nome} já trabalha e busca crescer profissionalmente.")


# ======= Programa Principal =======
def main():
    crianca = Crianca("Jess", 7)
    adolescente = Adolescente("Jess", 15)
    adulto = Adulto("Jess", 21)

    for fase in [crianca, adolescente, adulto]:
        print("──────────────────────────────")
        fase.viver()
        fase.estudar()
        fase.hobby()
        fase.trabalhar()


if __name__ == "__main__":
    main()
