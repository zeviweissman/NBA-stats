import requests
from utils import convert_utils

_generate_NBA_stats_url_by_year = lambda year: f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=150"



def _get_from_api(url):
    response = requests.request('GET', url)
    return response.json()

def _get_nba_stats_by_year(year):
    url = _generate_NBA_stats_url_by_year(year)
    return _get_from_api(url)

def _get_2024_stats():
    return _get_nba_stats_by_year(2024)
def _get_2023_stats():
    return _get_nba_stats_by_year(2023)
def _get_2022_stats():
    return _get_nba_stats_by_year(2022)



def get_NBA_player_models_of_last_three_seasons():
    three_year_stats = _get_2022_stats() + _get_2023_stats() + _get_2024_stats()
    return convert_utils.map_list_of_json_to_list_of_players(three_year_stats)

