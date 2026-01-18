def validate_record(record):
    """
    Validates a single data record.
    Returns True if valid, False otherwise.
    """

    # Check for missing values
    if not record["id"] or not record["name"] or not record["age"] or not record["salary"]:
        return False

    # Check if age is a number
    if not record["age"].isdigit():
        return False

    # Check if salary is a number
    if not record["salary"].isdigit():
        return False

    return True

