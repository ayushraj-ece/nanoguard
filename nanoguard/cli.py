import argparse
from .scanner import scan_path
from .report import print_report

def main():
    parser = argparse.ArgumentParser(description="NanoGuard - Smart security scanner")
    parser.add_argument("path", help="Path to scan")
    args = parser.parse_args()

    results = scan_path(args.path)
    print_report(results)
