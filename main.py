import csv
from validator import validate_record
from processor import process_record

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"


def read_input_file():
    with open(INPUT_FILE, mode="r") as file:
        return list(csv.DictReader(file))


def write_output_file(data):
    if not data:
        return

    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    records = read_input_file()
    processed_data = []

    for record in records:
        if validate_record(record):
            processed = process_record(record)
            processed_data.append(processed)

    write_output_file(processed_data)
    print("Processing completed. Check output.csv")


if __name__ == "__main__":
    main()

