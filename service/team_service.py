from model.Team import Team
import repository.team_repositoey as team_repository
from utils.convert_utils import parse_info_of_two_teams

def create_team(team):
    return team_repository.create_team(Team(**team))

def get_team_by_id(team_id):
    team = team_repository.get_team_by_id(team_id)
    return team


def delete_team_by_id(team_id):
    return team_repository.delete_team_by_id(team_id)

def compare_two_teams(team1_id, team2_id):
    team1 = get_team_by_id(team1_id)
    team2 = get_team_by_id(team2_id)
    parse_info_of_two_teams(team1, team2)

compare_two_teams(1,2)