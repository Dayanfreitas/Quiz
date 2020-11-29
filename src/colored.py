from helper import Translation

def colored(color, text, bg = None, n=None):
    color = Translation.get_label(color)
    if bg:
        bg = Translation.get_label(bg)

    reset_color = '\033[0;0m'    
    negrito     = '\033[1m'

    colors = {
        'magenta': '\033[35m',
        'yellow' : '\033[33m',
        'black'  : '\033[37m',
        'white'  : '\033[30m',
        'green'  : '\033[32m',
        'blue'   : '\033[34m',
        'cian'   : '\033[36m',
        'red'    : '\033[31m',
    }

    background = {
        'background_magenta' : '\033[45m',
        'background_yellow'  : '\033[43m',
        'background_black'   : '\033[40m',
        'background_green'   : '\033[42m',
        'background_white'   : '\033[47m',
        'background_blue'    : '\033[44m',
        'background_cian'    : '\033[46m',
        'background_red'     : '\033[41m'
    }

    string_return = ''
    if colors.get(color) is not None:
        string_return += colors.get(color)

    if background.get(bg) is not None:
        string_return += background.get(bg)

    if n:
        string_return += negrito

    return string_return + text +  reset_color    