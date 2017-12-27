#!/usr/bin/python3

passwords = {
    'email': 'abcdef'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Error')
    sys.exit()
account = sys.argv[1];

if account in passwords:
    pyperclip.copy(passwords[account])
    print('copied')
else:
    print(account , ' is not valid')
