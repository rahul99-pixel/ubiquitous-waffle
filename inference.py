from flask import Flask, request, jsonify

app = Flask(__name__)

state = 0

@app.route("/")
def home():
    return "Server is running"

@app.route("/reset", methods=["GET", "POST"])
def reset():
    global state
    state = 0
    return jsonify({"state": state})

@app.route("/step", methods=["POST"])
def step():
    global state

    try:
        data = request.get_json(silent=True) or {}
        action = int(data.get("action", 0))
    except:
        action = 0

    if action == 1:
        state += 1
    elif action == 2:
        state -= 1

    reward = 1.0 if state == 5 else 0.0
    done = state == 5

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done,
        "info": {}
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
