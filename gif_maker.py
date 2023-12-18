from PIL import Image,ImageShow

file0 = Image.open("/home/hamze/personal/timer/pic/"+str(0)+'.jpg')
pics = []
for i in range(1, 10000):
    path = "/home/hamze/personal/timer/pic/"+str(i)+'.jpg'
    locals()['file'+str(i)] = Image.open(path)
    pics.append(locals()['file'+str(i)])
        
         
file0.save("/home/hamze/personal/out1.gif", save_all=True, append_images=pics,
           optimize=True,
           duration=1000, loop=0)
