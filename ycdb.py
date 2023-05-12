import mysql.connector

db = mysql.connector.connect(host="localhost",
    user="root",
    passwd="Havana12!@#$",
    database="ycombinatordb"
)

mycursor = db.cursor()

compaines = [("Amplitude", "B2B Software and services", "Analytics", "B2B", "W12","San Francisco CA, USA", "Remote"),
             ("Segment", "B2B Software and services", "Analytics", "B2B, SAAS", "S11", "San Francisco CA, USA", "Remote"),
             ("Mixpanel", "B2B Software and services", "Analytics","B2B, CLOUD COMPUTING, DATABASE, DATA VISUALIZATION", "S09", "San Francisco CA, New york NY, Seattle WA, USA", "Remote"),
             ("Heap", "B2B Software and services", "Analytics", "SAAS", "W13", "San Francisco CA, USA", "Remote"),
             ("PostHog", "B2B Software and services", "Analytics","B2B, OPEN SOURCE", "W20","San Francisco CA, USA", "Remote"),
             ("Scuba", "B2B Software and services", "Analytics", "BIG DATA", "W13", "Redwood City CA, USA", "Remote"),
             ("HockeyStack", "B2B Software and services", "Analytics", "B2B, SAAS, DATA VISUALIZATION", "S23","San Francisco CA, USA", "Remote"),
             ("Poll Everywhere", "B2B Software and services", "Analytics","SAAS", "S08","San Francisco CA, USA", "Remote"),
             ("Drift Bio", "B2B Software and services", "Analytics","B2B, SAAS, BIOTECH, GENOMICS", "W23","San Francisco CA, USA", "Remote"),
             ("Turntable", "B2B Software and services", "Analytics", "AI", "W23", "New york NY, Austin TX, USA", "Remote"),
             ("CorgiAI", "B2B Software and services", "Analytics", "AI", "W23", "Remote"),
             ("Mantys","B2B Software and services", "Analytics","B2B, SAAS, FINANCE", "W23", "Bengaluru KA, India","Remote"),
             ("")]