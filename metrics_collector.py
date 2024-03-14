import time

def collect_metrics(duration):
    metrics = []
    end_time = time.time() + duration

    while time.time() < end_time:
        metrics.append(get_top_output())
        time.sleep(1)

    return metrics