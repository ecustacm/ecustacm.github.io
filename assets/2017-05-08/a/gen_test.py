
with open("in", "w") as f:
    f.write("53\n")
    for i in range(1, 11):
        for j in range(1, 11):
            if i * j <= 25:
                s = "%s %s\n" % (i, j)
                f.write(s)

