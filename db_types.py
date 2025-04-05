# The actual in memory structure of the database which is either a map or None if we're only working with a file
DbData = dict[str, str | list[str]] | None

# The potential return result from fetching the db
DbValue = str | list[str]
