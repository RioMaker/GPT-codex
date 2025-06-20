# quick script, not very tidy yet
import os


def main():
    # just read the '1' file for now
    try:
        with open('1') as f:
            data = f.read().strip()
    except FileNotFoundError:
        data = 'no data'

    print('data from file:', data)
    # TODO: add more features later


if __name__ == '__main__':
    main()
