import multiprocessing
import os
import time
from queue import Queue

# Interprocess Communication using a Pipe


def process_with_pipe(pipe, message):
    print(f"Process {os.getpid()} sending message: {message}")
    pipe.send(message)  # Send the message through the pipe
    pipe.close()  # Close the pipe


def process_with_pipe_receiver(pipe):
    message = pipe.recv()  # Receive the message from the pipe
    print(f"Process {os.getpid()} received message: {message}")

# Scheduling Algorithms Implementation


def fcfs_scheduling(processes):
    print("Running First Come First Serve Scheduling...")
    # TODO: Implement FCFS logic, calculate waiting and turnaround times


def sjn_scheduling(processes):
    print("Running Shortest Job Next Scheduling...")
    # TODO: Implement SJN logic, calculate waiting and turnaround times


def round_robin_scheduling(processes, quantum):
    print(f"Running Round Robin Scheduling with quantum: {quantum}")
    # TODO: Implement Round Robin logic, calculate waiting and turnaround times


if __name__ == "__main__":
    # Interprocess Communication Part
    print("Demonstrating Interprocess Communication using Pipe:")
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create the sender and receiver processes
    process_sender = multiprocessing.Process(
        target=process_with_pipe, args=(parent_conn, "Hello from child process!",))
    process_receiver = multiprocessing.Process(
        target=process_with_pipe_receiver, args=(child_conn,))

    # Start the processes
    process_sender.start()
    process_receiver.start()

    # Wait for the processes to finish
    process_sender.join()
    process_receiver.join()

    print("\nInterprocess Communication via Pipe Completed\n")

    # Scheduling Algorithms Part
    processes = [("P1", 0, 6), ("P2", 1, 8), ("P3", 2, 7), ("P4", 3, 3)]
    quantum = 2

    # Run each scheduling algorithm
    fcfs_scheduling(processes)  # TODO: Add implementation
    sjn_scheduling(processes)   # TODO: Add implementation
    round_robin_scheduling(processes, quantum)  # TODO: Add implementation
