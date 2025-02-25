from fastapi import FastAPI, HTTPException
from models import CO2Reading
from crud import create_table, add_reading, get_all_readings

app = FastAPI()

# Initialize the DB
create_table()

@app.post("/readings/")
def create_reading(reading: CO2Reading):
    add_reading(reading.ppm, reading.timestamp)
    return reading

@app.get("/readings/")
def get_readings():
    readings = get_all_readings()
    return [{"ppm": row[0], "timestamp": row[1]} for row in readings]

@app.get("/")
def root():
    return {"message": "CO₂ Sen API is running!"}
