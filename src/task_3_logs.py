from collections import Counter
from typing import Iterator

class LogRecord:
    date: str
    time: str
    level: str
    message: str

    def __init__(self, date: str, time: str, level: str, message: str):
        self.date = date
        self.time = time
        self.level = level
        self.message = message

def load_logs(file_path: str) -> list[LogRecord]:
    try:
        with open(file_path, 'r') as file:
            return list(map(lambda line: parse_log_line(line.strip()), file))
    except FileNotFoundError:
        print('File not found!')
        return []

def parse_log_line(line: str) -> LogRecord:
    date, time, level, message = line.split(' ', 3)
    return LogRecord(date, time, level, message)

def filter_logs_by_level(logs: list[LogRecord], level: str) -> list[LogRecord]:
    return list(filter(lambda log: log.level.lower() == level.lower(), logs))

def count_logs_by_level(logs: list[LogRecord]) -> dict:
    return Counter(log.level for log in logs)

def display_log_counts(counts: dict):
    col_1_header = "Log level"
    col_2_header = "Count"
    max_1_col_len = max([
        len(col_1_header),
        *list(map(lambda key: len(key), list(counts.keys())))
    ])
    max_2_col_len = max([
        len(col_2_header),
        *map(lambda key: len(str(key)), list(counts.values()))
    ])
    print(f"{col_1_header} | {col_2_header}")
    print(f"{"-"*max_1_col_len} | {"-"*max_2_col_len}")
    for level, count in counts.items():
        print(f"{level}{" "*(max_1_col_len - len(level))} | {" "*(max_2_col_len - len(str(count)))}{count}")

path = "./logs.txt"
logs = load_logs(path)

filtered_logs = filter_logs_by_level(logs, "debug")
print()
for log in filtered_logs:
    print(log.date, log.time, log.level, log.message)

log_counts = count_logs_by_level(logs)
display_log_counts(log_counts)

