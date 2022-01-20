import sys
from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_img(texts,index):
    #print(os.getcwd())
    src_dir = 'saved/'
    dest_dir = 'saved_finalimages/'
    img_name = 'hdimage'
    postfix = '.png'
    idx_beg = index
    idx_end = index+1
    images = []
    image = Image.open(src_dir + img_name + str(idx_beg) + postfix)
    width, height = image.size

    # resize canvas
    nof_canvas = len(texts) - 1
    x_gap = 200  # x gap between canvas
    canvas_width = int((width - x_gap) / nof_canvas - x_gap)
    half_canvas = int(canvas_width / 2)

    y_ratio = 0.3  # y percentage of the table area
    y_gap = 200  # y gap between canvas
    canvas_height = int(height * y_ratio - y_gap * 2)

    color = (255, 255, 255)
    font_size = 90
    font = ImageFont.truetype('./Textoverlay/assets/Quicksand-Medium.ttf', font_size)

    corner_width = 50
    corner_raius = 200

    for idx in range(idx_beg, idx_end, 1):
        x_canvas = int(x_gap)
        y_canvas = int(height * (1 - y_ratio) + y_gap)

        x_text_gap = 150
        y_text_gap = 130
        y_text_height = 120
        image = Image.open(src_dir + img_name + str(idx) + postfix)
        text_pos_y = 0
        for j in range(0, len(texts), 1):
            image_draw = ImageDraw.Draw(image)
            if j != 1:
                image_draw.rounded_rectangle((x_canvas, y_canvas, x_canvas + canvas_width, y_canvas + canvas_height),
                                             fill="black", outline="grey", width=corner_width, radius=corner_raius)

            if j == 0 or j == 2:
                text_pos_y = y_canvas + y_text_gap
                for text in texts[j]:
                    text_pos_x = x_canvas + x_text_gap
                    image_draw.text((text_pos_x, text_pos_y), text[0][0], font=font, fill=text[1])
                    text_pos_y += y_text_height
                text_pos_y = y_canvas + y_text_gap
                for text in texts[j]:
                    text_pos_x = x_canvas + half_canvas + x_text_gap
                    image_draw.text((text_pos_x, text_pos_y), text[0][1], font=font, fill=text[1])
                    text_pos_y += y_text_height
            else:
                if j != 1:
                    text_pos_y = y_canvas + y_text_gap
                for k in range(len(texts[j])):
                    text = texts[j][k]
                    text_pos_x = x_canvas + (half_canvas if k % 2 else 0) + x_text_gap
                    image_draw.text((text_pos_x, text_pos_y), text[0], font=font, fill=text[1])
                    if k % 2:
                        text_pos_y += y_text_height

            if j != 0:
                x_canvas += canvas_width + x_gap
        image.save(dest_dir + img_name + str(idx) + postfix)
        image.close()
