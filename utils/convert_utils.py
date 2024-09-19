from model.Player import Player

def convert_from_json_to_player(json):
    return Player(**json)

def map_list_of_json_to_list_of_players(json):
    return list(map(convert_from_json_to_player, json))