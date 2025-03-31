from par_pro.cli import get_parser, run_command  # Import CLI utilities

def main():
    # Get the command-line parser and parse arguments
    parser = get_parser()
    args = parser.parse_args()

    # Execute the mapped command
    run_command(args.command)

# Standard entry point for script execution
if __name__ == "__main__":
    main()
