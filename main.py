import cv2
import  pandas as pd
from PIL import Image, ImageFont, ImageDraw



img_src = "assets/base.png"

names_src = "assets/names.xlsx"

output_dir = "output"



def MakeCertificate(img_src,name):

    filename = name
    names = name.split(' ')
    firsthalf = name
    secondhalf = ""
    n = len (name)
    print (n)
    starting_point = [570- (3 * n), 340]
    print (len(names))
    if len(names) > 4 or n >22:
        firsthalf = ""
        secondhalf = ""
        starting_point = [540,320]
        if len(names ) <4:
            starting_point[0]+= ((4-len(names)) *53 )

        for i, name in enumerate(names):
            if i < int(len(names)/2):
                print(name)
                firsthalf+= name
                firsthalf+=" "
            else:
                secondhalf+=name
                secondhalf+=" "





    my_image = Image.open(img_src)

    title_font = ImageFont.truetype("assets/alfont_com_AlFont_com_arialbd.ttf", 100 -  min ((n*2), 42))
    name = firsthalf
    title_text = name

    image_editable = ImageDraw.Draw(my_image)

    image_editable.text(starting_point, title_text, (180, 149, 95), font=title_font)

    image_editable.text([starting_point[0],starting_point[1] +50], secondhalf, (180, 149, 95), font=title_font)
    my_image.save("output/"+filename+".png")

def GET_names(path):


    df = pd.read_excel(path)

    result = ''.join([i for i in df['attend'][1:]+"&" if not i.isdigit()])
    names = result.split('&')
    return names



names_list =GET_names(names_src)






for name in names_list[:-1]:
    print(name)
    MakeCertificate(img_src,name)


