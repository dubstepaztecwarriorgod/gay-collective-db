from pathlib import Path
from db_types import *


class GayCollectiveDb:
    '''
    I think the idea here is that we store the data which will look smth like

    ```
    age:20
    name:png
    games_is_bad_at:cod;cs2;minecraft
    ```

    into a map as long as we don't have too many items dictated by `max_capacity()`
    '''
    def __init__(self, db_path: str) -> None:
        self.src: Path = Path(db_path)
        self.data: DbData = None
    
    def __str__(self):
        return f"Path: {self.src}\nData: {self.data}"