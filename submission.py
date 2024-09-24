"""# Importing the main functions from the other two files
import mars_planner
import routefinder

def main():
    # Call the main function from mars_planner
    mars_planner.main()
    
    # Call the main function from routefinder
    routefinder.main()

# Entry point for submission.py
if __name__ == "__main__":
    main()
"""    
import subprocess

# Run mars_planner.py
subprocess.run(["python3", "mars_planner.py"])

# Run routefinder.py
subprocess.run(["python3", "routefinder.py"])

# Run mapcoloring.py
subprocess.run(["python3", "mapcoloring.py"])
