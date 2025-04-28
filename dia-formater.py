import gzip
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Format JSON log files with newline replacements.")
parser.add_argument("input_file", type=str, help="The path to the input .gz file.")
parser.add_argument("output_file", type=str, nargs="?", default="formatted.json", help="The path to the output file. Defaults to 'formatted-log-file.txt'.")

# Parse command-line arguments
args = parser.parse_args()

# Determine if the input file is a .gz or .json file based on its extension
input_file = args.input_file
file_extension = os.path.splitext(input_file)[-1]

# Read content based on the file extension
if file_extension == ".gz":
    # If the file is a .gz, use gzip to read it
    with gzip.open(input_file, "rt", encoding="utf-8") as file:
        log_content = file.read()
elif file_extension == ".json":
    # If the file is a .json, read it normally
    with open(input_file, "r", encoding="utf-8") as file:
        log_content = file.read()
elif file_extension == ".zip":
    with zipfile.ZipFile(input_file, "r") as zip_ref:
        # Expect the diagnose.json file inside
        try:
            with zip_ref.open("diagnose.json") as file:
                log_content = file.read().decode("utf-8")
        except KeyError:
            raise ValueError("diagnose.json not found inside the ZIP file.")
else:
    raise ValueError("Unsupported file format. Please provide a .gz or .json file.")

# Replace literal \n with actual newlines
formatted_content = log_content.replace("\\n", "\n")

# Write the formatted content to the specified output file
with open(args.output_file, "w") as formatted_file:
    formatted_file.write(formatted_content)

print(f"Formatting complete. Check '{args.output_file}'.")
