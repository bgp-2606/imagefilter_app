"""
    L5_10_image_filters.py
    
    ECOR 1051 Fall 2019
    Milestone 2
    
    Group L5-10
        Bren Gelyn Padlan, 101148482
        Claire Baggesen, 101149755
        Stacey Nip, 101151872
        Ajiile Moodie, 101147889
    
    Submitted on November 24, 2019
    
"""
from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, get_height, get_width

#-----------------------------------------------------------------
def two_tone(original_image: Image, color1: str, color2: str) -> Image:
    """ Author: Bren-Gelyn Padlan
    Returns a copy of the original_image with two_tone filter.
    Precondition: The colour names that can only be recognized by the function are:
            "black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", and "gray"
    
    >>> original_image = load_image(choose_file())
    >>> two_tone (original_image, color1, color2)
    """
    valid_colors = [("black",(0,0,0)), ("white",(255,255,255)), ("red",(255,0,0)), ("lime",(0,255,0)), \
                    ("blue",(0,0,255)), ("yellow",(255,255,0)), ("cyan",(0,255,255)), ("magenta",(255,0,255)), \
                    ("gray",(128,128,128))]
    
    for color in valid_colors:
        if color1.lower() == color[0]:
            tone1 = create_color(color[1][0], color[1][1], color[1][2])
        if color2.lower() == color[0]:
            tone2 = create_color(color[1][0], color[1][1], color[1][2])

    (r1, g1, b1) = tone1
    (r2, g2, b2) = tone2    

    two_tone_image = copy(original_image)
    for x, y, (r, g, b) in two_tone_image:
        brightness = (r + g + b) // 3 
        
        if (0 <= brightness <= 127):
            two_tone_color = create_color(r1, g1, b1)
            set_color(two_tone_image, x, y, two_tone_color)
        elif (128 <= brightness <= 255):
            two_tone_color = create_color(r2, g2, b2)
            set_color(two_tone_image, x, y, two_tone_color)
    return two_tone_image


def three_tone(original_image: Image, color1: str, color2: str, color3: str) -> Image:
    """ Author: Bren-Gelyn Padlan
    Returns a copy of the original_image with three_tone filter.
    Precondition: The colour names that can only be recognized by the function are:
            "black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", and "gray"
    
    >>> original_image = load_image(choose_file())
    >>> three_tone (original_image, color1, color2, color3)
    """
    valid_colors = [("black",(0,0,0)), ("white",(255,255,255)), ("red",(255,0,0)), ("lime",(0,255,0)), \
                    ("blue",(0,0,255)), ("yellow",(255,255,0)), ("cyan",(0,255,255)), ("magenta",(255,0,255)), \
                    ("gray",(128,128,128))]
    
    for color in valid_colors:
        if color1.lower() == color[0]:
            tone1 = create_color(color[1][0], color[1][1], color[1][2])
        if color2.lower() == color[0]:
            tone2 = create_color(color[1][0], color[1][1], color[1][2])
        if color3.lower() == color[0]:
            tone3 = create_color(color[1][0], color[1][1], color[1][2])
    
    (r1, g1, b1) = tone1
    (r2, g2, b2) = tone2
    (r3, g3, b3) = tone3
    
    three_tone_image = copy(original_image)
    for x, y, (r, g, b) in three_tone_image:
        brightness = (r + g + b) // 3 
        
        if (0 <= brightness <= 84):
            three_tone_color = create_color(r1, g1, b1)
            set_color(three_tone_image, x, y, three_tone_color)
        elif (85 <= brightness <= 170):
            three_tone_color = create_color(r2, g2, b2)
            set_color(three_tone_image, x, y, three_tone_color)
        elif (171 <= brightness <= 255):
            three_tone_color = create_color(r3, g3, b3)
            set_color(three_tone_image, x, y, three_tone_color)        
    return three_tone_image


