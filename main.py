import sys
from stats import recipt,words,count_Characters


file_path = sys.argv[1]
a = words(file_path)
b = count_Characters(file_path)


if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)



print(a)
print(recipt())