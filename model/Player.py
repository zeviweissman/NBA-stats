from dataclasses import dataclass

@dataclass
class Player:
    playerName: str
    position: str
    games: int
    threePercent: float
    twoPercent: float
    atr: int
    ppg: int
    points: int
    team: str
    season: int
    playerId: str