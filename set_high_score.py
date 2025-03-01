# High score dictionaries for Tic-Tac-Toe
TTThighScores = [
    {"name": "None", "score": 0},
    {"name": "None", "score": 0},
    {"name": "None", "score": 0}
]

# High score dictionaries for Number Guessing Game
NGGhighScores = [
    {"name": "None", "score": 0},
    {"name": "None", "score": 0},
    {"name": "None", "score": 0}
]

def setHighScore(game, name, score):
    """
    Updates the high scores for the given game.
    """
    # Select the correct high score list
    if game == "Tic-Tac-Toe":
        high_scores = TTThighScores
    elif game == "Number Guessing Game":
        high_scores = NGGhighScores
    else:
        print("Invalid game name.")
        return

    # Insert the new score in the correct position if it's high enough
    for i in range(3):
        if score >= high_scores[i]["score"]:
            high_scores.insert(i, {"name": name, "score": score})
            high_scores.pop()  # Remove the lowest score to maintain top 3
            break
