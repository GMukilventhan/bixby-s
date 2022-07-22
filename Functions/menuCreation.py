

# Function that create msg string centered in the screen
def msg_center(msg, color, color_text):
    width = 100
    msg_len = len(msg)
    if msg_len != 0:
        msg_centered = int((width - msg_len) / 2)
        msg_centered = f"{color}#" * int(msg_centered / 4) + " " * (
                msg_centered - int(msg_centered / 4)) + f"{color_text}" + msg + " " * (
                               msg_centered - int(msg_centered / 4)) + f"{color}#" * int(msg_centered / 4)
        if len(msg_centered) % 2 == 0:
            msg_centered += "#"
        print(msg_centered)
    else:
        print(f"{color}#" * width)


def header(color, color_text, textList):
    msg_center("", color, color_text)
    msg_center("Bienvenue dans l'application de gestion BIXBY", color, color_text)
    msg_center("---------------------------------------------------------------------", color, color)
    msg_center("Created By : SINGH Manveer & GEORGE Mukilventhan & AHOUNOU Jelil", color, color_text)
    msg_center("---------------------------------------------------------------------", color, color)
    msg_center(" ", color, color_text)
    for i in textList:
        msg_center(i, color, color_text)
    msg_center("0) Exit", color, color_text)


def footer(color):
    msg_center(" ", color, color)
    msg_center(" ", color, color)
    msg_center(" ", color, color)
    msg_center("", color, color)