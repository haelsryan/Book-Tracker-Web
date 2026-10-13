def getStatus(read, total):
    if read == 0:
        return "Plan to Read"
    elif read >= total:
        return "Completed"
    return "Reading"

def progressPercent(read, total):
    if total == 0:
        return 0.0
    return round(read / total * 100, 1)