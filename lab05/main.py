import logstats

def main():
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = logstats.count_levels(log)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))

    with open(path, encoding="utf-8") as log:
        errors = logstats.top_errors(log, 3)

    with open("report.txt", "w", encoding="utf-8") as report:
        report.write(logstats.format_report(counts, errors))

if __name__ == "__main__":
    main()