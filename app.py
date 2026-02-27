import sys
import matplotlib.pyplot as plt
from data import execution_time_gathering
def print_results(table):
    print("Size | lineal search (Time, Mem) | binary search (Time, Mem) | ternary search (Time, Mem)")
    for row in table:
        size, lineal_time, binary_time, ternary_time, lineal_mem, binary_mem, ternary_mem = row
        print(f"{size:<5} | [{lineal_time}, {lineal_mem}] | [{binary_time}, {binary_mem}] | [{ternary_time}, {ternary_mem}]")
def print_results_bin_ter(table):
    print("Size | binary search (Time, Mem) | ternary search (Time, Mem)")
    for row in table:
        size,  binary_time, ternary_time,  binary_mem, ternary_mem = row
        print(f"{size:<5} | [{binary_time}, {binary_mem}] | [{ternary_time}, {ternary_mem}]")
def plot_results_bin_ter(table):
    sizes = [row[0] for row in table]
    binary_time = [row[1] for row in table]
    ternary_time = [row[2] for row in table]
    binary_mem = [row[3] for row in table]
    ternary_mem = [row[4] for row in table]

    # Gráfico de tiempos de ejecución
    plt.figure(figsize=(10,5))
    plt.plot(sizes, binary_time, marker='s', label='binary search')
    plt.plot(sizes, ternary_time, marker='^', label='ternary search')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Execution Time of Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

    # Gráfico de uso de memoria
    plt.figure(figsize=(10,5))
    plt.plot(sizes, binary_mem, marker='s', label='binary search')
    plt.plot(sizes, ternary_mem, marker='^', label='ternary search')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Memory Usage of Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

def plot_results(table):
    sizes = [row[0] for row in table]
    lineal_time = [row[1] for row in table]
    binary_time = [row[2] for row in table]
    ternary_time = [row[3] for row in table]
    lineal_mem = [row[4] for row in table]
    binary_mem = [row[5] for row in table]
    ternary_mem = [row[6] for row in table]

    # Gráfico de tiempos de ejecución
    plt.figure(figsize=(10,5))
    plt.plot(sizes, lineal_time, marker='o', label='lineal search')
    plt.plot(sizes, binary_time, marker='s', label='binary search')
    plt.plot(sizes, ternary_time, marker='^', label='ternary search')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Execution Time of Search Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

    # Gráfico de uso de memoria
    plt.figure(figsize=(10,5))
    plt.plot(sizes, lineal_mem, marker='o', label='lineal search')
    plt.plot(sizes, binary_mem, marker='s', label='binary search')
    plt.plot(sizes, ternary_mem, marker='^', label='ternary search')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Memory Usage of Search Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    minimum_size = 10000000
    maximum_size = 50000000
    step = 7000000
    samples_by_size = 7
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print("Size | lineal search | Binary search | Ternary search")
    print_results(table)
    plot_results(table)

    table2 = execution_time_gathering.take_execution_time_bin_ter(minimum_size, maximum_size, step, samples_by_size)
    print("Binary Search vs Ternary Search")
    print("Size | Binary search | Ternary search")
    print_results_bin_ter(table2)
    plot_results_bin_ter(table2)