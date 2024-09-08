
import time
from multiprocessing import Process, current_process
from threading import Thread, current_thread
import numpy as np

# Function to compute sum of squares


def sum_of_squares(n):
    return sum(i * i for i in range(n))

# Function for processing with multiprocessing


def sum_of_squares_process(n):
    # TODO: Print the name and PID of the current process with a prompt message that the process has started.
    # TODO: Implement the logic to compute sum of squares using multiple processes
    # TODO: print the name and PID of the current process with a prompt message the the process has finished.
    pass  # Remove this line after implementing the logic


def compute_in_processes(n, num_processes):
    # TODO: Create multiple processes to perform the task
    processes = []
    for _ in range(num_processes):
        # TODO: Create a new process with the target function sum_of_squares_process
        # TODO: Append the process to the processes list
        # TODO: Start the process
        pass  # Remove this line after implementing the logic

    # TODO: Wait for all processes to complete. Hint: use the join method on each process


# Function for threading


def sum_of_squares_threaded(n):
    # TODO: Print the name of the current thread with a prompt message that the thread has started.
    # TODO: Implement the logic to compute sum of squares using threads
    # TODO: print the name of the current thread with a prompt message that the thread has finished.
    pass  # Remove this line after implementing the logic


def compute_in_threads(n, num_threads):
    # TODO: Create multiple threads to perform the task
    threads = []
    for _ in range(num_threads):
        # TODO: call the sum_of_squares_threaded function in a new thread
        # TODO: append the thread to the threads list
        # TODO: start the thread
        pass  # Remove this line after implementing the logic

    # TODO: Wait for all threads to complete. Hint: use the join method on each thread


def main():
    n = 10**6

    # Sequential Execution
    start_time = time.time()
    result = sum_of_squares(n)
    print(f"Sequential Result: {result}")
    print(f"Time taken (sequential): {time.time() - start_time:.2f} seconds\n")

    # Parallel Execution with Processes
    num_processes = 4
    start_time = time.time()
    compute_in_processes(n, num_processes)
    print(f"Time taken with processes: {
          time.time() - start_time:.2f} seconds\n")

    # Parallel Execution with Threads
    num_threads = 4
    start_time = time.time()
    compute_in_threads(n, num_threads)
    print(f"Time taken with threads: {time.time() - start_time:.2f} seconds\n")


if __name__ == "__main__":
    main()
