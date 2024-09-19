from dataclasses import asdict
import service.player_service as player_service
from flask import Blueprint, jsonify

player_blueprint = Blueprint("player", __name__)


@player_blueprint.route('/<player_position>', methods=['GET'])
def get_players_by_postion(player_position):
    players = player_service.get_all_players_by_postion(player_position)
    return jsonify(players), 200



@player_blueprint.route('/<player_position>/<int:season>', methods=['GET'])
def get_players_by_postion_and_season(player_position, season):
    players = player_service.get_all_players_by_postion_and_season(player_position, season)
    return jsonify(players), 200