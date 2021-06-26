from PIL import Image, ImageDraw, ImageFont
import textwrap


def generete_text(text):
    temp_text = ''
    for t in text:
        if(t=='E' or t=='e'):
            temp_text += t
            continue
        temp_text += t.lower()

    list_text = temp_text.split()
    result = ""
    for value in list_text:
        temp_result = translate_font(value)
        result += temp_result + " "
        

    return result

def translate_font(tempText):
    newText = ''
    index = 0
    while(index<len(tempText)):
        # Untuk A'
        list = ["q","z","v","x","f"]
        list_consonant_full = ['i','a','u','o','E','e']
        
        if(tempText[index] in list):
            index+=1
            continue
        
        if(len(tempText)-index>2):
            list_special = ['ny','ng','nc','nr','mp']
            temp = tempText[index:index+2]
            if(temp in list_special and tempText[index+2] in list_consonant_full):
                if(tempText[index+2]=='e'):
                    newText += 'e'
                    index+= 1

                if(temp=='ny'):
                    newText += 'N'
                    index += 2
                    continue
                if(temp=='ng'):
                    newText += 'G'
                    index += 2
                    continue
                if(temp=='nc'):
                    newText += 'C'
                    index += 2
                    continue
                if(temp=='nr'):
                    newText += 'R'
                    index += 2
                    continue
                if(temp=='mp'):
                    newText += 'P'
                    index += 2
                    continue
            


        if(len(tempText)-index>2):
            temp = tempText[index:index+3]
            if(temp=='ngg'):
                newText += 'g'
                index += 3
                continue

        if(len(tempText)-index>3):
            temp = tempText[index:index+4]
            if(temp=='ngka'):
                newText += 'K'
                index += 4
                continue

        
        if(index==len(tempText)-2 and  tempText[len(tempText)-2:len(tempText)]=='ng'):
            index+=2
            continue

        if(index==0):
            list_consonant = ['i','u','E','o']
            if(tempText[index] in list_consonant):
                newText += 'a'+tempText[index]
                index += 1
                continue
            if(tempText[index] == 'e'):
                newText += tempText[index]+'a'
                index+=1
                continue
        else :
            
            if(tempText[index] == 'a'):
                index += 1
                continue
            
            if(tempText[index] in list_consonant_full and tempText[index-1] in list_consonant_full):
                if(tempText[index]=='e'):
                    newText += tempText[index]+'a'
                    index+=1
                    continue
                
                newText += 'a'+tempText[index]
                index+=1
                continue
       
        if(index<len(tempText)-2):
            if(tempText[index] not in list_consonant_full and tempText[index+1] not in list_consonant_full):
                index += 1
                continue

            if(tempText[index+1]=='e'):
                newText += 'e'+tempText[index]
                index += 2
                continue

        newText += tempText[index]
        index += 1
    return newText     
    
def draw_text(text):
    width =  500
    height = 1000
    img = Image.new('RGB', (width, height), color = (242, 238, 203))
    fnt = ImageFont.truetype('bugis.ttf', 15)
    d = ImageDraw.Draw(img)

    lines = textwrap.wrap(text, width=35)
    y_text = 30
    for line in lines:
        width, height = fnt.getsize(line)
        d.text((10, y_text), line, font=fnt, fill=(22,38,76))
        y_text += height

    img.save('pil_text.png')


