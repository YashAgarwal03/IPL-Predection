from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# IPL Teams
teams = {
    "CSK": {
        "name": "Chennai Super Kings",
        "played": 11,
        "won": 6,
        "lost": 5,
        "points": 12
    },

    "DC": {
        "name": "Delhi Capitals",
        "played": 12,
        "won": 5,
        "lost": 7,
        "points": 10
    },

    "GT": {
        "name": "Gujarat Titans",
        "played": 11,
        "won": 7,
        "lost": 4,
        "points": 14
    },

    "KKR": {
        "name": "Kolkata Knight Riders",
        "played": 10,
        "won": 4,
        "lost": 5,
        "points": 9
    },

    "LSG": {
        "name": "Lucknow Super Giants",
        "played": 11,
        "won": 3,
        "lost": 8,
        "points": 6
    },

    "MI": {
        "name": "Mumbai Indians",
        "played": 11,
        "won": 3,
        "lost": 8,
        "points": 6
    },

    "PBKS": {
        "name": "Punjab Kings",
        "played": 11,
        "won": 6,
        "lost": 4,
        "points": 13
    },

    "RR": {
        "name": "Rajasthan Royals",
        "played": 11,
        "won": 6,
        "lost": 5,
        "points": 12
    },

    "RCB": {
        "name": "Royal Challengers Bengaluru",
        "played": 11,
        "won": 7,
        "lost": 4,
        "points": 14
    },

    "SRH": {
        "name": "Sunrisers Hyderabad",
        "played": 11,
        "won": 7,
        "lost": 4,
        "points": 14
    }
}


@app.route("/")
def home():

    return render_template(
        "index.html",
        teams=teams
    )


@app.route("/update", methods=["POST"])
def update():

    data = request.get_json()

    team1 = data["team1"]
    team2 = data["team2"]
    winner = data["winner"]

    # Validation
    if team1 == team2:

        return jsonify({
            "error": "Teams cannot be same"
        })

    # No Result
    if winner == "No Result":

        teams[team1]["played"] += 1
        teams[team2]["played"] += 1

        teams[team1]["points"] += 1
        teams[team2]["points"] += 1

    else:

        loser = team2 if winner == team1 else team1

        # Winner
        teams[winner]["played"] += 1
        teams[winner]["won"] += 1
        teams[winner]["points"] += 2

        # Loser
        teams[loser]["played"] += 1
        teams[loser]["lost"] += 1

    # SORT TABLE
    sorted_teams = dict(

        sorted(

            teams.items(),

            key=lambda item: item[1]["points"],

            reverse=True
        )
    )

    return jsonify(sorted_teams)

if __name__ == "__main__":

    app.run(debug=True)