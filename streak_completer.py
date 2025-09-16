import subprocess
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2025, 6, 19)
end_date = datetime(2025, 8, 2)
file_name = "streak.txt"

# Generate commit dates
current_date = start_date
while current_date <= end_date:
    
    # Write or append something to the file
    with open(file_name, "a") as f:
        f.write(f"Commit for {current_date.strftime('%Y-%m-%d')}\n")
    
    # Stage the file
    subprocess.run(["git", "add", file_name])
    
    # Format date for Git
    date_str = current_date.strftime("%Y-%m-%d 12:00:00")
    
    # Commit with backdated author and committer date
    subprocess.run([
        "git", "commit", "-m", f"Commit for {current_date.strftime('%Y-%m-%d')}",
        "--date", date_str
    ], env={
        **subprocess.os.environ,
        "GIT_AUTHOR_DATE": date_str,
        "GIT_COMMITTER_DATE": date_str
    })
    
    print(f"Committed for {current_date.strftime('%Y-%m-%d')}")
    
    # Move to next day
    current_date += timedelta(days=1)

print("All commits are done!")
