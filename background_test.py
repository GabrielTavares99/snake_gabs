from rembg import remove
from PIL import Image
input_path = 'SIDM23MMSP2302.jpg'
output = 'converted.png'

inp = Image.open(input_path)
outt = remove(inp)
outt.save(output)
