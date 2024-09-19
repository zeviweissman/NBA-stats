import requests
from utils import convert_utils
from toolz import pipe

_generate_NBA_stats_url_by_year = lambda year: f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=150"



def _get_from_api(url):
    response = requests.request('GET', url)
    return response.json()

def _get_nba_stats_by_year(year):
    url = _generate_NBA_stats_url_by_year(year)
    return _get_from_api(url)

def _get_nba_player_models(year):
    return pipe(
        _get_nba_stats_by_year(year),
        convert_utils.map_json_to_player_models,
        convert_utils.get_players_with_ppg_ratio
    )
def _get_2024_player_models():
    return _get_nba_player_models(2024)
def _get_2023_player_models():
    return _get_nba_player_models(2023)

def _get_2022_player_models():
    return _get_nba_player_models(2022)




def get_NBA_player_models_of_last_three_seasons():
    return _get_2024_player_models() + _get_2023_player_models() + _get_2022_player_models()