def extreme_contrast (image: Image) -> Image:
    """ Author: Claire Baggesen
    Returns a copy of the original image, in which the contrast between the pixels has been maximized.
    
    >>> image = load_image(choose_file())
    >>> new_contrast = extreme_contrast(image)
    >>> show(new_contrast)
    """  
    new_image = copy(image)
    
    max_red = create_color(255, 0, 0)
    max_red_green = create_color(255, 255, 0)
    max_red_blue = create_color(255, 0, 255)    
    max_green = create_color(0, 255, 0)
    max_green_blue = create_color(0, 255, 255)
    max_blue = create_color(0, 0, 255)
    max_white = create_color(255, 255, 255)
    max_black = create_color(0, 0, 0)    
    
    for x, y, (r, g, b) in new_image: 
        color1, color2, color3 = r, g, b
        
        if 0 <= color1 <= 127 and 0 <= color2 <= 127 and 0 <= color3 <= 127:
            set_color (new_image, x, y, max_black)
        elif 128 <= color1 <= 255 and 128 <= color2 <= 255 and 128 <= color3 <= 255:
            set_color (new_image, x, y, max_white)
        elif 0 <= color1 <= 127 and 0 <= color2 <= 127 and 128 <= color3 <= 255:
            set_color (new_image, x, y, max_blue) 
        elif 0 <= color1 <= 127 and 128 <= color2 <= 255 and 128 <= color3 <= 255:
            set_color (new_image, x, y, max_green_blue)
        elif 0 <= color1 <= 127 and 128 <= color2<= 255 and 0 <= color3 <= 127:
            set_color (new_image, x, y, max_green)        
        elif 128 <= color1 <= 255 and 0 <= color2 <= 127 and 128 <= color3 <= 255:
            set_color (new_image, x, y, max_red_blue)        
        elif 128 <= color1 <= 255 and 128 <= color2 <= 255 and 0 <= color3 <= 127:
            set_color (new_image, x, y, max_red_green)   
        elif 128 <= color1 <= 255 and 0 <= color2 <= 127 and 0 <= color3 <= 127:
            set_color (new_image, x, y, max_red) 
    return new_image


