#!/usr/bin/env python3
"""Interactive Todo List Application.

A simple, user-friendly CLI for managing your tasks.
"""

import sys
import shlex
from colorama import Fore, Style, init
from src.models.task import Task, TaskStatus
from src.services.task_store import TaskStore

# Initialize colorama for cross-platform colored output
init(autoreset=True)


def print_banner() -> None:
    """Print welcome banner."""
    print()
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * 50}")
    print(f"{Fore.GREEN}{Style.BRIGHT}           TODO LIST MANAGER")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * 50}")
    print(f"{Fore.YELLOW}Your friendly task management companion!")
    print(f"{Fore.WHITE}Type {Fore.CYAN}help{Fore.WHITE} to see available commands.")
    print()


def print_help() -> None:
    """Print available commands with clear explanations."""
    print(f"{Fore.WHITE}{Style.BRIGHT}+{'-' * 48}+")
    print(f"{Fore.WHITE}{Style.BRIGHT}|{'Available Commands':^48}|")
    print(f"{Fore.WHITE}{Style.BRIGHT}+{'-' * 48}+")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.GREEN}add{Style.RESET_ALL} <title> [desc]                      |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Add a new task{Style.RESET_ALL}" + " " * 30 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.BLUE}list{Style.RESET_ALL}                                   |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Show all tasks{Style.RESET_ALL}" + " " * 31 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.MAGENTA}get{Style.RESET_ALL} <id>                               |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   View task details{Style.RESET_ALL}" + " " * 28 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.RED}delete{Style.RESET_ALL} <id>                            |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Remove a task{Style.RESET_ALL}" + " " * 30 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.CYAN}complete{Style.RESET_ALL} <id>                          |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Mark task as done{Style.RESET_ALL}" + " " * 27 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.YELLOW}count{Style.RESET_ALL}                                  |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Show task count{Style.RESET_ALL}" + " " * 29 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.LIGHTRED_EX}clear{Style.RESET_ALL}                                  |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Delete ALL tasks (confirmation required){Style.RESET_ALL}" + " " + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.WHITE}help{Style.RESET_ALL}                                  |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Show this help message{Style.RESET_ALL}" + " " * 24 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}| {Fore.WHITE}exit{Style.RESET_ALL}                                  |")
    print(f"{Fore.WHITE}{Style.BRIGHT}|   Close the application{Style.RESET_ALL}" + " " * 26 + "|")
    print(f"{Fore.WHITE}{Style.BRIGHT}+{'-' * 48}+")
    print()
    print(f"{Fore.LIGHTBLACK_EX}Tips:{Style.RESET_ALL}")
    print(f"  - Use quotes for multi-word descriptions: {Fore.CYAN}add \"Buy Groceries\" \"Milk, eggs, bread\"{Style.RESET_ALL}")
    print(f"  - Press {Fore.CYAN}Ctrl+C{Style.RESET_ALL} to exit anytime")
    print()


def cmd_add(args: list[str], store: TaskStore) -> None:
    """Add a new task."""
    if not args:
        print(f"{Fore.RED}Error: Missing task title{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Usage: {Fore.GREEN}add{Style.RESET_ALL} <title> [description]")
        print(f"{Fore.LIGHTBLACK_EX}Example: add \"Buy Groceries\" \"Get milk and eggs\"{Style.RESET_ALL}")
        return

    # shlex.split() already removes quotes, but strip any remaining whitespace
    title = args[0].strip()
    description = " ".join(args[1:]).strip() if len(args) > 1 else ""

    # Validate title
    if not title:
        print(f"{Fore.RED}Error: Task title cannot be empty{Style.RESET_ALL}")
        return

    if len(title) > 100:
        print(f"{Fore.RED}Error: Title is too long (max 100 characters){Style.RESET_ALL}")
        return

    try:
        task = Task(title=title, description=description)
        store.add(task)
        print(f"{Fore.GREEN}[OK] Task added successfully!{Style.RESET_ALL}")
        print(f"   ID: {Fore.CYAN}{task.id}{Style.RESET_ALL}")
        print(f"   Title: {task.title}")
        if task.description:
            print(f"   Description: {task.description}")
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")


