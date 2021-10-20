"""
    L5_10_interactive_ui.py
    
    ECOR 1051 Fall 2019
    Milestone 3
    
    Authors:
    Group L5-10
        Bren Gelyn Padlan, 101148482
        Claire Baggesen, 101149755
        Stacey Nip, 101151872
        Ajiile Moodie, 101147889
    
    Submitted on December 1, 2019
"""
from Cimpl import choose_file, load_image, copy, show, save_as, Image

from L5_10_image_filters import two_tone, three_tone, extreme_contrast, sepia, \
                                posterize, detect_edges, detect_edges_better, \
                                flip_vertical, flip_horizontal
#-------------------------------------------------------------------------------
def display_prompt() -> str:
    """ Prints a message prompting the user to enter one of the commands and 
    returns the uppercase input entered by the user.
    
    >>> display_prompt()
    <input entered by user>
    """
    user_input = input("\nL)oad image    S)ave-as \n" 
                       + "2)-tone    3)tone    X)treme contrast    T)int sepia    P)osterize \n" 
                       + "E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip \n" 
                       + "Q)uit \n" 
                       + ": "
                       )  
    user_input = user_input.upper()
    return user_input


def apply_filter(user_input: str, image: Image) -> Image:
    """ Applies the filter.
    
    >>> apply_filter(input_entered, final_image)
    """
    if user_input == "2":
            filtered_image = two_tone(image, 'yellow', 'cyan')
    elif user_input == "3":
            filtered_image = three_tone(image, 'yellow', 'magenta', 'cyan')
    elif user_input == "X":
            filtered_image = extreme_contrast(image)
    elif user_input == "T":
            filtered_image = sepia(image)
    elif user_input == "P":
            filtered_image = posterize(image)
    elif user_input == "E":
            thresh = int(input("Threshold? "))
            filtered_image = detect_edges(image, thresh)
    elif user_input == "I":
            thresh = int(input("Threshold? "))
            filtered_image = detect_edges_better(image, thresh)
    elif user_input == "V":
            filtered_image = flip_vertical(image)
    elif user_input == "H":
            filtered_image = flip_horizontal(image)  
    show(filtered_image)        
    return filtered_image


def load() -> Image:
    """ Returns an image loaded by the user.
    
    >>> load()
    """
    image = load_image(choose_file())
    show(image)
    return image
    
    
def is_command_filter(list_commands: list, user_input: str) -> bool:
    """ Returns True if the user_input is a command for a filter.
    Otherwise, it returns False.
    
    >>> is_command_filter(commands, input_entered)
    True
    """
    num_filters = 9
    length_list = len(list_commands)
    for i in range((length_list - num_filters), length_list):
        if user_input == list_commands[i]:
            return True
    return False    
    

def is_valid(list_commands: list, user_input: str) -> bool:
    """ Returns True if the user_input is in the valid list of commands.
    Otherwise, it returns False.
    
    >>> is_valid(commands, input_entered)
    True
    """
    for command in list_commands:
        if user_input == command:
            return True
    print("No such command")
    return False
            
#-------------------------------------------------------------------------------
image = None
commands = ["L", "S", "Q", "2", "3", "X", "T", "P", "E", "I", "V", "H"]

input_entered = display_prompt()
command_valid = is_valid(commands, input_entered)

while input_entered != "Q":
    if command_valid and image == None:
        if input_entered == "L":
            image = load()
            final_image = copy(image)
        else:
            print("No image loaded")
    elif command_valid and image != None:
        if input_entered == "L":
            image = load()
            final_image = copy(image)
        elif is_command_filter(commands, input_entered):
            final_image = apply_filter(input_entered, final_image)
        elif input_entered == "S":
            save_as(final_image)                
                
    input_entered = display_prompt()
    command_valid = is_valid(commands, input_entered)