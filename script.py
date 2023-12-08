import subprocess
import os

def resolve_conflicts():
    try:
        # Run 'git diff --name-only --diff-filter=U' to get conflicted files
        result = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=U'], capture_output=True, text=True, check=True)
        conflicted_files = result.stdout.splitlines()

        if not conflicted_files:
            print("No conflicted files found.")
            return

        for file in conflicted_files:
            try:
                # Run 'git diff --' to get the diff content for the conflicted file
                result = subprocess.run(['git', 'diff', '--', file], capture_output=True, text=True, check=True)
                diff_content = result.stdout

                # Create a diff file for each conflicted file
                diff_filename = f"{file}_diff.diff"
                with open(diff_filename, 'w') as diff_file:
                    diff_file.write(diff_content)

                print(f"Diff file created: {diff_filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error running Git command: {e}")

        # Ask the user to choose a strategy
        strategy = input("After reviewing the code, choose a strategy (1 for ours, 2 for theirs): ")
        
        cmd = int(strategy)
        if cmd not in [1, 2]:
            print("Invalid strategy. No changes applied.")
            return
        elif cmd == "1":
            subprocess.run(['git', 'checkout', '--ours', '--', *conflicted_files], check=True)
            print("Conflicts resolved using 'mine' strategy.")
        elif cmd == "2":
            subprocess.run(['git', 'checkout', '--theirs', '--', *conflicted_files], check=True)
            print("Conflicts resolved using 'theirs' strategy.")
        else:
            print("Invalid strategy. No changes applied.")

    except subprocess.CalledProcessError as e:
        print(f"Error running Git command: {e}")

if __name__ == "__main__":
    resolve_conflicts()
