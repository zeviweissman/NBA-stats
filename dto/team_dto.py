from dataclasses import dataclass
from model.Player import Player

@dataclass
class TeamDTO:
  team_name: str
  team_ppg_ratio: float
  sg_player: Player
  sf_player: Player
  pg_player: Player
  pf_player: Player
  c_player: Player
  team_id: int