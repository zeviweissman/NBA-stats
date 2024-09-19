from model.Player import Player
from typing import List
from utils.calc_utils import *
from toolz import pipe, partial
from copy  import deepcopy
def parse_json_to_relvant_info(json):
    return {
      "player_name":json.get("playerName"),
      "position": json.get("position"),
      "games": json.get("games"),
      "three_percent": json.get("threePercent") or 0,
      "two_percent": json.get("twoPercent") or 0,
      "atr": calc_atr(json.get("assists"), json.get("turnovers")),
      "ppg": calc_ppg(json.get("points"),json.get("games")),
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


map_to_player_model = lambda li: map(lambda player: Player(**player), li)


def get_players_with_ppg_ratio(players):
    average_ppg = calc_ppg_average_from_list_of_players(deepcopy(players))
    return pipe(
        players,
        partial(map,lambda player:(player, {"ppgRatio":calc_ppg_ratio(player, average_ppg)})),
        list
    )



players = [
    Player(
        player_name="Zach LaVine",
        position="SG",
        games=25,
        three_percent=0.349,
        two_percent=0.536,
        atr=5,
        ppg=19,
        points=487,
        team="CHI",
        season=2024,
        player_id_str="lavinza01"
    ),
    Player(
        player_name="DeMar DeRozan",
        position="SF",
        games=25,
        three_percent=0.275,
        two_percent=0.491,
        atr=6,
        ppg=18,
        points=450,
        team="CHI",
        season=2024,
        player_id_str="derozde01"
    ),
    Player(
        player_name="Nikola Vucevic",
        position="C",
        games=25,
        three_percent=0.368,
        two_percent=0.523,
        atr=10,
        ppg=17,
        points=425,
        team="CHI",
        season=2024,
        player_id_str="vucevic01"
    ),
    Player(
        player_name="Lonzo Ball",
        position="PG",
        games=20,
        three_percent=0.392,
        two_percent=0.462,
        atr=4,
        ppg=14,
        points=280,
        team="CHI",
        season=2024,
        player_id_str="balllo01"
    ),
    Player(
        player_name="Patrick Williams",
        position="PF",
        games=25,
        three_percent=0.350,
        two_percent=0.490,
        atr=7,
        ppg=12,
        points=300,
        team="CHI",
        season=2024,
        player_id_str="willipa01"
    ),
    Player(
        player_name="Kobe White",
        position="PG",
        games=25,
        three_percent=0.325,
        two_percent=0.500,
        atr=5,
        ppg=15,
        points=375,
        team="CHI",
        season=2024,
        player_id_str="whiteko01"
    ),
    Player(
        player_name="Alex Caruso",
        position="SG",
        games=22,
        three_percent=0.300,
        two_percent=0.475,
        atr=3,
        ppg=8,
        points=176,
        team="CHI",
        season=2024,
        player_id_str="carusal01"
    ),
    Player(
        player_name="Tony Bradley",
        position="C",
        games=15,
        three_percent=0.150,
        two_percent=0.400,
        atr=2,
        ppg=5,
        points=75,
        team="CHI",
        season=2024,
        player_id_str="bradley01"
    ),
    Player(
        player_name="Derrick Jones Jr.",
        position="SF",
        games=20,
        three_percent=0.280,
        two_percent=0.460,
        atr=4,
        ppg=9,
        points=180,
        team="CHI",
        season=2024,
        player_id_str="jonesde01"
    ),
    Player(
        player_name="Marko Simonovic",
        position="C",
        games=18,
        three_percent=0.200,
        two_percent=0.430,
        atr=3,
        ppg=100,
        points=208,
        team="CHI",
        season=2024,
        player_id_str="simonma01"
    )
]

