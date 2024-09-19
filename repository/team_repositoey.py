from repository.database import get_from_database, change_in_data_base
from typing import List
from model.Team import Team
def create_team(team: Team):
    new_id = change_in_data_base(
        """INSERT INTO teams (team_name, sg_player_id, sf_player_id, pg_player_id , pf_player_id, c_player_id) 
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING team_id
        """,
        (team.team_name, team.SG_player_id, team.SF_player_id, team.PG_player_id, team.PF_player_id, team.C_player_id)
    )
    return new_id['team_id'] if new_id else None

def get_team_by_id(team_id):
    return get_from_database(
        """
        SELECT * 
        FROM teams t 
        INNER JOIN players p ON 
            p.player_id IN (t.sg_player_id, t.sf_player_id, t.pg_player_id, t.pf_player_id, t.c_player_id)
        WHERE t.team_id = %s
        """,
        (team_id,)
    ) or None


def delete_team_by_id(team_id):
    return change_in_data_base(
        """
        DELETE FROM teams WHERE team_id = %s RETURNING *
        """, (team_id,)
    ) or None


# def update_team(team):
#     team = change_in_data_base(
#         """
#             UPDATE users
#             SET first_name = %s, last_name = %s, email = %s
#             WHERE user_id = %s
#             RETURNING *
#         """, (user.first_name, user.last_name, user.email, user.user_id)
#     )
#     return User(**user) if user else None

