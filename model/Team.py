from dataclasses import dataclass

@dataclass
class Team:
    team_name: str
    sg_player_id: int
    sf_player_id: int
    pg_player_id: int
    pf_player_id: int
    c_player_id: int
    team_id: int = None