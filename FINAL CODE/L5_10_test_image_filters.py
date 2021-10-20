"""
    L5_10_test_image_filters.py
    
    ECOR 1051 Fall 2019
    Milestone 2
    
    Group L5-10
        Bren Gelyn Padlan, 101148482
        Claire Baggesen, 101149755
        Stacey Nip, 101151872
        Ajiile Moodie, 101147889
    
    Submitted on November 24, 2019
    
"""
from Cimpl import choose_file, load_image, copy, create_image, create_color,\
                  set_color, get_color, show, Image 

from L5_10_image_filters import two_tone, three_tone, extreme_contrast, sepia, posterize, \
                                detect_edges, detect_edges_better, flip_vertical, flip_horizontal

#-----------------------------------------------------------------
def test_two_tone() -> None:
    """ Author: Stacey Nip
    Tests the two-tone filter function. 
    If it passes, print 'Two-tone filter passed.' otherwise print 'Two-tone fiter failed."
    
    >>> test_two_tone()
    """
    image = create_image(2, 1)
    set_color(image, 0, 0, create_color(20, 15, 0))
    set_color(image, 1, 0, create_color(120, 200, 155))
    
    expected = create_image(2, 1)
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(128, 128, 128))

    two_toned = two_tone(image, 'lime', 'gray')
    for x, y, (r, g, b) in two_toned:
        if get_color(two_toned, x, y) == get_color(expected, x, y):
            print ('Two-tone filter passed.')
        else:
            print ('Two-tone filter failed.')
            print ('Actual:', get_color(two_toned, x, y))
            print ('Expected:', get_color(expected, x, y))
    return
            

def test_three_tone() -> None:
    """ Author: Stacey Nip
    Tests the three-tone filter function. 
    If it passes, print 'Three-tone filter passed.' otherwise print 'Three-tone filter failed."
    
    >>> test_three_tone()
    """
    image = create_image(3, 1)
    set_color(image, 0, 0, create_color(2, 25, 10))
    set_color(image, 1, 0, create_color(220, 25, 50))
    set_color(image, 2, 0, create_color(200, 200, 255))
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(255, 0 ,0))
    set_color(expected, 2, 0, create_color(0, 0, 255))
    
    three_toned = three_tone(image, 'lime', 'red', 'blue')
    for x, y, (r, g, b) in three_toned:
        if get_color(three_toned, x, y) == get_color(expected, x, y):
            print ('Three-tone filter passed.')
        else: 
            print ('Three-tone filter failed.')
            print ('Actual:', get_color(three_toned, x, y))
            print ('Expected:', get_color(expected, x, y))
    return


def test_extreme() -> None:
    """ Author: Ajiile Moodie
    Tests that the funtion extreme_contrast works as expected.

    >>> test_extreme()
    """     
    original = create_image(8,1)
    set_color(original, 0, 0, create_color(150, 80, 90))
    set_color(original, 1, 0, create_color(180, 150, 80))
    set_color(original, 2, 0, create_color(150, 90, 180))
    set_color(original, 3, 0, create_color(80, 150, 50))
    set_color(original, 4, 0, create_color(80, 170, 150))
    set_color(original, 5, 0, create_color(80, 100, 160))
    set_color(original, 6, 0, create_color(150, 150, 150))
    set_color(original, 7, 0, create_color(70, 60, 70))
    
    expected = create_image(8,1)
    set_color(expected, 0, 0, create_color(255, 0, 0))
    set_color(expected, 1, 0, create_color(255, 255, 0))
    set_color(expected, 2, 0, create_color(255, 0, 255))
    set_color(expected, 3, 0, create_color(0, 255, 0))
    set_color(expected, 4, 0, create_color(0, 255, 255))
    set_color(expected, 5, 0, create_color(0, 0, 255))
    set_color(expected, 6, 0, create_color(255, 255, 255))
    set_color(expected, 7, 0, create_color(0, 0, 0))
    
    extreme_image = extreme_contrast(original)    
    for x, y, (r, g, b) in extreme_image:
        if get_color(extreme_image , x, y) == get_color(expected, x, y):
            print('Extreme Contrast Passes')
        else:
            print('Extreme Contrast Fails')
            print(get_color(extreme_image , x, y))
            print(get_color(expected, x, y))
    return  


