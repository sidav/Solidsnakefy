from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import math

def set_fonth_and_fontw_by_textbox_size(text, w, h):
    global FONTW, FONTH
    totalsq = w*h * 7 / 10
    # currh = h
    # currw = w
    # while totalsq / (currh*currw) < len(text):
    #     currh -= 1
    #     currw = currh * 15 / 30
    # FONTH = int(currh)
    # FONTW = int(currw)

    textlen = len(text)
    fontarea = totalsq/textlen
    currh = math.sqrt(30*fontarea/15)
    FONTH = int(currh)
    FONTW = int(currh * 15 // 30)

    print("This is Snake. Font w/h are %f, %.f. Over." % (FONTW, FONTH))

def split_text_in_rect(text, pixelswidth):
    words = text.split()
    curr_line = 0
    curr_line_length = 0
    result = []
    curr_str = ""
    w = pixelswidth // FONTW
    # print(w, pixelswidth)
    for word in words:
        # print(len(word))
        if curr_line_length + len(word) >= w:
            result.append(curr_str)
            curr_str = ""
            curr_line += 1
            curr_line_length = 0
        curr_line_length += len(word) + 1
        curr_str += word + " "
    result.append(curr_str)
    for i in range(len(result)):
        if result[i][-1] == " ":
            result[i] = result[i][:-1]
    return result


def do():
    global FONTW, FONTH
    if len(sys.argv) == 1:
        print("This is Snake. Specify the text. Over.")
        return
    text = sys.argv[1]
    if len(sys.argv) >= 3:
        if text[-1] == '.':
            text = text[:-1]
        text = "This is Snake. %s. Over." % text

    print("This is Snake. Understood. Proceeding to write \"%s\". Over." % text)
    img = Image.open("snake-codec.png")
    draw = ImageDraw.Draw(img)

    width, height = img.size
    textboxw, textboxh = 85 * width / 100, height * 37 // 100
    set_fonth_and_fontw_by_textbox_size(text, textboxw, textboxh)
    font = ImageFont.truetype("univga-sidav.ttf", FONTH)

    split = split_text_in_rect(text, textboxw)
    print(split)
    if len(split) == 0:
        print("This is Snake. The mission is compromised. Cannot split the text. Over.")
    for i in range(len(split)):
        linew = len(split[i]) * FONTW
        textx = width/2 - linew/2
        print("ZOMG:", width, linew, len(split[i]), FONTW, textx)
        draw.text((textx, height - textboxh + i*FONTH), split[i], (255,255,255),font=font)
    img.save('out.png')


do()
