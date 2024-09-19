from model.Player import Player
from repository.database import get_from_database, change_in_data_base
from typing import List
from toolz import curry


def add_player(player: Player) -> int:
    new_id = change_in_data_base(
        """
        INSERT INTO players (player_name, position, games, three_percent, two_percent, atr, ppg, points, team, season, player_id_str) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
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
            player.player_id_str
        )
    )
    return new_id['player_id'] if new_id else None



def add_player_range(players: List[Player]):
    for player in players:
        add_player(player)


def get_all_players() -> List[Player]:
    return get_from_database(
        "SELECT * FROM players"
    )

@curry
def get_all_players_by_param(param, param_value) -> List[Player]:
    valid_params = ['player_name', 'position', 'games', 'three_percent', 'two_percent', 'atr', 'ppg', 'points', 'team', 'season', 'player_id_str', 'player_id']
    if param not in valid_params:
        raise Exception("invalid sql coulmn try a different one")
    return get_from_database(
        f"SELECT * FROM players WHERE {param} = %s",
        (param_value,)
    )

get_all_players_by_season = get_all_players_by_param('season')
get_all_players_by_postion = get_all_players_by_param('position')


def get_player_by_id(player_id) -> Player:
    return get_from_database(
        "SELECT * FROM players WHERE player_id = %s", (player_id,)
    )


print(len(get_all_players()))
