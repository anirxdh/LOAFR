import sys # Used for command line arguments
sys.path.insert(1, '/src') # Add our source directory for imports
from src import model
from src import viewcli
from src import controller

def run():
    """Runs the LOAFR program.

    Parses the system arguments (if present) to determine which version of LOAFR
    should be run, and launches the system controller in the given mode.
    
    Raises:
        ValueError: An error occurred when parsing the program arguments.
    """
    
    print("Welcome to LOAFR!")
    
    mode = "cli"  # Default to CLI if no arguments are given
    if (len(sys.argv) > 1):
        mode = sys.argv[1]

    if (mode == "cli"):
        m = model.Model()
        v = viewcli.ViewCLI()
        c = controller.Controller(m, v)
    elif (mode == "gui"):
        print("GUI - Not implemented")
    else:
        print(f"Invalid argument. {mode} is not a valid mode.")
        return
        
    return

# Program entry point
if __name__ == "__main__":
    run()
