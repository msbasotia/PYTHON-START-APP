f_lines = open("sample_lines.txt", "r")
file_contents_lines = f_lines.read()

records_lines = file_contents_lines.split("\n")

print(records_lines)


f_words = open("sample_words.txt", "r")
file_contents_words = f_words.read()

records_words = file_contents_words.split(" ")

print(records_words)


f_names = open("sample_names.csv", "r")
file_contents_names = f_names.read()

records_names = file_contents_names.split(",")

print(records_names)