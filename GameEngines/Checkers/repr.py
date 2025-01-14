from colorama import Fore
import numpy as np


def _repr(self):
    board: np.ndarray = self.board

    index = '  ' + ' '.join(f'{i}' for i in range(8))
    line_acc = [index]
    for i in range(8):
        line = board.diagonal(4-i)
        line = line[line != 3]
        val_acc = []
        for v in line:
            if v > 0:
                val_acc.append(f'{Fore.LIGHTBLUE_EX}{int(v)}{Fore.RESET}')
            elif v < 0:
                val_acc.append(f'{Fore.LIGHTYELLOW_EX}{abs(int(v))}{Fore.RESET}')
            elif v == 0:
                val_acc.append(f' ')

        line_acc.append(' \u2588 '.join(val_acc))
        line_acc[-1] = f'{i} ' + (line_acc[-1] + ' \u2588' if i % 2 == 1 else '\u2588 ' + line_acc[-1])

    return '\n'.join(line_acc)
