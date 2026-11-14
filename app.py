from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simplified game data for learning. These are GAME BALANCE values,
# not real spacecraft engineering specifications.
INSTRUMENTS = {
    "camera": {"name": "High-Resolution Camera", "mass": 40, "power": 20, "cost": 12, "data": 25, "science": 25},
    "spectrometer": {"name": "Mineral Spectrometer", "mass": 55, "power": 30, "cost": 18, "data": 35, "science": 35},
    "radar": {"name": "Subsurface Radar", "mass": 70, "power": 40, "cost": 22, "data": 45, "science": 40},
    "magnetometer": {"name": "Magnetometer", "mass": 25, "power": 15, "cost": 9, "data": 15, "science": 18}
}

ROCKETS = {
    "small": {"name": "Pioneer", "capacity": 180, "cost": 25},
    "medium": {"name": "Pathfinder", "capacity": 300, "cost": 40},
    "heavy": {"name": "Atlas", "capacity": 500, "cost": 60}
}

ORBITS = {
    "low": {"name": "Low Lunar Orbit", "cost": 10, "communications": 70, "coverage": 65},
    "polar": {"name": "Polar Lunar Orbit", "cost": 15, "communications": 60, "coverage": 95},
    "high": {"name": "High Lunar Orbit", "cost": 8, "communications": 85, "coverage": 55}
}

OBJECTIVES = {
    "ice": {"name": "Search for Water Ice", "bonus": 30},
    "mapping": {"name": "Map the Lunar Surface", "bonus": 25},
    "geology": {"name": "Study Lunar Minerals", "bonus": 28}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulate", methods=["POST"])

def simulate():
    choices = request.get_json(silent=True)

    if not isinstance(choices, dict):
        return jsonify({"error": "Invalid mission data."}), 400

    objective = OBJECTIVES.get(
        choices.get("objective"), OBJECTIVES["ice"]
    )
    rocket = ROCKETS.get(
        choices.get("rocket"), ROCKETS["small"]
    )
    orbit = ORBITS.get(
        choices.get("orbit"), ORBITS["low"]
    )

    selected = [
        INSTRUMENTS[key]
        for key in choices.get("instruments", [])
        if key in INSTRUMENTS
    ]

    base_mass = 80
    base_power = 25
    base_cost = 30

    mass = base_mass + sum(item["mass"] for item in selected)
    power_needed = base_power + sum(item["power"] for item in selected)
    power_available = 100

    cost = (
        base_cost
        + rocket["cost"]
        + orbit["cost"]
        + sum(item["cost"] for item in selected)
    )

    data_generated = sum(item["data"] for item in selected)
    science = objective["bonus"] + sum(
        item["science"] for item in selected
    )

    budget = 120

    mass_ok = mass <= rocket["capacity"]
    budget_ok = cost <= budget
    power_ok = power_needed <= power_available
    communications_ok = data_generated <= orbit["communications"]

    issues = []

    if not mass_ok:
        issues.append("Your spacecraft is too heavy for the selected rocket.")

    if not budget_ok:
        issues.append("Your mission exceeds its available budget.")

    if not power_ok:
        issues.append("Your instruments need more power than the spacecraft can provide.")

    if not communications_ok:
        issues.append("Your instruments generate more data than the selected orbit can support transmitting.")

    score = 0
    score += 25 if mass_ok else 0
    score += 25 if budget_ok else 0
    score += 25 if power_ok else 0
    score += 25 if communications_ok else 0

    if not issues:
        score = min(100, score + min(science, 100) // 5)
        status = "MISSION READY"
        summary = "Your design meets the simplified mission constraints. The mission is ready for simulation."
    elif len(issues) == 1:
        status = "MISSION AT RISK"
        summary = "One major constraint needs attention before launch."
    else:
        status = "MISSION NOT READY"
        summary = "Several constraints conflict. Revise your design and simulate again."

    return jsonify({
        "status": status,
        "summary": summary,
        "score": score,
        "mass": mass,
        "rocket_capacity": rocket["capacity"],
        "power_needed": power_needed,
        "power_available": power_available,
        "cost": cost,
        "budget": budget,
        "data_generated": data_generated,
        "communications": orbit["communications"],
        "coverage": orbit["coverage"],
        "science": science,
        "issues": issues,
        "objective": objective["name"],
        "rocket": rocket["name"],
        "orbit": orbit["name"]
    })


if __name__ == "__main__":
    app.run(debug=True)