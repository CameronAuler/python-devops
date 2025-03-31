import argparse  # For parsing command-line arguments
from par_pro.multi_processing.mp_use_cases import run_prime_computation_use_case  # Multiprocessing use case
from par_pro.threading.th_use_cases import run_network_simulation_use_case       # Threading use case

# Updated command mapping based on actual use cases defined
COMMANDS = {
    "primes": run_prime_computation_use_case,    # CPU-bound multiprocessing example
    "network": run_network_simulation_use_case,  # I/O-bound threading example
}


def get_parser() -> argparse.ArgumentParser:
    """
    Returns a configured ArgumentParser with registered subcommands.
    """
    parser = argparse.ArgumentParser(
        description="Run parallel processing use cases (multiprocessing + threading)"
    )
    parser.add_argument(
        "command",
        choices=COMMANDS.keys(),
        help="Use case to run (e.g., primes, network)"
    )
    return parser


def run_command(command: str):
    """
    Executes the function associated with the given command.
    """
    fn = COMMANDS[command]  # Get the function tied to the command
    print(f"\n=== Running: {command} ===")
    fn()  # Execute the selected use case
    print("\n=== Execution complete ===\n")
