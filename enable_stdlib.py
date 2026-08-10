#!/usr/bin/env python3
import json
import sys


def get_stdlib_modules():
    """Return a sorted list of public standard library module names (including __future__)."""
    if hasattr(sys, "stdlib_module_names"):
        return sorted(
            mod for mod in sys.stdlib_module_names
            if not mod.startswith("_") or mod == "__future__"
        )
    else:
        # Fallback for older Python versions (not recommended)
        # A comprehensive static list is impractical; we rely on Python 3.10+.
        raise RuntimeError(
            "Python version < 3.10 is not supported. "
            "Please use Python 3.10 or newer."
        )


def main():
    modules = get_stdlib_modules()
    stdlib_str = ",".join(modules)

    # Load the JSON configuration
    json_file = "n8n-task-runners.json"
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_file} not found.")
        sys.exit(1)

    # Find the Python runner and update the environment variable
    updated = False
    for runner in data.get("task-runners", []):
        if runner.get("runner-type") == "python":
            env = runner.setdefault("env-overrides", {})
            env["N8N_RUNNERS_STDLIB_ALLOW"] = stdlib_str
            updated = True
            break

    if not updated:
        print("No Python runner found in the configuration. No changes made.")
        sys.exit(0)

    # Write the updated JSON back to the file
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")   # ensure trailing newline

    print("Successfully updated N8N_RUNNERS_STDLIB_ALLOW.")
    print(f"Number of standard library modules: {len(modules)}")


if __name__ == "__main__":
    main()