
import logging
import psutil

# Configure logging to save messages to a file and show them in the terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("system_health.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def check_health(usage, metric):
    if usage >= 90:
        return f"CRITICAL - High {metric} usage"
    elif usage > 80:
        return f"WARNING - Investigate {metric} usage"
    else:
        return f"NORMAL - {metric} is healthy"


def main():
    cpu_usage = psutil.cpu_percent(interval=2)
    memory = psutil.virtual_memory()
    try:
        disk = psutil.disk_usage("C:\\")
    except OSError as error:
        logging.error("Unable to read disk usage: %s", error)
        return

    print("\nSYSTEM HEALTH MONITOR")
    print("=" * 40)

    metrics = [
        ("CPU", cpu_usage),
        ("Memory", memory.percent),
        ("Disk (C:)", disk.percent),
    ]

    statuses = []

    for metric, usage in metrics:
        status = check_health(usage, metric)
        statuses.append(status)

        print(f"{metric} Usage: {usage}%")
        print(f"{metric} Status: {status}")
        print("-" * 40)

        # Save each metric and its status to the log
        if status.startswith("CRITICAL"):
            logging.critical(
                "%s usage: %.1f%% | Status: %s",
                metric, usage, status
            )
        elif status.startswith("WARNING"):
            logging.warning(
                "%s usage: %.1f%% | Status: %s",
                metric, usage, status
            )
        else:
            logging.info(
                "%s usage: %.1f%% | Status: %s",
                metric, usage, status
            )

    if any(status.startswith("CRITICAL") for status in statuses):
        overall_status = "CRITICAL"
    elif any(status.startswith("WARNING") for status in statuses):
        overall_status = "WARNING"
    else:
        overall_status = "NORMAL"

    print("OVERALL SYSTEM STATUS:", overall_status)
    logging.info("Overall system status: %s", overall_status)


if __name__ == "__main__":
    main()