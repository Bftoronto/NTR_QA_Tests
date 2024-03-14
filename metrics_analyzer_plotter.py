import matplotlib.pyplot as plt

def analyze_metrics(metrics):
    cpu_values = []
    mem_values = []

    for metric in metrics:
        # Добавьте значения процессора и памяти в соответствующие списки
        cpu_values.append(cpu_value)
        mem_values.append(mem_value)


    if any(condition for condition in your_criteria):
        return "FAIL"
    else:
        return "PASS"

def plot_metrics(metrics):
    cpu_values = []
    mem_values = []
    time_values = []

    for metric in metrics:
        # Добавьте значения процессора, памяти и времени в соответствующие списки
        cpu_values.append(cpu_value)
        mem_values.append(mem_value)
        time_values.append(time_value)

    # График потребления памяти с течением времени
    plt.figure(1)
    plt.plot(time_values, mem_values)
    plt.xlabel('Time')
    plt.ylabel('Memory Consumption')
    plt.title('Memory Consumption over Time')

    # График использования процессора с течением времени
    plt.figure(2)
    plt.plot(time_values, cpu_values)
    plt.xlabel('Time')
    plt.ylabel('CPU Usage')
    plt.title('CPU Usage over Time')

    plt.show()