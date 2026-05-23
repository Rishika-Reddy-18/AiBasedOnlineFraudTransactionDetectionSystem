def rule_based_check(data):

    amount = data["amount"]
    device = data["device_change"]
    location = data["location_change"]

    # HIGH RISK FRAUD
    if amount > 50000 and device == 1 and location == 1:
        return "FRAUD"

    # MEDIUM RISK
    if amount > 30000 and (device == 1 or location == 1):
        return "SUSPICIOUS"

    return "SAFE"