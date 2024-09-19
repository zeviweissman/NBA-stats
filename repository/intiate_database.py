from repository.player_repository import add_player_range
from api_service.get_service import get_NBA_player_models_of_last_three_seasons


def seed_players():
    players = get_NBA_player_models_of_last_three_seasons()
    add_player_range(players)


seed_players()