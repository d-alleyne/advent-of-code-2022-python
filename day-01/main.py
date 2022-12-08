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

