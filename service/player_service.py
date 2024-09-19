import repository.player_repository as player_repository
from model.Player import Player
from utils.convert_utils import get_players_with_ppg_ratio, map_to_player_model
from toolz import pipe


def get_all_players():
    return pipe(
        player_repository.get_all_players(),
        map_to_player_model,
        get_players_with_ppg_ratio
    )

def get_all_players_by_season(season: int):
    return pipe(
        player_repository.get_all_players_by_param('season', season),
        map_to_player_model,
        get_players_with_ppg_ratio
    )

def get_all_players_by_postion(position: str):
    return pipe(
        player_repository.get_all_players_by_param('position', position),
        map_to_player_model,
        get_players_with_ppg_ratio
    )


def get_player_by_id(player_id):
    player = player_repository.get_player_by_id(player_id)
    return Player(**player)