def test_sepia(image: Image): 
    """ Author: Claire Baggesen, 101149755
    Tests if all the pixels in the image are sepia. 
 
    >>> test_sepia()
    """    
    final_result = "Passed"
    for x, y, (r, g, b) in new_photo:
        sepia = sepia_image.get_color(x, y)
        average = (r + g + b)//3 
   
        if average < 63:
            sepia_filter = create_color(average*1.1, average, average*0.9)
        elif average < 192: 
            sepia_filter = create_color(average*1.15, average, average*0.85)
        else:
            sepia_filter = create_color(average*1.08, average, average*0.93)
        if not sepia == sepia_filter:
            print("Test failed at X =", x, ",Y =", y, sepia)
            final_result = "Failed"     
    print ("Test", final_result)
    return


def test_adjust_component() -> None:
    """ Author: Bren-Gelyn Padlan
    Tests the helper function _adjust_component()
    
    >>> test_adjust_component()
    Enter a pixel component(0-255): 255
    _adjust_component() function Passed
    >>> test_adjust_component()
    Enter a pixel component(0-255): 115
    _adjust_component() function Passed
    >>> test_adjust_component()
    Enter a pixel component(0-255): 0
    _adjust_component() function Passed
    """
    pixel_comp = int(input("Enter a pixel component(0-255): "))
    new_component_value = L5_10_P4_posterize._adjust_component(pixel_comp)
    
    (Q1_MIN, Q1_MIDPOINT, Q1_MAX) = (0, 31, 63)
    (Q2_MIN, Q2_MIDPOINT, Q2_MAX) = (64, 95, 127)
    (Q3_MIN, Q3_MIDPOINT, Q3_MAX) = (128, 159, 191)
    (Q4_MIN, Q4_MIDPOINT, Q4_MAX) = (192, 233, 255)
    
    if Q1_MIN <= pixel_comp <= Q1_MAX:
        if new_component_value != Q1_MIDPOINT:
            print("_adjust_component() function Failed: Adjusted component value,",
                  new_component_value, "is not equal to quadrant 1 midpoint value", Q1_MIDPOINT) 
            return        
    elif Q2_MIN <= pixel_comp <= Q2_MAX:
        if new_component_value != Q2_MIDPOINT:
            print("_adjust_component() function Failed: Adjusted component value,", 
                  new_component_value, "is not equal to quadrant 2 midpoint value", Q2_MIDPOINT) 
            return         
    elif Q3_MIN <= pixel_comp <= Q3_MAX:
        if new_component_value != Q3_MIDPOINT:
            print("_adjust_component() function Failed: Adjusted component value,", 
                  new_component_value, "is not equal to quadrant 3 midpoint value", Q3_MIDPOINT) 
            return            
    elif Q4_MIN <= pixel_comp <= Q4_MAX:
        if new_component_value != Q4_MIDPOINT:
            print("_adjust_component() function Failed: Adjusted component value,", 
                  new_component_value, "is not equal to quadrant 4 midpoint value", Q4_MIDPOINT) 
            return    
    else:
        print("_adjust_component() function Passed")
        return
        
    
def test_posterize() -> None:
    """ Author: Bren-Gelyn Padlan
    Tests the function posterize() and prints a message if it passed or failed.
    
    >>> test_posterize()
    Posterize Filter Channel Passed
    """
    original_image = create_image(3,1)
    set_color(original_image, 0,0, create_color(50,100,150))
    set_color(original_image, 1,0, create_color(100,150,50))
    set_color(original_image, 2,0, create_color(150,200,100))
    
    expected_image = create_image(3,1)
    set_color(expected_image, 0,0, create_color(31, 95, 159))
    set_color(expected_image, 1,0, create_color(95, 159, 31)) 
    set_color(expected_image, 2,0, create_color(159, 223, 95))     
    
    posterize_image = L5_10_P4_posterize.posterize(original_image)  
    
    for y in range(1):
        for x in range(3):
            posterize_r, posterize_g, posterize_b = get_color(posterize_image, x, y)
            expected_r, expected_g, expected_b = get_color(expected_image, x, y)
            
            if (posterize_r != expected_r) or (posterize_g != expected_g) or (posterize_b != expected_b):
                print('Posterize Channel Filter Failed: Pixel @ (', x, ',', y, ') r =', posterize_r, 'g =', posterize_g, 'b =', posterize_b)
            else:
                print("Posterize Channel Filter Passed")   
    return        


