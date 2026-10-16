import logstats

path = input("Введите имя файла:")
report_text = ""
with open(path, encoding = "utf-8") as f:
    levels_with_count = logstats.count_levels(f.readlines())
    count_of_parsed_strings = levels_with_count["BROKEN"] + levels_with_count["DEBUG"] + levels_with_count["INFO"] + levels_with_count["WARNING"] + levels_with_count["ERROR"]
    report_text = f"{count_of_parsed_strings}\n{levels_with_count['ERROR']}\n{levels_with_count['BROKEN']}"

with open("report.txt", "w", encoding = "utf-8") as f:
    f.write(report_text)

