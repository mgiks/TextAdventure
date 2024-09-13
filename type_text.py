import sys
import time


def type_text(text, speed):
    delay = 0

    match speed:
        case 1:
            delay = 0.05
        case 2:
            delay = 0.035
        case 3:
            delay = 0.02
        case _:
            delay = 0.05

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == " ":
            continue
        time.sleep(delay)

    sys.stdout.write("\n")
