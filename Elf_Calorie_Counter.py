# Setup variables for future computation.
elf_calorie_count = []
current_elf_calories = 0

# Open file and read it in line by line.
file = open("Resources\\Elf_Calorie_Count.txt", "r")
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
