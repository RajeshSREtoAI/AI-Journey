# psutil load the monitoring library 
# psutil.virtual_memory() reads real RAM statistics.
# psutil.disk_usage("C:\\") reads usage statistics for your C: drive.
# memory.percent and disk.percent provide the utilization percentages.
# f"..." is a Python f-string, which inserts variable values directly into text.

import psutil
cpu_usage = psutil.cpu_percent(interval=2)
# measures actual CPU utilization over a two second intervals.
memory = psutil.virtual_memory()
disk = psutil.disk_usage("C:\\")
print("System Health Monitor")
print("=" * 30)
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory.percent}%")
print(f"Disk Usage (C:): {disk.percent}%")