import repository.database as database
import repository.intiate_database as seed
from flask import Flask, jsonify, request
from controller.player_controller import player_blueprint
from controller.team_controller import team_blueprint
from controller.stats_controller import stats_blueprint
import os
def create_flask_app():
    app = Flask(__name__)
    app.register_blueprint(player_blueprint, url_prefix="/api/players")
    app.register_blueprint(team_blueprint, url_prefix="/api/teams")
    app.register_blueprint(stats_blueprint, url_prefix="/api/stats")
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        a = 0
        # database.drop_db()
        # database.create_db_if_not_exist()
        # seed.seed_players()
    return app


if __name__ == '__main__':
    app = create_flask_app()
    app.run(debug=True)