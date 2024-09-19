from model.Player import Player
from dataclasses import asdict
from typing import List
from utils.calc_utils import *
from toolz import pipe, partial
from copy  import deepcopy
from dto.team_dto import TeamDTO
def parse_player_json_to_relvant_info(json):
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


def parse_team_json_to_relvant_info(json):
    return {
      "player_name":json.get("player_name"),
      "position": json.get("position"),
      "games": json.get("games"),
      "three_percent": json.get("three_percent") or 0,
      "two_percent": json.get("two_percent") or 0,
      "atr": json.get("atr"),
      "ppg": json.get("ppg"),
      "points": json.get("points"),
      "team": json.get("team"),
      "season": json.get("season"),
      "player_id_str": json.get("player_id_str"),
        "player_id": json.get("player_id")
    }


def convert_from_json_to_player(json):
    return Player(**json)

def map_json_to_player_models(json):
    return pipe(
        json,
        partial(map, parse_json_to_relvant_info),
        partial(map, convert_from_json_to_player),
    )


map_to_player_model = lambda li: map(lambda player: Player(**player), li)


def get_players_with_ppg_ratio(players):
    average_ppg = calc_ppg_average_from_list_of_players(deepcopy(players))
    return pipe(
        players,
        partial(map,lambda player:(Player(**{**asdict(player),"ppg_ratio":calc_ppg_ratio(player, average_ppg)}))),
        list
    )

def convert_team_player_into_player(player):
    return parse_team_json_to_relvant_info(player)


def parse_team_info(team):
    team_ppg_ratio = sum([player.get("ppg_ratio") for player in team])
    team_name = team[0]["team_name"]
    team_id = team[0]["team_id"]
    sg_player = convert_team_player_into_player(team[0])
    sf_player = convert_team_player_into_player(team[1])
    pg_player = convert_team_player_into_player(team[2])
    pf_player = convert_team_player_into_player(team[3])
    c_player = convert_team_player_into_player(team[4])
    return TeamDTO(team_id=team_id,
                   team_name=team_name,
                   team_ppg_ratio=team_ppg_ratio,
                   c_player=c_player,
                   pf_player=pf_player,
                   pg_player=pg_player,
                   sf_player=sf_player,
                   sg_player=sg_player)


def parse_info_of_two_teams(team1, team2):
    return parse_team_info(team1), parse_team_info(team2)
