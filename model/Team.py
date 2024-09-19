from dataclasses import dataclass
from typing import List
from model.Player import Player

class team:
    players: List[Player]
    id: int = None