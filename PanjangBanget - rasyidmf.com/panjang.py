from PIL import Image
import json

im = Image.open('panjangbet.png')
rgb_im = im.convert('RGB')

#print(rgb_im) #monitoring outputnya rgb_im

sizex =350 # size didapat dari akar 122500
sizey =350
im_new = Image.new("RGB",(sizex,sizey)) #buat image baru dengan palete color RGB ukuran sizex x sizey
map = im_new.load()

for y in range(sizey):
    for x in range(sizex):
        r, g, b = im.getpixel((x*sizex+y,0))
        #print(r,g,b) #monitoring Extract Pixel Value dari RGB
        map[x,y] = (r,g,b) #menambahkan nilai dari R,G,B secara berulang ke dalam variabel 'map' pada tiap blok pikselnya. 
        #print(x,y) #monitorin x,y yang merupakan dimensi pikxel
im_new.save('asulagh2.png')    
#f3=open("map.txt", "a+")
#f3.write(json.dumps(r,g,b))
#SOLVED YEAYYY