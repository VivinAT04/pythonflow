import argparse
import runpy

from .storage import Storage


def run_dag(file_path):
    runpy.run_path(file_path, run_name="__main__")


def show_history():
    storage = Storage()
    rows = storage.get_history()

    if not rows:
        print("No task history found.")
        return

    print("DAG | TASK | STATE | ATTEMPT | ERROR | CREATED_AT")
    print("-" * 70)

    for row in rows:
        dag_name, task_name, state, attempt, error, created_at = row
        print(
            f"{dag_name} | {task_name} | {state} | "
            f"{attempt} | {error or ''} | {created_at}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="PythonFlow workflow orchestrator"
    )

    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("file")

    subparsers.add_parser("history")

    args = parser.parse_args()

    if args.command == "run":
        run_dag(args.file)

    elif args.command == "history":
        show_history()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