def test_edge() -> None:
    """ Author: Bren-Gelyn Padlan
    Tests the function detect_edges() and prints a message if it passed or failed. 
    For this test function,  a threshold of 50 was used.
    
    >>> test_edge()
    Edge Detection Filter Passed
    """
    THRESHOLD = 50
    
    original_image = create_image(1,3)
    set_color(original_image, 0,0, create_color(80, 100, 120))
    set_color(original_image, 0,1, create_color(140, 160, 180))
    set_color(original_image, 0,2, create_color(120, 150, 180))
                  
    expected_image = create_image(1,3)
    set_color(expected_image, 0,0, create_color(0, 0, 0))
    set_color(expected_image, 0,1, create_color(255, 255, 255))
    
    edge_image = detect_edges(original_image, THRESHOLD)
    
    for y in range(0,2):
        edge_color = get_color(edge_image, 0,y)
        expect_color = get_color(expected_image, 0,y)
        
        if edge_color != expect_color:
            print('Edge Detection Filter Failed')
        else:
            print('Edge Detection Filter Passed') 
    return


def test_detect_imp_edges() -> None:
    """ Author: Claire Baggesen, 101149755
    Tests the function detect_edges_better(). 
    For this test function, a threshold of 50 was used.  
    
    >>> test_detect_imp_edges()
    Improved Edge Detection Filter Passed
    """
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    original = create_image(3, 3)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 10, 20))
    set_color(original, 2, 0, create_color(132, 132, 132))
    set_color(original, 0, 1, create_color(123, 63, 212))
    set_color(original, 1, 1, create_color(200, 123, 192))
    set_color(original, 2, 1, create_color(255, 255, 255))
    set_color(original, 0, 2, create_color(189, 12, 23))
    set_color(original, 1, 2, create_color(12, 76, 42))
    set_color(original, 2, 2, create_color(0, 20, 10))

    expected_image = create_image(3, 3)
    set_color(expected_image, 0, 0, create_color(0, 0, 0))
    set_color(expected_image, 1, 0, create_color(0, 0, 0))
    set_color(expected_image, 2, 0, create_color(132, 132, 132))
    set_color(expected_image, 0, 1, create_color(0, 0, 0))
    set_color(expected_image, 1, 1, create_color(0, 0, 0))
    set_color(expected_image, 2, 1, create_color(255, 255, 255))
    set_color(expected_image, 0, 2, create_color(189, 12, 23))
    set_color(expected_image, 1, 2, create_color(12, 76, 42))
    set_color(expected_image, 2, 2, create_color(0, 20, 10))
    
    imp_edge_image = detect_edges_better(original, 12)
    
    for pixel in imp_edge_image:
        x, y, (r, g, b) = pixel
        if (r, g, b) == get_color(expected_image, x, y):
            print("PASSED", x, y)
        else:
            print("FAILED", x, y)      
    return


def test_vertical() -> None:
    """ Author: Stacey Nip, 101151872
    Tests vertical flip function. 
    If it passes, print 'Vertical flip passed.' otherwise print 'Vertical flip failed.'
    
    >>> test_vertical()
    """
    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(25, 62, 16))
    set_color(original, 1, 0, create_color(45, 90, 2))
    set_color(original, 2, 0, create_color(18, 250, 153))
    set_color(original, 3, 0, create_color(245, 144, 62))
    
    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(245, 144, 62))
    set_color(expected, 1, 0, create_color(18, 250, 153))
    set_color(expected, 2, 0, create_color(45, 90, 2))
    set_color(expected, 3, 0, create_color(25, 62, 16))
    
    flipped_vertical = flip_vertical(original)
    for x, y, (r, g, b) in flipped_vertical:
        if get_color(flipped_vertical, x, y) == get_color(expected, x, y):
            print ('Vertical flip passed.')
        else:
            print ('Vertical flip failed.')
            print ('Actual color:', get_color(flipped_vertical, x, y))
            print ('Expected color:', get_color(expected, x, y))
    return


def test_horizontal()-> None:
    """ Author: Ajiile Moodie, 101147889
    Tests if the function flip_horizontal works as expected.
    
    >>> test_horizontal()
    """
    original = create_image(1,2)
    set_color(original, 0, 0, create_color(44,55,33))
    set_color(original, 0, 1, create_color(67,78,89))
    
    expected = create_image(1,2)
    set_color(expected, 0, 0, create_color(67,78,89))
    set_color(expected, 0, 1, create_color(44,55,33))
    
    flipped_horizontal = flip_horizontal(original)
    
    for x, y, (r, g, b) in flipped_horizontal:
        if get_color(flipped_horizontal,x, y) == get_color(expected, x, y):
            print('Horizontal flip passes')
        else:
            print('Horizontal flip fails')
            print(get_color(flipped_horizontal,x, y))
            print(get_color(expected, x, y))
    return