# Simple fraud risk scoring logic

valid_number = True
carrier_present = True
country = "India"

risk_score = 0

if not valid_number:
    risk_score += 50

if not carrier_present:
    risk_score += 20

if country != "India":
    risk_score += 30

print("Fraud Risk Score:", risk_score)
