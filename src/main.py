import json

# === 1. Define the Alien class ===
class Alien:
    def __init__(self, id, name, homeworld, traits):
        self.id = id
        self.name = name
        self.homeworld = homeworld
        self.traits = traits
        self.universe = None  # will be filled later

    def summary(self):
        return f"{self.name} from {self.homeworld} → {self.universe}"


# === 2. Read data from input.json ===
def read_input(path="../input.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    aliens = [Alien(**a) for a in data]
    return aliens


# === 3. Classify each alien ===
def classify(aliens):
    for a in aliens:
        t = [trait.lower() for trait in a.traits]
        if "acid_blood" in t or "tentacles" in t:
            a.universe = "Alien"
        elif "rebel" in t or "laser_weapons" in t:
            a.universe = "StarWars"
        elif "metal_skin" in t or "avenger" in t:
            a.universe = "Marvel"
        else:
            a.universe = "Unknown"
    return aliens


# === 4. Save results to output.json ===
def write_output(aliens, path="../output.json"):
    data = [
        {
            "id": a.id,
            "name": a.name,
            "homeworld": a.homeworld,
            "traits": a.traits,
            "universe": a.universe
        }
        for a in aliens
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Saved results to", path)


# === 5. Main program ===
if __name__ == "__main__":
    aliens = read_input()
    aliens = classify(aliens)
    for a in aliens:
        print(a.summary())
    write_output(aliens)
