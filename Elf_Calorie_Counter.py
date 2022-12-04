import os.path
import sys

# Setup variables for future computation.
elf_calorie_count = []
current_elf_calories = 0
filepath = "Resources\\Elf_Calorie_Count.txt"

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File could not be found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

for line in lines:
    # When we see whitespace we are done with that elf, add their total to the array.
    if line in ['\n', '\r\n']:
        elf_calorie_count.append(current_elf_calories)
        current_elf_calories = 0
    # No whitespace means we need to add the current item's calories to the total number of calories for the current elf.
    else:
        current_elf_calories += int(line)

file.close()

# Reverse sort so we know that the first position has the highest number of calories, second position has the second highest and so on.
elf_calorie_count.sort(reverse=True)

# Day 1, Part 1 Solution.
print("Calorie count for the elf with the most calories: " + str(elf_calorie_count[0]))

# Day 1, Part 2 Solution.
print("Calorie count for the top three elves: " + str(elf_calorie_count[0] + elf_calorie_count[1] + elf_calorie_count[2]))
