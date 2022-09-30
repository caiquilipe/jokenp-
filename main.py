from classes.jokenpo import Jokenpo


nickname = input("Digite seu nickname: ")
stone_value = input("Digite o valor de pedra: ")
paper_value = input("Digite o valor de papel: ")
scissors_value = input("Digite o valor de tosoura: ")
jokenpo = Jokenpo(
    nickname=nickname,
    stone_value=stone_value,
    paper_value=paper_value,
    scissors_value=scissors_value,
)

while True:
    jokenpo.run()
