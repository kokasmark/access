
class Color():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

    contrast_map = {
        '\33[90m': '\33[37m',  # CGREY -> CWHITE
        '\33[91m': '\33[31m',  # CRED2 -> CRED
        '\33[92m': '\33[32m',  # CGREEN2 -> CGREEN
        '\33[93m': '\33[33m',  # CYELLOW2 -> CYELLOW
        '\33[94m': '\33[34m',  # CBLUE2 -> CBLUE
        '\33[95m': '\33[35m',  # CVIOLET2 -> CVIOLET
        '\33[96m': '\33[36m',  # CBEIGE2 -> CBEIGE
        '\33[97m': '\33[90m',  # CWHITE2 -> CGREY

        '\33[30m': '\33[37m',  # CBLACK -> CWHITE
        '\33[31m': '\33[91m',  # CRED -> CRED2
        '\33[32m': '\33[92m',  # CGREEN -> CGREEN2
        '\33[33m': '\33[93m',  # CYELLOW -> CYELLOW2
        '\33[34m': '\33[94m',  # CBLUE -> CBLUE2
        '\33[35m': '\33[95m',  # CVIOLET -> CVIOLET2
        '\33[36m': '\33[96m',  # CBEIGE -> CBEIGE2
        '\33[37m': '\33[97m',  # CWHITE -> CWHITE2
    }

class Symbols():
    KEY = u"\U0001F511"
    OPEN_FOLDER = u"\U0001F4C2"
    RUN = u"\u23F5"
    INFO = u"\u2139"
    PENCIL = u"\u270F"
    FILE = u"\U0001F4C4"
    FOLDER = u"\U0001F4C1"
    BLOCK = u"\u2588"
    PLUS = u"\u2795"
    ESC = "esc"
    ENTER = "enter"
    UP_ARROW = u"\u2191"
    DOWN_ARROW = u"\u2193"
    LEFT_ARROW = u"\u2190"
    RIGHT_ARROW = u"\u2192"