#!/bin/bash

# Loop through containers container_0 to container_4
for i in {0..4}; do
    container_name="container_$i"

    # Kill the container
    echo "Killing $container_name..."
    docker kill "$container_name" 2>/dev/null

    # Remove the container
    echo "Removing $container_name..."
    docker rm "$container_name" 2>/dev/null

done

echo "Clean-up completed."