def cmd_list(store: TaskStore) -> None:
    """List all tasks with nice formatting."""
    tasks = store.get_all()
    if not tasks:
        print(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Add a task with: {Fore.GREEN}add <title> [description]{Style.RESET_ALL}")
        return

    print(f"\n{Fore.WHITE}{Style.BRIGHT}Your Tasks ({len(tasks)} total):{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-' * 60}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}{'ID':<4} {'Status':<10} {'Title':<40}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-' * 60}{Style.RESET_ALL}")

    for task in tasks:
        status_icon = {
            TaskStatus.PENDING: f"{Fore.YELLOW}[ ]{Style.RESET_ALL}",
            TaskStatus.IN_PROGRESS: f"{Fore.BLUE}[~]{Style.RESET_ALL}",
            TaskStatus.COMPLETED: f"{Fore.GREEN}[X]{Style.RESET_ALL}",
        }.get(task.status, f"{Fore.LIGHTBLACK_EX}[?]{Style.RESET_ALL}")

        title = task.title[:38] + ".." if len(task.title) > 40 else task.title

        print(f"{task.id:<4} {status_icon:<10} {title:<40}")
    print(f"{Fore.CYAN}{'-' * 60}{Style.RESET_ALL}\n")


def cmd_get(args: list[str], store: TaskStore) -> None:
    """Get task details by ID."""
    if not args:
        print(f"{Fore.RED}Error: Missing task ID{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Usage: {Fore.MAGENTA}get{Style.RESET_ALL} <id>")
        return

    try:
        task_id = int(args[0])
        task = store.get(task_id)
        if task:
            status_color = {
                TaskStatus.PENDING: Fore.YELLOW,
                TaskStatus.IN_PROGRESS: Fore.BLUE,
                TaskStatus.COMPLETED: Fore.GREEN,
            }.get(task.status, Fore.WHITE)

            print(f"\n{Fore.WHITE}{Style.BRIGHT}Task Details:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'-' * 40}{Style.RESET_ALL}")
            print(f"  {Fore.WHITE}ID:        {Fore.CYAN}{task.id}{Style.RESET_ALL}")
            print(f"  {Fore.WHITE}Title:     {task.title}")
            print(f"  {Fore.WHITE}Status:    {status_color}{task.status.value.upper()}{Style.RESET_ALL}")
            if task.description:
                print(f"  {Fore.WHITE}Description:{Style.RESET_ALL}")
                print(f"    {task.description}")
            print(f"{Fore.CYAN}{'-' * 40}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Task #{task_id} not found.{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Use {Fore.BLUE}list{Fore.LIGHTBLACK_EX} to see all tasks.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Error: Invalid ID '{args[0]}'{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Task IDs are numbers (e.g., 1, 2, 3){Style.RESET_ALL}")


def cmd_delete(args: list[str], store: TaskStore) -> None:
    """Delete task by ID."""
    if not args:
        print(f"{Fore.RED}Error: Missing task ID{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Usage: {Fore.RED}delete{Style.RESET_ALL} <id>")
        return

    try:
        task_id = int(args[0])
        task = store.get(task_id)
        if task:
            confirm = input(f"{Fore.YELLOW}Delete task #{task_id} '{task.title}'? (y/n): {Style.RESET_ALL}").strip().lower()
            if confirm in ('y', 'yes'):
                store.delete(task_id)
                print(f"{Fore.GREEN}[OK] Task #{task_id} deleted.{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTBLACK_EX}Deletion cancelled.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Task #{task_id} not found.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Error: Invalid ID '{args[0]}'{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Task IDs are numbers (e.g., 1, 2, 3){Style.RESET_ALL}")


def cmd_complete(args: list[str], store: TaskStore) -> None:
    """Mark task as complete."""
    if not args:
        print(f"{Fore.RED}Error: Missing task ID{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Usage: {Fore.CYAN}complete{Style.RESET_ALL} <id>")
        return

    try:
        task_id = int(args[0])
        task = store.update(task_id, status=TaskStatus.COMPLETED)
        if task:
            print(f"{Fore.GREEN}[OK] Task #{task_id} marked as complete!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Task #{task_id} not found.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Error: Invalid ID '{args[0]}'{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Task IDs are numbers (e.g., 1, 2, 3){Style.RESET_ALL}")


def cmd_count(store: TaskStore) -> None:
    """Show task count with breakdown."""
    count = store.count()
    tasks = store.get_all()

    pending = sum(1 for t in tasks if t.status == TaskStatus.PENDING)
    in_progress = sum(1 for t in tasks if t.status == TaskStatus.IN_PROGRESS)
    completed = sum(1 for t in tasks if t.status == TaskStatus.COMPLETED)

    print(f"\n{Fore.WHITE}{Style.BRIGHT}Task Statistics:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-' * 30}{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}Total:    {Fore.CYAN}{count}{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}Pending:  {pending}{Style.RESET_ALL}")
    print(f"  {Fore.BLUE}In Prog:  {in_progress}{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}Done:     {completed}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-' * 30}{Style.RESET_ALL}\n")


def cmd_clear(store: TaskStore) -> None:
    """Delete all tasks with confirmation."""
    count = store.count()
    if count == 0:
        print(f"{Fore.YELLOW}No tasks to clear.{Style.RESET_ALL}")
        return

    print(f"{Fore.RED}{Style.BRIGHT}WARNING:{Style.RESET_ALL}")
    print(f"  This will delete ALL {count} tasks. This cannot be undone!")
    confirm = input(f"\n{Fore.RED}Are you sure you want to delete everything? (type 'yes' to confirm): {Style.RESET_ALL}").strip()

    if confirm == "yes":
        store.clear()
        print(f"{Fore.GREEN}[OK] All tasks have been deleted.{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTBLACK_EX}Clear cancelled.{Style.RESET_ALL}")


def main() -> int:
    """Run the interactive todo shell."""
    store = TaskStore()
    print_banner()
    print_help()

    while True:
        try:
            # Use a simple prompt without the "todo>" prefix to avoid confusion
            line = input(f"{Fore.CYAN}todo> {Style.RESET_ALL}").strip()

            # Skip empty input
            if not line:
                continue

            # Remove "todo>" prefix if user accidentally included it
            if line.startswith("todo>"):
                line = line[5:].strip()
                if not line:
                    continue

            try:
                parts = shlex.split(line)
            except ValueError as e:
                print(f"{Fore.RED}Error: Invalid quotes in command - {e}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTBLACK_EX}Make sure all quotes are properly closed.{Style.RESET_ALL}\n")
                continue

            cmd = parts[0].lower()
            args = parts[1:]

            if cmd in ("exit", "quit", "q"):
                print(f"\n{Fore.GREEN}Goodbye! Have a productive day!{Style.RESET_ALL}")
                return 0
            elif cmd in ("help", "h", "?"):
                print_help()
            elif cmd == "add":
                cmd_add(args, store)
            elif cmd == "list":
                cmd_list(store)
            elif cmd == "get":
                cmd_get(args, store)
            elif cmd == "delete":
                cmd_delete(args, store)
            elif cmd == "complete":
                cmd_complete(args, store)
            elif cmd == "count":
                cmd_count(store)
            elif cmd == "clear":
                cmd_clear(store)
            else:
                print(f"\n{Fore.RED}Unknown command: '{cmd}'{Style.RESET_ALL}")
                print(f"{Fore.LIGHTBLACK_EX}Type {Fore.CYAN}help{Fore.LIGHTBLACK_EX} to see available commands.{Style.RESET_ALL}\n")

        except KeyboardInterrupt:
            print(f"\n\n{Fore.GREEN}Goodbye! Have a productive day!{Style.RESET_ALL}")
            return 0
        except EOFError:
            print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
            return 0
        except Exception as e:
            print(f"\n{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Press Ctrl+C to restart if needed.{Style.RESET_ALL}\n")


if __name__ == "__main__":
    sys.exit(main())
