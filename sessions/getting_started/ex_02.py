"""Read a file as text."""


def main():
    new_lines = []
    with open('file-from-ken.json', 'r') as fin:
        filedata = fin.readlines()

    for line in filedata:
        new_lines.append(line.replace("launchpad", "10.5.2.1"))

    with open('new-file.json', 'w') as fout:
        for line in new_lines:
            fout.write(line)

        # With list comprehension
        # [fout.write(line) for line in new_lines]


if __name__ == "__main__":
    main()