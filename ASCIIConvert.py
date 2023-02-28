from PIL import Image
    #ascii characters used for output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image
def resize_image(image, new_width=250):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

#convert pixels to greyscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#convert pixels to string of ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=250):
    #attempt to open image
    path = input("Enter a valid pathname to an image (all lowercase): \n")
    try:
        image = Image.open(path)
    except:
        print(path,"No path can be found for that image.")
        main()

    #convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    #print
    print(ascii_image)
    
    #save
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
main()