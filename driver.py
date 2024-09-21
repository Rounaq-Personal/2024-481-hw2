import subprocess
import os

def process_filenames():
    # Step 1: Read filenames from rk-input.txt
    with open('driver-input.txt', 'r') as file:
        filenames = [line.strip() for line in file]

    # Step 2: Process each filename
    for filename in filenames:
        print(f"Processing {filename}:")
        
        # Run ./pngtest command
        pngtest_command = f"./pngtest /YOUR/TEST_SUITE/FILEPATH/HERE{filename}"
        print(f"Running command: {pngtest_command}")
        try:
            subprocess.run(pngtest_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running pngtest for {filename}: {e}")
            continue

        # Run gcov command
        gcov_command = "gcov *.c"
        print(f"Running command: {gcov_command}")
        try:
            subprocess.run(gcov_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running gcov: {e}")

    print("Processing complete.")

if __name__ == "__main__":
    process_filenames()
