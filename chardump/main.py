from sys import argv


LINE_NUMBER_LEN = 8
LINE_LEN = 16

ASCII_TABLE = [
    'NUL', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL',
    'BS ', 'HT ', 'NL ', 'VT ', 'NP ', 'CR ', 'SO ', 'SI ',
    'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB',
    'CAN', 'EM ', 'SUB', 'ESC', 'FS ', 'GS ', 'RS ', 'US ',
    'SP ', ' ! ', ' " ', ' # ', ' $ ', ' % ', ' & ', ' \' ',
    ' ( ', ' ) ', ' * ', ' + ', ' , ', ' - ', ' . ', ' / ',
    ' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ',
    ' 8 ', ' 9 ', ' : ', ' ; ', ' < ', ' = ', ' > ', ' ? ',
    ' @ ', ' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ',
    ' H ', ' I ', ' J ', ' K ', ' L ', ' M ', ' N ', ' O ',
    ' P ', ' Q ', ' R ', ' S ', ' T ', ' U ', ' V ', ' W ',
    ' X ', ' Y ', ' Z ', ' [ ', ' \ ', ' ] ', ' ^ ', ' _ ',
    ' ` ', ' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ',
    ' h ', ' i ', ' j ', ' k ', ' l ', ' m ', ' n ', ' o ',
    ' p ', ' q ', ' r ', ' s ', ' t ', ' u ', ' v ', ' w ',
    ' x ', ' y ', ' z ', ' { ', ' | ', ' } ', ' ~ ', 'DEL'
]


def main():
    if len(argv) < 2:
        print('usage: python3 {} filepath'.format(__file__))
        exit(1)

    filepath = argv[1]

    line_number = lambda i: '{:x}'.format(i).zfill(LINE_NUMBER_LEN) + '  '
    with open(filepath, mode='rb') as f:
        ctx = f.read()
        array = list(map(lambda b: ASCII_TABLE[int(b)], ctx))

        for i in range(0, len(array), LINE_LEN):
            line = line_number(i)
            line += ' '.join(array[i:i+LINE_LEN])
            print(line)

        print(line_number(len(array)))


if __name__ == '__main__':
    main()
