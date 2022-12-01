def main():
    return max(
        [
            sum([int(x) for x in elf.split("\n") if x != ""])
            for elf in open("ch1.input.txt").read().split("\n\n")
        ]
    )


if __name__ == "__main__":
    print(main())
