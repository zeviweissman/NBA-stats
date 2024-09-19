from dataclasses import asdict
import repository.player_repository as player_repository
from flask import Blueprint, jsonify

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route('/<player_position>', methods=['GET'])
def get_players_by_postion(player_position):
    players = player_repository.get_all_players_by_postion(player_position)
    return jsonify(players), 201