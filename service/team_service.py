from model.Team import Team
import repository.team_repositoey as team_repository

def create_team(team):
    return team_repository.create_team(Team(**team))

def get_team_by_id(team_id):
    team = team_repository.get_team_by_id(team_id)
    return team


def delete_team_by_id(team_id):
    return team_repository.delete_team_by_id(team_id)