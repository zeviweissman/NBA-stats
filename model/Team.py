from dataclasses import dataclass

@dataclass
class Team:
    team_name: str
    SG_player_id: int
    SF_player_id: int
    PG_player_id: int
    PF_player_id: int
    C_player_id: int
    team_id: int = None