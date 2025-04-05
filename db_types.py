from enum import IntFlag

# The actual in memory structure of the database which is either a map or None if we're only working with a file
DbData = dict[str, str | list[str]] | None

# The potential return result from fetching the db
DbValue = str | list[str]

class DbOptions(IntFlag):
    '''Flags for different db settings'''
    SAVE_ON_EXIT = 0b1