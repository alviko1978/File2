print("Программа объединения нескольких файлов в порядке возрастания строк в них")
def number_string(current_file):
    with open(current_file, "rt", encoding="utf-8") as file:
        n = len(file.readlines())
    d_line = {current_file: n}
    return d_line

d_sum = {}
d_sum.update(number_string("1.txt"))
d_sum.update(number_string("2.txt"))
d = sorted(d_sum.items(), key=lambda x: x[1])
number_string("1.txt")
number_string("2.txt")
def wr_file():
    with open("Result.txt", "wt", encoding="utf-8") as res:
        for key, volume in d:
            name = str(key)
            number = str(volume)
            with open(name, "rt", encoding="utf-8") as f:
                text = f.read()
                res.write(name + "\n")
                res.write(number + "\n")
                res.write(text + "\n")

wr_file()
