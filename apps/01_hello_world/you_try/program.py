#!/usr/bin/env python3

import os


def main():
    print('-------------------------------------')
    print('               HELLO APP             ')
    print('-------------------------------------')
    print()

    user_text = input('What do you want me to say buddy?')

    system_statement = 'say "{}"'.format(user_text)

    print(user_text)

    os.system(system_statement)


if __name__ == '__main__':
    main()

