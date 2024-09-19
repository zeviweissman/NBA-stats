from model.Player import Player
from utils.calc_utils import calc_atr, calc_ppg
from toolz import pipe, partial
def parse_json_to_relvant_info(json):
    return {
      "player_name":json.get("playerName"),
      "position": json.get("position"),
      "games": json.get("games"),
      "three_percent": json.get("threePercent") if json.get("threePercent") else 0,
      "two_percent": json.get("twoPercent") if json.get("twoPercent") else 0,
      "atr": calc_atr(json.get("assists"), json.get("turnovers")),
      "ppg": calc_ppg(1,1),
      "points": json.get("points"),
      "team": json.get("team"),
      "season": json.get("season"),
      "player_id_str": json.get("playerId")
    }






def convert_from_json_to_player(json):
    return Player(**json)

def map_list_of_json_to_list_of_players(json):
    return pipe(
        json,
        partial(map, parse_json_to_relvant_info),
        partial(map, convert_from_json_to_player),
        list
    )