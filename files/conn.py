import paramiko
import time
import random
from retrying import retry
from timeout_decorator import timeout

# SSH credentials
HOST = "192.168.4.64"
USERNAME = "xzhao2"
PASSWORD = "clover"
COMMAND = "sleep 8"  # Example command to run on the remote machine

# Retry decorator: Retries up to 3 times, waiting 2 seconds between attempts
@retry(stop_max_attempt_number=3, wait_fixed=2000)
# Timeout decorator: If the function takes longer than 5 seconds, it raises an error
@timeout(5)
def ssh_connect_and_run():
    print(f"Attempting SSH connection to {HOST}...")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Simulate random failures for testing purposes
        if random.choice([True, False]):
            raise ConnectionError("Simulated network issue, retrying...")

        # Establish SSH connection
        client.connect(HOST, username=USERNAME, password=PASSWORD)
        print("SSH connection successful!")

        # Execute a command
        stdin, stdout, stderr = client.exec_command(COMMAND)
        output = stdout.read().decode()
        print(f"Command output:\n{output}")

        return output
    except Exception as e:
        print(f"SSH error: {e}")
        raise  # Ensure the retry decorator catches this error and retries
    finally:
        client.close()

# Running the function
try:
    result = ssh_connect_and_run()
    print("SSH Task Completed Successfully!")
except Exception as e:
    print(f"SSH Operation failed: {e}")
