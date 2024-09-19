from dataclasses import dataclass

@dataclass
class Player:
    player_id_str: str
    player_name: str
    atr: int
    ppg: int
    team: str
    season: int
    points: int
    position: str
    games: int
    three_percent: float
    two_percent: float
    player_id: int = None
