
import sys
from PIL import Image, ImageDraw, ImageFont
import os




def realign_text(li,maxlen=20,widths=[900,690]):
    c_dict = {(255,255,255):0,(51,255,51):1,(102,178,255):2,(0,128,255):2,(255,51,255):3,(255,128,0):4, (255,0,0):5}
    font_size = 90
    font = ImageFont.truetype(os.path.join(os.getcwd()+'/TextOverlay/assets/'+'Quicksand-Medium.ttf'), font_size)
    w_l = []
    r_l = []
    for l in li:
        r_l.append(c_dict[l[1]])
    seq = []
    mx = 5
    while mx >= 0:
        for i in range(len(r_l)):
            if r_l[i] == mx:
                seq.append(i)
        mx -= 1
    #print(seq)
    li_sorted = []
    for i in seq:
        li_sorted.append(li[i])
    for l in li_sorted:
        bg = Image.new('RGB',(1200,500))
        bg_draw = ImageDraw.Draw(bg)
        bg_draw.text((0,0),l[0],font=font,fill=l[1])
        bound = bg.getbbox()
        width = bound[2]-bound[0]+20
        w_l.append(width)
    #print(w_l)
    place = []
    for i in range(len(w_l)):
        if w_l[i] in range(widths[1],widths[0]+1):
            place.append(1)
        elif w_l[i] < widths[1]:
            place.append(0)
        elif w_l[i] > widths[0]:
            place.append(2)
    #print(place)
    li_new = [[] for i in range(50)]
    j = 0
    li_index = [i for i in range(len(li_sorted))]
    for i in range(len(li_sorted)):
        if i in li_index:
            l = li_sorted[i]
            p = place[i]
            if p == 0:
                li_new[j] = l
                li_index.remove(i)
                j += 1
            elif p == 1:
                if j % 2 == 0:
                    li_new[j] = l
                    #li_new[j+1] = ['',(255,255,255)]
                    li_index.remove(i)
                    j += 1
                else:
                    k = j
                    s = 0
                    while k < len(li_sorted) and s == 0:
                        if k in li_index:
                            l_ = li_sorted[k]
                            p_ = place[k]
                            if p_ == 0:
                                li_new[j] = l_
                                li_index.remove(k)
                                j += 1
                                s = 1
                        k += 1
                    li_new[j] = l
                    li_index.remove(i)
                    j += 1
            elif p == 2:
                if j % 2 == 0:
                    li_new[j] = l
                    li_new[j+1] = ['',(255,255,255)]
                    li_index.remove(i)
                    j += 2
                else:
                    k = j
                    s = 0
                    while k < len(li_sorted) and s == 0:
                        if k in li_index:
                            l_ = li_sorted[k]
                            p_ = place[k]
                            if p_ == 0:
                                li_new[j] = l_
                                li_index.remove(k)
                                j += 1
                                s = 1
                        k += 1
                    li_new[j] = l
                    li_new[j+1] = ['',(255,255,255)]
                    li_index.remove(i)
                    j += 2
            else:pass
    li_f = []
    for l in li_new:
        if len(l) > 0:
            li_f.append(l)
    if len(li_f) > maxlen:
        return li_f[:maxlen]
    else:
        return li_f

def replaceimage(image,bottom):
    dim = image.getbbox()
    core = image.crop(dim)
    y_top = bottom - dim[3] + dim[1]
    x_left = dim[0]
    bg = Image.new('RGBA',image.size)
    bg.paste(core,(x_left,y_top))
    return bg

