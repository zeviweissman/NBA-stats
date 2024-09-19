from repository.database import create_db_if_not_exist, drop_db
import pytest
import repository.player_repository as player_repository
import repository.intiate_database as seed_repository

@pytest.fixture(scope="module")
def setup_database():
    create_db_if_not_exist()
    yield


def test_get_all_players(setup_database):
    players = player_repository.get_all_players()
    assert len(players) == 450


def test_get_all_players_by_param(setup_database):
    players_of_2022 = player_repository.get_all_players_by_param('season', 2022)
    players_of_2023 = player_repository.get_all_players_by_param('season', 2023)
    players_of_2024 = player_repository.get_all_players_by_param('season', 2024)
    assert len(players_of_2022) == 150
    assert len(players_of_2023) == 150
    assert len(players_of_2024) == 150
def test_get_player_by_id(setup_database):
    player = player_repository.get_player_by_id(100)
    assert player[0]["player_name"] == "Chris Duarte"

