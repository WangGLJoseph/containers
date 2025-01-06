import docker
import time
import sys


import sys
import time

def main():
    try:
        # Initialize Docker client
        client = docker.from_env()
    except docker.errors.DockerException as e:
        print(f"Error connecting to Docker: {e}")
        sys.exit(1)

    # Number of containers to run
    num_containers = 5  # You can adjust this number as needed

    # List to keep track of container objects
    containers = []

    try:
        print("Pulling the 'busybox' image...")
        client.images.pull('busybox')
        print("Image pulled successfully.")
    except docker.errors.APIError as e:
        print(f"Error pulling image: {e}")
        sys.exit(1)

    print(f"Starting {num_containers} containers...")
    for i in range(num_containers):
        try:
            container = client.containers.run(
                'busybox',
                command='tail -f /dev/null',
                detach=True,
                name=f'container_{i}'
            )
            containers.append(container)
            print(f"Started container {i + 1}/{num_containers}: {container.id}")
        except docker.errors.APIError as e:
            print(f"Error starting container {i + 1}: {e}")

    print("All containers started. Waiting for 10 seconds...")
    time.sleep(10)

    print("Stopping and removing containers...")
    for i, container in enumerate(containers):
        try:
            container.stop()
            container.remove()
            print(f"Stopped and removed container {i + 1}/{len(containers)}: {container.id}")
        except docker.errors.APIError as e:
            print(f"Error stopping/removing container {container.id}: {e}")

    print("All containers have been stopped and removed.")


if __name__ == "__main__":
    main()
