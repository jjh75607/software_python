import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

# file1
file = open(file1, 'w')
file.write('this is file1\n')
file.close()

file = open(file1, 'r')
file1_content = file.read()
file.close()

# file2
file = open(file2, 'w')
file.write('this is file2\n')
file.close()

file = open(file2, 'r')
file2_content = file.read()
file.close()

# file3
file = open(file3, 'w')
file.write(file1_content + file2_content)
file.close()