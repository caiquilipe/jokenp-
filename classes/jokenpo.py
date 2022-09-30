from random import choice


class Jokenpo:
    __stone = {"name": "PEDRA"}
    __paper = {"name": "PAPEL"}
    __scissors = {"name": "TESOURA"}
    __sep = "-=" * 20
    __message = "\nEscolha inválida\n"
    __win = 0
    __tie = 0
    __lose = 0
    __chooses: list

    def __init__(self, stone_value, paper_value, scissors_value, nickname) -> None:
        self.__nickname = nickname
        self.__stone.update({"value": stone_value})
        self.__paper.update({"value": paper_value})
        self.__scissors.update({"value": scissors_value})
        self.__chooses = list(
            (
                self.__stone.get("value"),
                self.__paper.get("value"),
                self.__scissors.get("value"),
            )
        )

    def mount_message_invalid(self):
        return self.__sep + self.__message + self.__sep + f"\n\n{self.menu()}"

    def menu(self):
        return f"""Suas opções:
    [{self.__stone.get('value')}] {self.__stone.get('name')}
    [{self.__paper.get('value')}] {self.__paper.get('name')}
    [{self.__scissors.get('value')}] {self.__scissors.get('name')}
    """

    def points(self, result):
        response = {
            "GANHOU": self.adding_win,
            "EMPATOU": self.adding_tie,
            "PERDEU": self.adding_lose,
        }
        return response[result]()

    def adding_win(self):
        self.__win += 1

    def adding_lose(self):
        self.__lose += 1

    def adding_tie(self):
        self.__tie += 1

    def machine_choice(self):
        return choice(self.__chooses)

    def question(self):
        try:
            value = input("Qual é a sua jogada? ")
            validate = self.conditionals(self.check_input(value))
            validate()
            return value
        except Exception as e:
            print(self.mount_message_invalid())
            return self.question()

    def conditionals_player(self, player_choice):
        response = {
            self.__stone.get("value"): self.conditional_stone,
            self.__paper.get("value"): self.conditional_paper,
            self.__scissors.get("value"): self.conditional_scissors,
        }
        return response[player_choice]

    def conditional_stone(self, pc_choice):
        response = {
            self.__stone.get("value"): "EMPATOU",
            self.__scissors.get("value"): "GANHOU",
            self.__paper.get("value"): "PERDEU",
        }
        return response[pc_choice]

    def conditional_paper(self, pc_choice):
        response = {
            self.__paper.get("value"): "EMPATOU",
            self.__stone.get("value"): "GANHOU",
            self.__scissors.get("value"): "PERDEU",
        }
        return response[pc_choice]

    def conditional_scissors(self, pc_choice):
        response = {
            self.__scissors.get("value"): "EMPATOU",
            self.__paper.get("value"): "GANHOU",
            self.__stone.get("value"): "PERDEU",
        }
        return response[pc_choice]

    def check_input(self, value):
        return value in self.__chooses

    def mount_response(self, text_player, text_pc, result):
        return f"""
        GANHOU: {self.__win}    |   EMPATOU: {self.__tie}   |   PERDEU: {self.__lose}
        {text_player}
        {text_pc}
        {result}!
    """

    def run(self):
        print(self.menu())
        player_choice = self.question()
        pc_choice = self.machine_choice()
        cond = self.conditionals_player(player_choice=player_choice)
        result = cond(pc_choice=pc_choice)
        self.points(result=result)
        print(
            self.mount_response(
                text_player=self.get_text(value=player_choice),
                text_pc=self.get_text_pc(value=pc_choice),
                result=result,
            )
        )

    def conditionals(self, value):
        response = {
            False: self.check_invalid_value,
            True: self.check_valid_value,
            self.__stone.get("value"): self.__stone,
            self.__paper.get("value"): self.__paper,
            self.__scissors.get("value"): self.__scissors,
        }
        return response[value]

    def check_invalid_value(self):
        raise Exception()

    def check_valid_value(self):
        pass

    def get_text_pc(self, value):
        choice = self.conditionals(value)
        return f"Computador: {choice.get('name')}"

    def get_text(self, value):
        choice = self.conditionals(value)
        return f"{self.__nickname}: {choice.get('name')}"
