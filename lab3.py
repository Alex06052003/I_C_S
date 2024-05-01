# Лабораторная работа 3
# Манякало Александр
# Тема: крестики-нолики 3D
# Об игре: https://en.wikipedia.org/wiki/3D_tic-tac-toe
#
# Игра:
# два игрока (Bot1, Bot2) по очереди выставляют на поле X и 0.
# Каждую пару ходов выводятся: номер хода, результат действий ботов (обновляется поле)
# Игра продолжается до 2-х побед одного из ботов
# (Пример: Bot1: 2, Bot2: 0 - выиграл первый бот. Если же Bot1: 1, Bot2: 1 - играется третий, решающий раунд)


import itertools
import random

class TicTacToe3D:
    def __init__(self):
        self.board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
        self.players = ['X', 'O']
        self.player_names = {'X': 'Bot1', 'O': 'Bot2'}
        self.scores = {player: 0 for player in self.players}
        self.rounds_to_play = 3
        self.rounds_played = 0

    def print_board(self):
        for i in range(4):
            print("Layer", i+1)
            for row in self.board[i]:
                print(" | ".join(cell if cell else ' ' for cell in row))
                print("-" * 7)
            print()

    def make_move(self, player, x, y, z):
        if self.board[z][y][x] is None:
            self.board[z][y][x] = player
            if self.check_win(x, y, z, player):
                self.print_board()
                print(f"{self.player_names[player]} wins!")
                self.scores[player] += 1
                return True
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                return True
        else:
            print("Invalid move, try again.")
        return False

    def check_win(self, x, y, z, player):
        directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1), (1, -1, 1)]
        for dx, dy, dz in directions:
            count = 0
            for i in range(-3, 4):
                nx, ny, nz = x + i*dx, y + i*dy, z + i*dz
                if 0 <= nx < 4 and 0 <= ny < 4 and 0 <= nz < 4:
                    if self.board[nz][ny][nx] == player:
                        count += 1
                        if count == 4:
                            return True
                    else:
                        count = 0
        return False

    def check_draw(self):
        return all(self.board[z][y][x] for x, y, z in itertools.product(range(4), range(4), range(4)))

    def random_move(self):
        empty_cells = [(x, y, z) for z in range(4) for y in range(4) for x in range(4) if self.board[z][y][x] is None]
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None

    def play_round(self, round_num):
        move_count = 0
        while move_count < 4*4*4:
            for player in self.players:
                x, y, z = self.random_move()
                if self.make_move(player, x, y, z):
                    return
                if player == 'O':
                    print(f"Move {move_count // 2 + 1}")
                    self.print_board()
                move_count += 1

    def play(self):
        while self.rounds_played < self.rounds_to_play:
            self.board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
            print(f"Round {self.rounds_played + 1}")
            self.play_round(self.rounds_played)
            scores_string = ", ".join([f"{self.player_names[player]}: {score}" for player, score in self.scores.items()])
            print(f"Scores: {scores_string}")
            self.rounds_played += 1
            if self.scores['X'] == 2 or self.scores['O'] == 2:
                print("Game Over!")
                break

def main():
    game = TicTacToe3D()
    game.play()

if __name__ == "__main__":
    main()
