from PIL import Image

def resize_image(size1, size2):

    image = Image.open('#yourimagenamehere')

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('pratham-kun'+ str(size1) +'.jpeg')



size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1 , size2)    


