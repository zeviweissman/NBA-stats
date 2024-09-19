from model.Player import Player
from typing import List
from toolz import pipe, partial
from operator import attrgetter
import statistics
def calc_ppg(points, games):
    return points / games if games > 0 else 0

def calc_atr(assists, turnovers):
    return assists / turnovers if turnovers > 0 else 0


def calc_ppg_average_from_list_of_players(players: List[Player]) -> float:
    return pipe(
        players,
        partial(map, attrgetter("ppg")),
        statistics.mean,
    )

def calc_ppg_ratio(player: Player, ppg_average: float):
    return player.ppg / ppg_average




