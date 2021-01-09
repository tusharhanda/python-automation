#!python3
# main.py - A multi-clipboard program
import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds good!""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'ttyl': "'""Talk to you later."""}


if len(sys.argv)<2:
    print('Usage: python main.py [keyphrase] - copy phrase text')
    sys.exit()

# first command line arg is the keyphrase
keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + 'copied to clipboard')
else:
    print('There is no text for ' + keyphrase)
