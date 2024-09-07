
import time
from multiprocessing import Process, current_process
from threading import Thread, current_thread
from PIL import Image
import numpy as np
import asyncio
import aiofiles
import cv2
import uuid

# Function to compute sum of squares


def sum_of_squares(n):
    return sum(i * i for i in range(n))

# Function for processing with multiprocessing


def sum_of_squares_process(n):
    print(f"Process {current_process().name} is running...")
    # TODO: Implement the logic to compute sum of squares using processes


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
    print(f"Thread {current_thread().name} is running...")
    # TODO: Implement the logic to compute sum of squares using threads


def compute_in_threads(n, num_threads):
    # TODO: Create multiple threads to perform the task
    threads = []
    for _ in range(num_threads):
        # TODO: call the sum_of_squares_threaded function in a new thread
        # TODO: append the thread to the threads list
        # TODO: start the thread
        pass  # Remove this line after implementing the logic

    # TODO: Wait for all threads to complete. Hint: use the join method on each thread


def convert_to_grayscale(image_path, num_blocks):
    # Open the image file
    image = Image.open(image_path)
    width, height = image.size

    # Calculate the new size that is divisible by the number of blocks
    new_width = (width // num_blocks) * num_blocks
    new_height = (height // num_blocks) * num_blocks
    image = image.resize((new_width, new_height))

    # Convert image to numpy array
    pixels = np.array(image)

    # Convert to grayscale using a single-threaded approach
    start_time = time.time()
    grayscale_pixels = np.zeros_like(pixels)

    # TODO: Convert the image to grayscale using a single-threaded approach
    # TODO: 1. Iterate over each pixel in the image using two nested loops
    # TODO: 2. Compute the grayscale value for each pixel using the formula: (0.299 * R + 0.587 * G + 0.114 * B)
    # TODO: 3. Set the grayscale value for each channel (R, G, B) to the computed value

    # Create grayscale image
    grayscale_image = Image.fromarray(grayscale_pixels)
    # Create GUID for the image
    image_guid = uuid.uuid4()
    # Append to image name to avoid overwriting
    grayscale_image.save(f'grayscale_single_threaded_{image_guid}.png')
    print(
        f"Single-threaded conversion done in {time.time() - start_time:.2f} seconds")


def multi_threaded_grayscale(image_path, num_blocks):
    # Open the image file
    image = Image.open(image_path)
    width, height = image.size

    # Calculate the new size that is divisible by the number of blocks
    new_width = (width // num_blocks) * num_blocks
    new_height = (height // num_blocks) * num_blocks
    image = image.resize((new_width, new_height))

    # Convert image to numpy array
    pixels = np.array(image)
    grayscale_pixels = np.zeros_like(pixels)

    # Inner function to convert a block of the image to grayscale
    def process_block(start_row, end_row):
        # TODO: Implement the logic to convert a block of the image to grayscale
        # TODO: 1. Get the RGB values of the pixel at position (i, j)
        # TODO: 2. Compute the grayscale value for each pixel using the formula: (0.299 * R + 0.587 * G + 0.114 * B)
        # TODO: 3. Set the grayscale value for each channel (R, G, B) to the computed value
        pass  # Remove this line after implementing the logic

    # TODO: Divide the image into blocks
    block_size = new_height // num_blocks
    threads = []

    # TODO: Create and start threads for each block
    start_time = time.time()
    for i in range(num_blocks):
        start_row = i * block_size
        end_row = (i + 1) * block_size
        # TODO: call the process_block function with the appropriate arguments in a new thread
        # TODO: append the thread to the threads list
        # TODO: start the thread

    # TODO: Wait for all threads to complete. Hint: use the join method on each thread

    # Save the multi-threaded grayscale image
    grayscale_image = Image.fromarray(grayscale_pixels)
    # Create GUID for the image
    image_guid = uuid.uuid4()
    # Append to image name to avoid overwriting
    grayscale_image.save(f'grayscale_multi_threaded_{image_guid}.png')
    print(
        f"Multi-threaded conversion done in {time.time() - start_time:.2f} seconds")


async def async_read_image(image_path):
    # TODO: Use aiofiles to read the image file asynchronously
    print(f"Reading {image_path} asynchronously...")
    content = None
    # TODO: Use aiofiles to read the image file asynchronously

    image_array = np.frombuffer(content, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)  # Decode the image
    return image


async def async_save_image(image, output_path):
    # Use OpenCV to encode the image
    print(f"Saving {output_path} asynchronously...")
    _, encoded_image = cv2.imencode('.png', image)

    # TODO: Use aiofiles to save the image file asynchronously


async def process_image_async(image_path):
    # Asynchronously read the image
    image = await async_read_image(image_path)

    # Perform image processing (convert to grayscale)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # TODO: Asynchronously save the grayscale image

    print("Image processing and saving completed asynchronously.")


def main():
    n = 10**6
    image_path = 'banf.jpg'  # Replace with your actual image path
    num_blocks = 4  # Number of blocks for image processing

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

    # Single-Threaded Grayscale Conversion
    start_time = time.time()
    convert_to_grayscale(image_path, num_blocks)
    print(f"Time taken for single-threaded grayscale conversion: {
          time.time() - start_time:.2f} seconds\n")

    # Multi-Threaded Grayscale Conversion
    start_time = time.time()
    multi_threaded_grayscale(image_path, num_blocks)
    print(f"Time taken for multi-threaded grayscale conversion: {
          time.time() - start_time:.2f} seconds\n")

    # Async image processing task
    asyncio.run(process_image_async(image_path))


if __name__ == "__main__":
    main()
