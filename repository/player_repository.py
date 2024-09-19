from model.Player import Player
from repository.database import get_from_database, change_in_data_base
from typing import List
from toolz import curry


def add_player(player: Player) -> int:
    new_id = change_in_data_base(
        """
        INSERT INTO players (player_name, position, games, three_percent, two_percent, atr, ppg, points, team, season, player_id_str, ppg_ratio) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        RETURNING player_id
        """,
        (
            player.player_name,
            player.position,
            player.games,
            player.three_percent,
            player.two_percent,
            player.atr,
            player.ppg,
            player.points,
            player.team,
            player.season,
            player.player_id_str,
            player.ppg_ratio
        )
    )
    return new_id['player_id'] if new_id else None



def add_player_range(players: List[Player]):
    for player in players:
        add_player(player)


def get_all_players():
    return get_from_database(
        "SELECT * FROM players"
    )

@curry
def get_all_players_by_param(param, param_value):
    valid_params = ['player_name', 'position', 'games', 'three_percent', 'two_percent', 'atr', 'ppg', 'points', 'team', 'season', 'player_id_str', 'player_id']
    if param not in valid_params:
        raise Exception("invalid sql coulmn try a different one")
    return get_from_database(
        f"SELECT * FROM players WHERE {param} = %s",
        (param_value,)
    )


@curry
def get_all_players_by_two_params(param1, param2, param_value1, parm_value2):
    valid_params = ['player_name', 'position', 'games', 'three_percent', 'two_percent', 'atr', 'ppg', 'points', 'team', 'season', 'player_id_str', 'player_id']
    if param1 not in valid_params or param2 not in valid_params:
        raise Exception("invalid sql coulmn try a different one")
    return get_from_database(
        f"SELECT * FROM players WHERE {param1} = %s AND {param2} = %s",
        (param_value1, parm_value2)
    )





def get_player_by_id(player_id):
    return get_from_database(
        "SELECT * FROM players WHERE player_id = %s",
        (player_id,)
    )


