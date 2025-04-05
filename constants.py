# Python doesn't have real constants without jumping through hoops to do bullshit but functions should work just fine as constants too since these are "Pure" 

def prefix_separator() -> str:
    '''
    The character that separates the prefix from the value
    
    Example: `name:dub`
    '''
    return ":"

def value_separator() -> str:
    '''
    The character that separates multiple value
    
    Example `names:dub;dubby;doob`
    '''
    return ";"

def max_capacity() -> int:
    '''
    The db should be pretty fast if try and keep everything in memory as a map but there's only so much data you can store before it becomes way too much.
    Once this number is exceeded we should switch to doing all operations in a file via IO instead of the map. so even though it will be slower it won't
    use nearly the same memory usage
    '''
    # We should actually test this later to figure out a good number to choose this is just a stand in
    return 0xDEAD