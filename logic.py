def getStatus(read, total):
    if read == 0:
        return "Plan to Read"
    elif read >= total:
        return "Completed"
    return "Reading"

def progressPercent(read, total):
    return round(read / total * 100, 1)