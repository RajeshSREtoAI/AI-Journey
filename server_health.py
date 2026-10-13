
def check_health(usage, metric):
    if usage >= 90:
        return f"CRITICAL - High {metric} usage"
    elif usage > 80:
        return f"WARNING - Investigate {metric} usage"
    else:
        return f"NORMAL - {metric} is healthy"


servers = [
    ("PROD-SERVER-01", 65, 70),
    ("PROD-SERVER-02", 85, 88),
    ("PROD-SERVER-03", 95, 92),
]

for server_name, cpu_usage, memory_usage in servers:
    print("Server:", server_name)
    print("CPU:", cpu_usage, "%")
    print("CPU Status:", check_health(cpu_usage, "CPU"))
    print("Memory:", memory_usage, "%")
    print("Memory Status:", check_health(memory_usage, "memory"))
    print("-" * 35)
