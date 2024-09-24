import multiprocessing
import os
import time

# Part 1: Interprocess Communication (IPC)

# Interprocess Communication using a Pipe


def process_with_pipe(pipe, message):
    # TODO: Add code to send a message through the pipe
    pass


def process_with_pipe_receiver(pipe):
    # TODO: Add code to receive a message from the pipe
    pass

# Interprocess Communication using a Queue


def process_with_queue(queue, message):
    # TODO: Add code to send a message to the queue
    pass


def process_with_queue_receiver(queue):
    # TODO: Add code to receive a message from the queue
    pass

# Part 2: Scheduling Algorithms

# First Come First Serve (FCFS) Scheduling


def fcfs_scheduling(processes):
    print("\nFirst Come First Serve Scheduling")
    # TODO: Implement the FCFS algorithm and calculate waiting and turnaround times
    pass

# Shortest Job Next (SJN) Scheduling


def sjn_scheduling(processes):
    print("\nShortest Job Next Scheduling")
    # TODO: Implement the SJN algorithm and calculate waiting and turnaround times
    pass

# Round Robin (RR) Scheduling


def round_robin_scheduling(processes, quantum):
    print("\nRound Robin Scheduling")
    # TODO: Implement the Round Robin algorithm and calculate waiting and turnaround times
    pass

# Scheduling Scenario


def scheduling_scenario():
    print("\n--- Scheduling Scenario ---")
    print("Scenario: The university's main server is overloaded with several tasks arriving at different times.")
    print("You, as the system administrator, need to schedule the execution of the following tasks:\n")

    print("1. A critical database backup operation, which will take 6 units of time (Process P1).\n"
          "2. A routine data synchronization task, which will take 8 units of time (Process P2).\n"
          "3. A quick maintenance script that should run as soon as possible, expected to take 3 units of time (Process P3).\n"
          "4. A large report generation that is expected to take 7 units of time (Process P4).\n")

    print("Propose the best scheduling algorithm to minimize waiting time and ensure critical tasks don't get delayed.\n")

    print("**Challenge:** The critical database backup (P1) is time-sensitive and must be executed at least once every 5 units of time. "
          "Modify the scheduling approach to meet this new constraint.\n")

    processes = [("P1", 0, 6), ("P2", 1, 8), ("P3", 2, 3), ("P4", 3, 7)]

    print("Process Table:")
    print("Process    Arrival Time    Burst Time")
    for process in processes:
        print(f"{process[0]}         {process[1]}              {process[2]}")

    print("\nYou will implement and test your proposed solution. Then, modify the code to handle the additional challenge.\n")


if __name__ == "__main__":
    # Interprocess Communication Part with Pipe
    print("Interprocess Communication using Pipe:")
    parent_conn, child_conn = multiprocessing.Pipe()

    process_sender = multiprocessing.Process(
        target=process_with_pipe, args=(parent_conn, "Hello from child process!",))
    process_receiver = multiprocessing.Process(
        target=process_with_pipe_receiver, args=(child_conn,))

    # TODO: Start and join the sender and receiver processes for Pipe-based IPC

    print("\nInterprocess Communication via Pipe Completed\n")

    # Interprocess Communication Part with Queue
    print("Interprocess Communication using Queue:")
    message_queue = multiprocessing.Queue()

    process_sender_q = multiprocessing.Process(
        target=process_with_queue, args=(message_queue, "Hello from queue!",))
    process_receiver_q = multiprocessing.Process(
        target=process_with_queue_receiver, args=(message_queue,))

    # TODO: Start and join the sender and receiver processes for Queue-based IPC

    print("\nInterprocess Communication via Queue Completed\n")

    # Scenario-based Scheduling
    scheduling_scenario()

    # Scheduling Algorithms Part
    processes = [("P1", 0, 6), ("P2", 1, 8), ("P3", 2, 3), ("P4", 3, 7)]
    quantum = 2

    print("\n--- Test Your Proposed Scheduling Algorithm Here ---")

    # TODO: Uncomment and test the scheduling algorithms based on the scenario

    # fcfs_scheduling(processes)
    # sjn_scheduling(processes)
    # round_robin_scheduling(processes, quantum)

    print("\nModify the code to handle the challenge of ensuring the critical backup task is run every 5 units of time.")
