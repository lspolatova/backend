"""
игра в крестики нолики
"""
import random
from PIL import Image, ImageDraw, ImageFont
from colorit import background, init_colorit


class TicTacGame:
    """
    реализация игры в крестики нолики
    """
    list_symbol = ["x", "o"]

    def __init__(self, size):
        self.size = size
        self.field = None
        self.draw = None
        self.font = ImageFont.truetype("Roboto-Bold.ttf", size=int(size / 3))
        self.game = [['0', '1', '2'],
                     ['3', '4', '5'],
                     ['6', '7', '8']]
        init_colorit()

    def _fill_board(self):
        for y_coordinate in range(3):
            for x_coordinate in range(3):
                if self.game[y_coordinate][x_coordinate] == 'x':
                    self._draw_cross(x_coordinate, y_coordinate)
                elif self.game[y_coordinate][x_coordinate] == 'o':
                    self._draw_zero(x_coordinate, y_coordinate)
                else:
                    self._draw_number(x_coordinate, y_coordinate)

    def _draw_board(self):
        self.field = Image.new('RGB', (self.size, self.size), (204, 204, 250))
        self.draw = ImageDraw.Draw(self.field)
        self.draw.line(xy=((self.size / 3, 0), (self.size / 3, self.size),), fill='green')
        self.draw.line(xy=((self.size / 3 * 2, 0), (self.size / 3 * 2, self.size),), fill='green')
        self.draw.line(xy=((0, self.size / 3), (self.size, self.size / 3),), fill='green')
        self.draw.line(xy=((0, self.size / 3 * 2), (self.size, self.size / 3 * 2),), fill='green')
        self._fill_board()

    def show_board(self):
        """
        метод выводит поле игры в консоль
        """
        self._draw_board()
        for y_coordinate in range(self.field.size[1]):
            for x_coordinate in range(self.field.size[0]):
                print(background(" ", self.field.getpixel((x_coordinate, y_coordinate))), end='')
            print()
        print()

    def validate_input(self, move):
        """
        метод проверяет возможен ли ход в игре, предлагаемый пользователем
        """
        class CellNumberError(Exception):
            """
            ошибка:ячейки н существует
            """

        class CellOccupied(Exception):
            """
            ошибка:ячейка занята
            """

        try:
            move = int(move)
            if 0 <= move <= 8:
                if self.game[move // 3][move % 3] != 'x' and self.game[move // 3][move % 3] != 'o':
                    return move
                raise CellOccupied
            raise CellNumberError
        except ValueError:
            print("Неверный тип")
            return False
        except CellNumberError:
            print("Такой ячейки нет")
            return False
        except CellOccupied:
            print("ячейка занята")
            return False

    def _draw_cross(self, x_coordinate, y_coordinate):
        self.draw.line(xy=((x_coordinate * self.size / 3, y_coordinate * self.size / 3),
                           ((x_coordinate + 1) * self.size / 3,
                            (y_coordinate + 1) * self.size / 3),), fill='red')
        self.draw.line(xy=((x_coordinate * self.size / 3, (y_coordinate + 1) * self.size / 3),
                           ((x_coordinate + 1) * self.size / 3,
                            y_coordinate * self.size / 3),), fill='red')

    def _draw_zero(self, x_coordinate, y_coordinate):
        self.draw.ellipse((x_coordinate * self.size / 3, y_coordinate * self.size / 3,
                           (x_coordinate + 1) * self.size / 3,
                           (y_coordinate + 1) * self.size / 3), fill='red', outline=(0, 0, 0))

    def _draw_number(self, x_coordinate, y_coordinate):
        self.draw.text((x_coordinate * self.size / 3, y_coordinate * self.size / 3),
                       self.game[y_coordinate][x_coordinate], (0, 0, 0), font=self.font)

    def insert_into_field(self, symbol, move):
        """
        метод вставляет символ в иговое поле
        """
        self.game[move // 3][move % 3] = symbol
        self.show_board()

    def player_move(self, symbol):
        """
        ход игрока
        """
        move = self.validate_input(input())
        while move is False:
            print("Неверный ввод, попробуйте еще:")
            move = self.validate_input(input())
        self.insert_into_field(symbol, move)
        return move

    def computer_move(self, symbol):
        """
        ход компьютера
        """
        move = int(random.choice(
            [element for line in self.game for element in line
             if element not in ('x', 'o')]))
        self.insert_into_field(symbol, move)
        return move

    def check_winner(self, move):
        """
        проверка: привел ли ход к победе игрока
        """
        if len(set(self.game[move // 3])) == 1:
            return True
        if len({line[move % 3] for line in self.game}) == 1:
            return True
        if move % 3 == move // 3 and len({self.game[i][i] for i in range(3)}) == 1:
            return True
        if move % 3 + move // 3 == 2 and len({self.game[i][2 - i] for i in range(3)}) == 1:
            return True
        return False

    def start_game(self):
        """
        метод запускает игру
        """
        print("Cколько играков?")
        number_player = input()
        while True:
            if number_player == '1':
                list_play = [self.player_move, self.computer_move]
                break
            if number_player == '2':
                list_play = [self.player_move, self.player_move]
                break
            print("Неверный ввод, попробуйте еще:")
            number_player = input()
        self.show_board()
        random.shuffle(list_play)
        for i in range(9):
            print("Ходит игрок " + str(i % 2 + 1) + ":")
            move = list_play[i % 2](self.list_symbol[i % 2])
            if i > 3:
                if self.check_winner(move):
                    print("Выиграл игрок " + str(i % 2 + 1))
                    break
        else:
            print("Ничья")


if __name__ == '__main__':
    k = TicTacGame(30)
    k.start_game()
