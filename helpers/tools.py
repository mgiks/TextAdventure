import time


class TextTyper:
    @staticmethod
    def type_text(text, speed):
        match speed:
            case 2:
                delay = 0.035
            case 3:
                delay = 0.02
            case _:
                delay = 0.05

        for char in text:
            print(char, end="", flush=True)

            # Makes typing effect slightly more 'intuitive'
            if char == " ":
                continue

            time.sleep(delay)

        print("\n")


class Action:
    @staticmethod
    def complete_action():
        text = "Success!"
        TextTyper.type_text(text, 2)

    @staticmethod
    def fail_action():
        text = "You can't do that!"
        TextTyper.type_text(text, 2)
