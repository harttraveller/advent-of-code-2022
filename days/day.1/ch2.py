def main():
    data = [
        sum([int(x) for x in elf.split("\n") if x != ""])
        for elf in open("input.txt").read().split("\n\n")
    ]
    data.sort(reverse=True)
    return sum(data[:3])


if __name__ == "__main__":
    print(main())
