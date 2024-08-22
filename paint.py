from re import sub
import sys

if not sys.argv[1]:
    print("enter something genius")
    exit()

if sys.argv[1] == "-c":
    if not sys.argv[2]:
        print("enter some code genius")
        exit()
    code = sys.argv[2]
else:
    with open(sys.argv[1], "r") as f:
        code = sub(r"[^01\+\-><',;.:{}\[\]`~cf]", "", f.read())

def interpret(code):
    # []
    loopStack = []
    for i, item in enumerate(code):
        if item == "[":
            loopStack.append(i)
        elif item == "]":
            loop = loopStack.pop(-1)
            # Im lazy pls fix later