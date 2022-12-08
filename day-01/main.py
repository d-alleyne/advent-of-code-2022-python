if __name__ == "__main__":
    # open a file named "input.txt" for read-only mode
    with open("input.txt", "r") as f:
        elf_array = f.read().splitlines()
        elf = [0]
        elf_number = 0
        for i in range(len(elf_array)):
            if elf_array[i] != "":
                elf[elf_number] = elf[elf_number] + int(elf_array[i])
            else:
                elf_number += 1
                elf.append(0)

        elf_with_most = max(elf)
        elf_number = elf.index(elf_with_most)
        print("Elf number", elf_number + 1, "has the most calories with", elf_with_most, "calories.")

        # find the top 3 values of elf array
        top_3 = sorted(elf, reverse=True)[:3]
        # Display the top 3 values and their sum
        print("The top 3 elves have", top_3[0], "calories,", top_3[1], "calories, and", top_3[2], "calories, for a "
                                                                                                  "total of",
              sum(top_3), "calories.")
