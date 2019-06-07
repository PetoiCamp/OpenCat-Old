_READLINE_LIBRARY_VERSION = '7.0'
_READLINE_RUNTIME_VERSION = 1792
_READLINE_VERSION = 1792
__doc__ = 'Importing this module enables command line editing using GNU readline.'
__file__ = '/usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'readline'
__package__ = ''
def add_history(string):
    'add_history(string) -> None\nadd an item to the history buffer'
    pass

def append_history_file(nelements, filename=None):
    'append_history_file(nelements[, filename]) -> None\nAppend the last nelements items of the history list to file.\nThe default filename is ~/.history.'
    pass

def clear_history():
    'clear_history() -> None\nClear the current readline history.'
    pass

def get_begidx():
    'get_begidx() -> int\nget the beginning index of the completion scope'
    return 1

def get_completer():
    'get_completer() -> function\n\nReturns current completer function.'
    pass

def get_completer_delims():
    'get_completer_delims() -> string\nget the word delimiters for completion'
    return ''

def get_completion_type():
    'get_completion_type() -> int\nGet the type of completion being attempted.'
    return 1

def get_current_history_length():
    'get_current_history_length() -> integer\nreturn the current (not the maximum) length of history.'
    return 1

def get_endidx():
    'get_endidx() -> int\nget the ending index of the completion scope'
    return 1

def get_history_item():
    'get_history_item() -> string\nreturn the current contents of history item at index.'
    return ''

def get_history_length():
    'get_history_length() -> int\nreturn the maximum number of lines that will be written to\nthe history file.'
    return 1

def get_line_buffer():
    'get_line_buffer() -> string\nreturn the current contents of the line buffer.'
    return ''

def insert_text(string):
    'insert_text(string) -> None\nInsert text into the line buffer at the cursor position.'
    pass

def parse_and_bind(string):
    'parse_and_bind(string) -> None\nExecute the init line provided in the string argument.'
    pass

def read_history_file(filename=None):
    'read_history_file([filename]) -> None\nLoad a readline history file.\nThe default filename is ~/.history.'
    pass

def read_init_file(filename=None):
    'read_init_file([filename]) -> None\nExecute a readline initialization file.\nThe default filename is the last filename used.'
    pass

def redisplay():
    "redisplay() -> None\nChange what's displayed on the screen to reflect the current\ncontents of the line buffer."
    pass

def remove_history_item(pos):
    'remove_history_item(pos) -> None\nremove history item given by its position'
    pass

def replace_history_item(pos, line):
    'replace_history_item(pos, line) -> None\nreplaces history item given by its position with contents of line'
    pass

def set_auto_history(enabled):
    'set_auto_history(enabled) -> None\nEnables or disables automatic history.'
    pass

def set_completer(function=None):
    "set_completer([function]) -> None\nSet or remove the completer function.\nThe function is called as function(text, state),\nfor state in 0, 1, 2, ..., until it returns a non-string.\nIt should return the next possible completion starting with 'text'."
    pass

def set_completer_delims(string):
    'set_completer_delims(string) -> None\nset the word delimiters for completion'
    pass

def set_completion_display_matches_hook(function=None):
    'set_completion_display_matches_hook([function]) -> None\nSet or remove the completion display function.\nThe function is called as\n  function(substitution, [matches], longest_match_length)\nonce each time matches need to be displayed.'
    pass

def set_history_length(length):
    'set_history_length(length) -> None\nset the maximal number of lines which will be written to\nthe history file. A negative length is used to inhibit\nhistory truncation.'
    pass

def set_pre_input_hook(function=None):
    'set_pre_input_hook([function]) -> None\nSet or remove the function invoked by the rl_pre_input_hook callback.\nThe function is called with no arguments after the first prompt\nhas been printed and just before readline starts reading input\ncharacters.'
    pass

def set_startup_hook(function=None):
    'set_startup_hook([function]) -> None\nSet or remove the function invoked by the rl_startup_hook callback.\nThe function is called with no arguments just\nbefore readline prints the first prompt.'
    pass

def write_history_file(filename=None):
    'write_history_file([filename]) -> None\nSave a readline history file.\nThe default filename is ~/.history.'
    pass

