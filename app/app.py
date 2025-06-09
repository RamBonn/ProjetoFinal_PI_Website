import requests
from flask import Flask, render_template, jsonify
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('principal.html')

@app.route("/api/seismic")
def seismic_data():
    url = 'https://api.ipma.pt/open-data/observation/seismic/7.json'
    headers = { 'User-Agent': 'Mozilla/5.0' }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        raw_data = res.json().get("data", [])
    except Exception as e:
        return jsonify({"error": "Failed to fetch seismic data", "details": str(e)}), 500

    now = datetime.utcnow()
    results = []

    for quake in raw_data:
        try:
            lat = float(quake.get("lat"))
            lon = float(quake.get("lon"))
            mag = float(quake.get("magnitud", 1.0))
            region = quake.get("obsRegion", "Unknown region")
            time_str = quake.get("time")
            if not (lat and lon and time_str):
                continue

            time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
            age_hours = (now - time_obj).total_seconds() / 3600

            results.append({
                "lat": lat,
                "lon": lon,
                "mag": mag,
                "region": region,
                "time": time_str,
                "age_hours": age_hours
            })

        except Exception:
            continue  # skip bad entries

    return jsonify(results)

