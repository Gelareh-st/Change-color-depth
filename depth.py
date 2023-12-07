from PIL import Image

# Open the image file
image= Image.open(input('Enter image path : '))
# convert iamge to greyscale
image = image.convert('L')
# Get the width and height of the image
width, height = image.size
# Get the depth
n= int(input('Enter depth : '))

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the current pixel's color
        current_color = image.getpixel((x, y))
        color=0
        min=0
        # Loop throught colors in defined depth
        for i in range (2**n):
            max=int(min+(256/(2**n)))
            # Find color range
            if current_color>=min and current_color<=max :
                new_color= int(color) 
            min=max    
            color=int(color+(256/((2**n)-1)))
        # Set the new color for the pixel
        image.putpixel((x, y), new_color)

# Show the modified image
image.show()