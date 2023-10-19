import os

from dotenv import dotenv_values


def find_env_file(filename=".env"):
    # Start from the current directory
    current_dir = os.getcwd()

    # Traverse parent directories until the specified filename is found
    while True:
        env_path = os.path.join(current_dir, filename)
        if os.path.isfile(env_path):
            return env_path
        parent_dir = os.path.dirname(current_dir)

        # Break the loop if we've reached the root directory
        if current_dir == parent_dir:
            break

        current_dir = parent_dir

    # If the specified file is not found, return None
    return None


dot_env_file = find_env_file(filename=".env.variables")
config = dotenv_values(dot_env_file)
