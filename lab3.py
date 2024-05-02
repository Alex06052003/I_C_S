# Лабораторная работа 3
# Тема: 3D крестики-нолики
# Об игре: https://en.wikipedia.org/wiki/3D_tic-tac-toe

import itertools
import random
import copy

class TicTacToe3D:
    def __init__(self):
        self.board = [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]
        self.players = ['X', 'O']
        self.player_names = {'X': 'Bot1', 'O': 'Bot2'}
        self.scores = {player: 0 for player in self.players}
        self.rounds_to_play = 1001
        self.rounds_played = 0
        self.variations = {player: {} for player in self.players}

    def print_board(self):
        for z in range(4):
            print("Layer", z+1)
            for row in self.board[z]:
                print(" | ".join(cell for cell in row))
                print("-" * 13)
            print()

    def make_move(self, player, x, y, z):
        if self.board[z][y][x] == ' ':
            self.board[z][y][x] = player
            self.update_variations(player)
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
        return all(self.board[z][y][x] != ' ' for x, y, z in itertools.product(range(4), range(4), range(4)))

    def random_move(self):
        empty_cells = [(x, y, z) for z in range(4) for y in range(4) for x in range(4) if self.board[z][y][x] == ' ']
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None

    def update_variations(self, player):
        for z in range(4):
            for y in range(4):
                for x in range(4):
                    if self.board[z][y][x] == ' ':
                        variation = copy.deepcopy(self.board)
                        variation[z][y][x] = player
                        self.generate_variations(variation, player)

    def generate_variations(self, variation, player):
        string = self.from_list_to_string(variation)
        if string not in self.variations[player]:
            self.variations[player][string] = {}
        empty_cells = [(x, y, z) for z in range(4) for y in range(4) for x in range(4) if variation[z][y][x] == ' ']
        for x, y, z in empty_cells:
            new_variation = copy.deepcopy(variation)
            new_variation[z][y][x] = player
            new_string = self.from_list_to_string(new_variation)
            self.variations[player][string][new_string] = 1

    def from_list_to_string(self, variation):
        string = ""
        for z in range(4):
            for y in range(4):
                for x in range(4):
                    string += variation[z][y][x]
        return string

    def machine_learning(self, player):
        possibilities = list(self.variations[player].keys())
        for _ in range(1500):
            for possibility in possibilities:
                next_moves = list(self.variations[player][possibility].keys())
                chosen_move = random.choice(next_moves)
                self.variations[player][possibility][chosen_move] += 1

    def play_round(self, round_num):
        move_count = 0
        while move_count < 64:
            for player in self.players:
                x, y, z = self.random_move()
                if self.make_move(player, x, y, z):
                    return
                move_count += 1

    def play(self):
        for _ in range(self.rounds_to_play):
            self.board = [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]
            print(f"Round {self.rounds_played + 1}")
            self.play_round(self.rounds_played)
            scores_string = ", ".join([f"{self.player_names[player]}: {score}" for player, score in self.scores.items()])
            print(f"Scores: {scores_string}")
            self.rounds_played += 1
            if self.scores['X'] == 1000 or self.scores['O'] == 1000:
                print("Game Over!")
                break
        self.machine_learning('X')
        self.machine_learning('O')
        print("Machine learning completed.")

def main():
    game = TicTacToe3D()
    game.play()

if __name__ == "__main__":
    main()
