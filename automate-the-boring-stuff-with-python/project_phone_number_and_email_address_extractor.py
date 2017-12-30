#! python3
'''
Say you have the boring task of finding every phone number and email address in a long web page or document. If you manually scroll through the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and email addresses, you could simply press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, and then run your program. It could replace the text on the clipboard with just the phone numbers and email addresses it finds.

Whenever you’re tackling a new project, it can be tempting to dive right into writing code. But more often than not, it’s best to take a step back and consider the bigger picture. I recommend first drawing up a high-level plan for what your program needs to do. Don’t think about the actual code yet—you can worry about that later. Right now, stick to broad strokes.

For example, your phone and email address extractor will need to do the following:

- Get the text off the clipboard.
- Find all phone numbers and email addresses in the text.
- Paste them onto the clipboard.
'''

import pyperclip, re

phone_regex = re.compile(r'''(
  (\d{3}|\(\d{3}\))? # Area Code
  (\s|-|\.)?         # separator
  (\d{3})            # first 3 digits
  (\s|-|\.)          # separator
  (\d{4})            # last 4 digits
  (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

email_regex = re.compile(r'''(
  ([a-zA-Z0-9._%+-]+) # username
  @                   # @ symbol
  ([a-zA-Z0-9.-]+)    # domain name
  (\.[a-zA-Z]{2,})    # dot-something
)''', re.VERBOSE)

# TODO: Find Matches in clipboard text
text = str(pyperclip.paste())
phone_matches = []
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_number += ' x' + groups[8]
    phone_matches.append(phone_number)

email_matches = []
for groups in email_regex.findall(text):
    email_matches.append(groups[0])

res = 'Phone Numbers\n--------------\n'
for phone in phone_matches:
    res += phone + '\n'
res += '\n'

res += 'Emails\n-----------\n'
for email in email_matches:
    res += email + '\n'
res += '\n'

print(res)
pyperclip.copy(res)
