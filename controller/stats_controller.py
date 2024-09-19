import service.team_service as team_service
from flask import Blueprint, jsonify

stats_blueprint = Blueprint("stats", __name__)

@stats_blueprint.route('/team<int:team1_id>/team<int:team2_id>', methods=['GET'])
def compare_two_teams(team1_id, team2_id):
    res = team_service.compare_two_teams(team1_id, team2_id)
    return jsonify(players), 200


