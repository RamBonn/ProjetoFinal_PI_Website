from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/api/seismic')
def get_seismic_data():
    url = 'https://api.ipma.pt/open-data/observation/seismic/7.json'
    try:
        res = requests.get(url)
        data = res.json().get('data', [])
    except Exception as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

    now = datetime.utcnow()
    filtered = []

    for quake in data:
        try:
            lat = float(quake.get('lat', 0))
            lon = float(quake.get('lon', 0))
            mag = float(quake.get('magnitud', 1.0))
            time_str = quake.get('time')
            region = quake.get('obsRegion', 'Unknown region')
            if not (lat and lon and time_str):
                continue

            time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
            age_hours = (now - time_obj).total_seconds() / 3600

            filtered.append({
                'lat': lat,
                'lon': lon,
                'mag': mag,
                'time': time_str,
                'region': region,
                'age_hours': age_hours
            })

        except Exception as e:
            continue

    return jsonify(filtered)
