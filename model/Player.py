from dataclasses import dataclass

@dataclass
class Player:
    id: int
    playerName: str
    position: str
    age: int
    games: int
    gamesStarted: int
    minutesPg: float
    fieldGoals: int
    fieldAttempts: int
    fieldPercent: float
    threeFg: int
    threeAttempts: int
    threePercent: float
    twoFg: int
    twoAttempts: int
    twoPercent: float
    effectFgPercent: float
    ft: int
    ftAttempts: int
    ftPercent: float
    offensiveRb: int
    defensiveRb: int
    totalRb: int
    assists: int
    steals: int
    blocks: int
    turnovers: int
    personalFouls: int
    points: int
    team: str
    season: int
    playerId: str