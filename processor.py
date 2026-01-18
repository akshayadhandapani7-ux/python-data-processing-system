def process_record(record):
    """
    Processes a valid record and returns a cleaned version.
    """

    processed = {
        "id": int(record["id"]),
        "name": record["name"].strip(),
        "age": int(record["age"]),
        "salary": int(record["salary"])
    }

    return processed

