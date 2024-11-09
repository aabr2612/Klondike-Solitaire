def validate_movement(source,destination,source_index,destination_index):
    if (source not in ["T", "F", "W"] or destination not in ["T", "F"]) or (source=="F" and destination=="F"):
        return False

    if not (str(source_index).isnumeric() and str(destination_index).isnumeric()):
        return False
    
    source_index = int(source_index)
    destination_index = int(destination_index)
    
    if source == "T":
        if source_index < 1 or source_index > 7:
            return False
    elif source == "F":
        if source_index < 1 or source_index > 4:
            return False
    
    if destination == "T":
        if destination_index < 1 or destination_index > 7:
            return False
    elif destination == "F":
        if destination_index < 1 or destination_index > 4:
            return False
    
    if source==destination and destination_index==source_index:
        return False

    return True