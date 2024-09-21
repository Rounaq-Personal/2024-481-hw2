import subprocess
import os

def process_filenames():
    # Step 1: Read filenames from rk-input.txt
    with open('driver-input.txt', 'r') as file:
        filenames = [line.strip() for line in file]

    # Step 2: Process each filename
    for filename in filenames:
        print("Processing {}:".format(filename))
        
        # Run ./pngtest command
        pngtest_command = "./pngtest rk-submission/{}".format(filename)
        print("Running command: {}".format(pngtest_command))
        try:
            subprocess.check_call(pngtest_command, shell=True)
        except subprocess.CalledProcessError as e:
            print("Error running pngtest for {}: {}".format(filename, e))
            continue

        # Run gcov command
        gcov_command = "gcov *.c"
        print("Running command: {}".format(gcov_command))
        try:
            subprocess.check_call(gcov_command, shell=True)
        except subprocess.CalledProcessError as e:
            print("Error running gcov: {}".format(e))
        
    end_command = "gcovr --html-details coverage.html --exclude '.*contrib/.*'"
    subprocess.check_call(end_command, shell=True)
    
    subprocess.check_call("rm *.gcda pngout.png", shell=True)

    print("Processing complete.")

if __name__ == "__main__":
    process_filenames()
