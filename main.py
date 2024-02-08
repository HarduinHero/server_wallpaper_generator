from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json
import const

def gen_wallpaper(data:dict) :
    # Open an Image
    # Call draw Method to add 2D graphics in an image
    # Custom font style and font size
    # Add Text to an image
    img = Image.open(f'{const.BACKGROUND_FOLDER}/{data[const.BACKGROUND_KEY]}')
    I1 = ImageDraw.Draw(img)
    filename = 'wallpaper'
    y_origin_increment = 0
    for field in data :
        if field == const.BACKGROUND_KEY :
            continue
        
        if field[0] != "_" :
            text = f'{field} : {data[field][const.TEXT_KEY]}'
        else :
            text = f'{data[field][const.TEXT_KEY]}'
            

        origin = (const.TEXT_ORIGIN[0], const.TEXT_ORIGIN[1]+y_origin_increment)
        color = tuple(data[field].get(const.COLOR_KEY, const.DEFAULT_COLOR))
        size = data[field].get(const.SIZE_KEY, const.DEFAULT_FONT_SIZE)
        filename += '-' + data[field][const.TEXT_KEY]
        
        font = ImageFont.truetype(const.FONT_FILE, size)
        I1.text(origin, text, font=font, fill=tuple(color))
        y_origin_increment += size

    return img, filename

if __name__ == '__main__' :

    with open(const.DATA_FILE_PATH, 'r') as json_file :
        json_data = json.load(json_file)

    for wall_paper_data in json_data :
        a, filename = gen_wallpaper(wall_paper_data)
        a.save(f'{const.OUTPUT_FOLDER}/{filename}.png')

