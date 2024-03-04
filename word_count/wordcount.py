# Word Count
import os
import multiprocessing

def mapper(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

def reducer(word_counts):
    final_word_count = {}
    for word_count in word_counts:
        for word, count in word_count.items():
            final_word_count[word] = final_word_count.get(word, 0) + count
    return final_word_count

def main():
    # List all text files in the directory
    files = [f for f in os.listdir() if f.endswith('.txt')]

    # Define the number of processes
    num_processes = multiprocessing.cpu_count()

    # Ensure at least one file per process
    files_per_process = max(1, len(files) // num_processes)

    # Divide files among processes
    file_chunks = [files[i:i+files_per_process] for i in range(0, len(files), files_per_process)]

    # Create and start processes
    processes = []
    for chunk in file_chunks:
        p = multiprocessing.Process(target=worker, args=(chunk,))
        processes.append(p)
        p.start()

    # Join processes
    for p in processes:
        p.join()

    print("All processes finished.")


def worker(files):
    word_counts = []
    for file in files:
        word_counts.append(mapper(file))
    result = reducer(word_counts)
    print(result)

if __name__ == "__main__":
    main()
