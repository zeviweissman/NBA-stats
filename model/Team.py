from dataclasses import dataclass
from typing import List
from model.Player import Player

class team:
    team_name: str
    SG_player_id: int
    SF_player_id: int
    PG_player_id: int
    PF_player_id: int
    C_player_id: int
    team_id: int = None