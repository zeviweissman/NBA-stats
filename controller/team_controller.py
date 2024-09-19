from dataclasses import asdict
import service.team_service as team_service
from flask import Blueprint, jsonify, request

team_blueprint = Blueprint("team", __name__)

@team_blueprint.route('/<int:team_id>', methods=['GET'])
def get_team_by_id(team_id):
    team = team_service.get_team_by_id(team_id)
    return jsonify(team), 200



@team_blueprint.route('/create', methods=['POST'])
def create_team():
    json = request.json
    team = team_service.create_team(json)
    return jsonify(team), 201


@team_blueprint.route('/delete/<int:team_id>', methods=['DELETE'])
def delete_team_by_id(team_id):
    team = team_service.delete_team_by_id(team_id)
    return jsonify(team), 200