def grayscale(image: Image) -> Image:
    """
    This function code was provided.
    Returns a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image


def sepia(image: Image) -> Image:
    """ Author: Ajiile Moodie
    Returns a copy of the original image with a sepia filter overlayed
    
    >>> image = load_image(choose_file())
    >>> sepia(image)
    """
    new_image = copy(image)
    sepia_image = (grayscale(new_image))
    
    for x, y, (r, g, b) in sepia_image:
        if g < 63:
            sepia = create_color(r * 1.10, g, b * 0.90) 
            if r * 1.10 > 255:
                sepia = create_color(255, g, b * 0.90)
            elif r * 1.10 > 255 and b * 0.90 > 255:
                sepia = create_color(255, g, 255)
            elif b * 0.90 > 255:
                sepia = create_color(r * 1.10, g, 255)    
            set_color(sepia_image, x, y, sepia) 
        
        if 63 <= g <= 191:
            sepia = create_color(r * 1.15, g, b * 0.85)
            if r * 1.15 > 255:
                sepia = create_color(255, g, b * 0.85)
            elif r * 1.15 > 255 and b * 0.85 > 255:
                sepia = create_color(255, g, 255)
            elif b * 0.85 > 255:
                sepia = create_color(r * 1.15, g, 255)
            set_color(sepia_image, x, y, sepia)  
        
        if g > 191:
            sepia = create_color(r * 1.08, g, b * 0.93)
            if r * 1.08 > 255:
                sepia = create_color(255, g, b * 0.93)
            elif r * 1.08 > 255 and b * 0.93 > 255:
                sepia = create_color(255, g, 255)
            elif b * 0.93 > 255:
                sepia = create_color(r * 1.08, g, 255)            
            set_color(sepia_image, x, y, sepia) 
    return sepia_image


def _adjust_component(comp: int) -> int:
    """ Author: Stacey Nip
    Return the midpoint of the quadrant in which a given component lies. 
    Precondition: 0 <= comp <= 255
    
    >>> _adjust_component(128)
    159
    >>> _adjust_component(0)
    31
    >>> _adjust_component(255)
    223
    """
    comp = int(comp)

    quad1_min, quad1_max = (0, 63)
    quad2_min, quad2_max = (64, 127)
    quad3_min, quad3_max = (128, 191)
    if quad1_min <= comp <= quad1_max:
        return 31
    elif quad2_min <= comp <= quad2_max:
        return 95
    elif quad3_min <= comp <= quad3_max:
        return 159
    else:
        return 223
    
        
def posterize(image: Image) -> Image:
    """ Author: Stacey Nip
    Return a posterized copy of an image.
    
    >>> image = load_image(choose_file())
    >>> posterize_image = posterize(image)
    >>> show(posterize_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        red = _adjust_component(r)
        green = _adjust_component(g)
        blue = _adjust_component(b)
        
        new_color = create_color(red, green, blue)
        set_color(new_image, x, y, new_color)
    return new_image


def detect_edges(image: Image, threshold: int) -> Image:
    """ Author: Claire Baggesen
    Takes a copy of an original image and returns the image in black and white using edge detection. \
    The function checks the contrast between two pixels.  The contrast is checked for every pixel and the pixel below it.  \
    If the contrast between the two pixels is high, change the top pixel's color to black and if the contrast is low, \
    change the top pixel's color to white.  
    
    >>> image = load_image(choose_file())
    >>> edges_detect = detect_edges(image, 12)
    >>> show(edges_detect)
    """
    new_image = copy(image)
    
    height = get_height(new_image)
    width = get_width(new_image)    
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for y in range(0, get_height(new_image) -1):
        for x in range(0, get_width(new_image)):
            r, g, b = get_color(new_image, x, y)
            red_two, green_two, blue_two = get_color(new_image, x, y + 1)
            if abs (( r + g + b) // 3 - (red_two + green_two + blue_two) // 3) > threshold:
                set_color(new_image, x, y, black)
            if abs (( r + g + b) // 3 - (red_two + green_two + blue_two) // 3) < threshold:
                set_color(new_image, x, y, white)
    return new_image


def detect_edges_better(image: Image, threshold: int) -> Image:
    """ Author: Claire Baggesen
        Modified by: Bren-Gelyn Padlan
    Takes a copy of an original image and returns the image in black and white using a better edge detection filter. 
    The contrast is checked for every pixel, the pixel below it and the pixel to the right of it.
    Precondition: threshold > 0
    
    >>> photo = load_image(choose_file())
    >>> detect_edges_better(photo, 12)
    """                       
    new_image = copy(image)
    
    height = get_height(new_image)
    width = get_width(new_image)    
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # The proceeding code below has been modified
    for y in range(0, get_height(new_image) -1):
        for x in range(0, get_width(new_image) -1): # Modified code: Omits the last column of pixel to the right by adding -1 to the range.
            r, g, b = get_color(new_image, x, y)
            
            red_below, green_below, blue_below = get_color(new_image, x, y + 1)
            
            # Added code: Gets the color component of the pixel to the right.
            red_right, green_right, blue_right = get_color(new_image, x + 1, y) 
            
            abs_val_below = abs (( r + g + b) // 3 - (red_below + green_below + blue_below) // 3) # Modified code: The code was changed as a local variable
            
            #Added code: Evaluates the absolute difference of the pixel and the pixel to its right.
            abs_val_right = abs (( r + g + b) // 3 - (red_right + green_right + blue_right) // 3) 
            
            if (abs_val_below > threshold) or (abs_val_right > threshold): #Modified code: The values for conditions were changed into variable names.
                set_color(new_image, x, y, black)
            if (abs_val_below < threshold) or (abs_val_right < threshold): #Modified code: The values for conditions were changed into variable names.
                set_color(new_image, x, y, white)
    return new_image


def flip_vertical(image: Image) -> Image:
    """ Author: Ajiile Moodie
    Returns an image that is the original image, flipped vertically.
    
    >>> image = load_image('riveter.jpg')
    >>> vertical_image = flip_vertical(image)
    >>> show(vertical_image)
    """
    new_image = copy(image)
    height = get_height(new_image)
    width = get_width(new_image)
    
    for y in range(0, height):
        for x in range(0, width//2):
            right_pixel = get_color(new_image, x, y)
            left_pixel = get_color(new_image, width - x - 1, y)
            set_color(new_image, x, y, left_pixel)
            set_color(new_image, width - x - 1, y, right_pixel)
    return new_image


def flip_horizontal(image: Image) -> Image:
    """ Author: Stacey Nip
    Return a horizontally flipped copy of the original image where the colour of the top-left pixel is switched with the bottom-left pixel.
    
    >>> image = load_image(choose_file())
    >>> horizontal_image = flip_horizontal(image)
    >>> show(horizontal_image)
    """
    new_image = copy(image)
    
    width = get_width(new_image)
    height = get_height(new_image)
    
    for y in range(0, height//2): 
        for x in range(0, width): 
            top_pixel = get_color(new_image, x, y) 
            bottom_pixel = get_color(new_image, x, height - y - 1)
            
            set_color(new_image, x, y, bottom_pixel)
            set_color(new_image, x, height - y - 1, top_pixel)
    return new_image