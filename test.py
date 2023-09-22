import random

def paste(str, p=True, c=True):
    from subprocess import Popen, PIPE
    bytes = str.encode('utf-8')
    if p:
        p = Popen(['xsel', '-pi'], stdin=PIPE)
        p.communicate(input=bytes)
    if c:
        p = Popen(['xsel', '-bi'], stdin=PIPE)
        p.communicate(input=bytes)

while True:
    label = input("Enter a string: ")
    test = label.replace(" ", "%20")
    # random color in rgb
    color = ("#%06x" % random.randint(0, 0xFFFFFF)).replace("#", "%23")
    url = f"https://img.shields.io/badge/{test}-{color}?style=for-the-badge"
    print(f"![{label}]({url})")
    # copy to clipboard
    paste(f"![{label}]({url})", p=True, c=True)