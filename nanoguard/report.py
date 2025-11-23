def print_report(results):
    if not results:
        print("No issues found. System clean.")
        return

    print("\n=== NanoGuard Report ===\n")

    for item in results:
        print(f"- File: {item['file']}")
        print(f"  Issue: {item['type']}")
        print(f"  Count: {item['count']}\n")

    print("Scan complete.")
