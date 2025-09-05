class Pessoa:
    def __init__(self, nome, idade, signo, paixoes):
        self._nome = nome
        self._idade = idade
        self._signo = signo
        self._paixoes = paixoes

    def apresentacao(self):
        print("🌟 Minha História Estilo 'Todo Mundo Odeia o Jess' 🌟\n")
        print(f"Oi, eu sou {self._nome}, tenho {self._idade} anos e sou do signo de {self._signo}.")
        print(f"Amo: {', '.join(self._paixoes)}.\n")
        print("A vida nem sempre foi fácil, mas foi sempre cheia de histórias que vale a pena contar...\n")


class LinhaDoTempo:
    def __init__(self, periodo, narrativa, momentos):
        self.periodo = periodo
        self.narrativa = narrativa
        self.momentos = momentos

    def mostrar(self):
        print("──────────────────────────────")
        print(f"📖 {self.periodo}: {self.narrativa}")
        for momento in self.momentos:
            print(f"✨ No momento {momento}")


# ======= Linha do Tempo com frases de efeito ajustadas =======
historia = [
    LinhaDoTempo("2001 - 2006",
        "Comecei a descobrir o mundo, tropeçando e aprendendo ao mesmo tempo.",
        ["com 5 anos, caí de bicicleta e grudaram esparadrapo nos meus machucados; fiquei brava e me tranquei no banheiro pra dormir.",
         "com 6 anos, caí do cavalo tentando correr gado com meu pai; levantei e quis continuar, mas meu pai não contou para minha mãe."]),

    LinhaDoTempo("2007 - 2008",
        "Aprendi que ser pequena não significa ser fraca.",
        ["com 7 para 8 anos, taquei uma pedra em um colega que me chamou de baixinha."]),

    LinhaDoTempo("2009 - 2013",
        "Descobri paixões, música, rodeio e meu amor por tecnologia.",
        ["com 11 para 12, entrei para a banda do colégio.",
         "com 12, comecei a gostar muito de rodeio e da vida de campo.",
         "comecei a laçar e a me interessar por tecnologia.",
         "fiz um curso básico de TI.",
         "com uns 14 anos, pensei em ser veterinária, mas não consegui lidar com o sacrifício de um animal; terminei o curso e segui outro caminho."]),

    LinhaDoTempo("2014 - 2016",
        "Comecei a sonhar e a me desafiar mais.",
        ["com 15 anos, ganhei meu primeiro laço prenda.",
         "com 16 anos, comecei no IFF, jogava basquete, me mudei de cidade e precisei me virar sozinha a 500 km de casa."]),

    LinhaDoTempo("2017 - 2019",
        "Entre desafios e conquistas, aprendi a me cuidar e não desistir.",
        ["com 17 anos, meu time passou para a segunda fase do JERGS.",
         "fiquei internada uma semana por não me alimentar direito 😅",
         "com 18 anos, terminando o curso, ficamos em 3º lugar no JEIF."]),

    LinhaDoTempo("2019 - 2021",
        "A vida adulta chegou de repente, trazendo mudanças e oportunidades.",
        ["com 19 anos, entrei em colapso pensando: 'o que vou fazer agora?'",
         "na pandemia, comecei a estudar outras coisas e tive meu primeiro emprego cuidando de um garotinho.",
         "no final de 2020, descobri a AMF pelo Facebook, visitei e me apaixonei. Me matriculei um dia antes do Natal 🎄."]),

    LinhaDoTempo("2021 - 2025",
        "Faculdade, trabalho, aventuras e experiências inesquecíveis.",
        ["em 2021, comecei a faculdade e logo em seguida já estava empregada em um projeto da FAM, aprendendo muito na prática.",
         "em 2022, comecei na EVO e foi só sucesso!",
         "em 2024, nasceu a ideia de viajar; em 2025, realizei meu sonho.",
         "comecei a namorar em 2021, mas terminei antes da viagem; meus amigos me apoiaram e me incentivaram, e foi uma experiência incrível.",
         "comecei meu TCC sobre rodeio, porque sou maluca e amo isso."])
]


# ======= Programa Principal =======
def main():
    jess = Pessoa("Jessika", 24, "Aquário", ["cavalos", "gatinhos", "tecnologia", "música", "família"])
    jess.apresentacao()

    for periodo in historia:
        periodo.mostrar()

    print("\n🌈 Conclusão 🌈")
    print("Hoje me sinto mais renovada e feliz com tudo que vivi.")
    print("Que este final de ano seja incrível e cheio de novas histórias para contar! 💖")


if __name__ == "__main__":
    main()