def add_text_to_img(texts,i1,src='saved/',dest='saved_finalimages/'):
    #print(os.getcwd())
    src_dir = src
    dest_dir = dest
    #dest_dir = ''
    img_name = 'hdimage'
    postfix = '.png'
    idx_beg = i1
    #idx_end = i2
    images = []
    try:
        image = Image.open(os.path.join(src_dir, img_name + str(idx_beg) + postfix))
    except:
        print('directory might be wrong. try "python xxx/TextOverlay/main.py imageindex sourcefolder destfolder.')
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
    #print(os.getcwd())
    fontpath = os.path.join(os.getcwd()+'/TextOverlay/assets/'+'Quicksand-Medium.ttf')
    #print(fontpath,os.getcwd()+'/TextOverlay/assets/'+'Quicksand-Medium.ttf')
    #font = ImageFont.truetype('./TextOverlay/assets/Quicksand-Medium.ttf', font_size)
    font = ImageFont.truetype(fontpath, font_size)
    corner_width = 50
    corner_raius = 200

    idx = idx_beg
    x_canvas = int(x_gap)
    y_canvas = int(height * (1 - y_ratio) + y_gap)

    x_text_gap = 150
    y_text_gap = 130
    y_text_height = 120
    image = Image.open(os.path.join(src_dir, img_name + str(idx) + postfix))
    width, height = image.size
    pic_low = int(height-height * y_ratio)-0
    image = replaceimage(image,pic_low)
    text_pos_y = 0

    image_draw = ImageDraw.Draw(image)
    for j in range(0, len(texts), 1):
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
            if j == 1:
                texts[1] = realign_text(texts[1],10)
                divide = '______________________'
                text_pos_x = x_canvas + x_text_gap
                image_draw.text((text_pos_x, text_pos_y), divide, font=font, fill=(255, 255, 255))
                text_pos_y += y_text_height
            else:
                text_pos_y = y_canvas + y_text_gap
                texts[3] = realign_text(texts[3],20)
            
            for k in range(len(texts[j])):
                text = texts[j][k]
                text_pos_x = x_canvas + (half_canvas if k % 2 else 0) + x_text_gap
                image_draw.text((text_pos_x, text_pos_y), text[0], font=font, fill=text[1])
                if k % 2:
                    text_pos_y += y_text_height

        if j != 0:
            x_canvas += canvas_width + x_gap

    # watermark
    '''if idx == idx_beg:
        font_size = 1000
        watermark_font = ImageFont.truetype('Textoverlay/assets/Quicksand-Light.ttf', font_size)
        image_draw.text((int(width / 2) - font_size * 2, int(height / 2)), "SAMPLE", font=watermark_font, fill=(255, 0, 0))'''

    image.save(os.path.join(dest_dir, img_name + str(idx) + postfix))
    image.close()
    pass


        






'''test_texts = [[[['area', '112896m²'], (255, 255, 255)], [['land', '50.87%'], (255, 255, 255)], [['water', '49.13%'], (255, 255, 255)], [['soil', '23.33%'], (255, 255, 255)]],
                    [['lukewarm_oceannnnnn', (51, 255, 51)], ['swamppppppnnnppp', (0, 128, 255)], ['windswept_savannnnnnna', (255, 51, 255)], ['warm_oceannnnnnnnn', (0, 128, 255)], ['savanna', (51, 255, 51)], ['forest', (255, 255, 255)], ['beach', (255, 255, 255)], ['river', (255, 255, 255)]],
                    [[['Amethyst', '6.05%'], (0, 128, 255)], [['Diamond', '3.97%'], (255, 255, 255)], [['Gold', '7.03%'], (255, 255, 255)], [['Emerald', '0.0%'], (255, 255, 255)], [['Bone', '0.0%'], (255, 255, 255)], [['Copper', '21.33%'], (255, 255, 255)], [['Iron', '22.61%'], (51, 255, 51)], [['Coal', '22.76%'], (255, 255, 255)], [['Lapis', '6.53%'], (255, 255, 255)], [['Redstone', '9.72%'], (255, 255, 255)]],
                    [['ocean_ruin', (51, 255, 51)], ['mineshaft', (255, 255, 255)], ['more metal', (51, 255, 51)], ['more gem', (51, 255, 51)], ['multiclimate', (51, 255, 51)], ['uncommon biomes', (255, 128, 0)], ['corals', (0, 128, 255)]]]
add_text_to_img(test_texts,1,2)'''
