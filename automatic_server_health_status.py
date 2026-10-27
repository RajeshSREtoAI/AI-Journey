import psutil
def check_health(usage, metric):
    if usage>= 90:
        return f"CRITICAL - High {metric} usage"
    elif usage > 80:
        return f"WARNING - Investigate {metric} usage"
    else:
        return f"NORMAL - {metric} is healthy"

cpu_usage = psutil.cpu_percent(interval=2)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("C:\\")

print("SYSTEM HEALTH MONITOR")
print("=" * 40)

print(f"CPU Usage: {cpu_usage}%")
print("CPU Status:", check_health(cpu_usage, "CPU"))
print()

print(f"Memory Usage:{memory.percent}%")
print("Memory Status:", check_health(memory.percent, "memory"))
print()

print(f"Disk Usage (C:): {disk.percent}%")
print("Disk Status:", check_health(disk.percent, "disk"))



# Overall system health
if (
    cpu_usage >= 90
    or memory.percent >= 90
    or disk.percent >= 90
):
    overall_status = "CRITICAL"
elif (
    cpu_usage > 80
    or memory.percent > 80
    or disk.percent > 80
):
    overall_status = "WARNING"
else:
    overall_status = "NORMAL"

print()
print("=" * 40)
print("OVERALL SYSTEM STATUS:", overall_status)
