def staircase(n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            print("", end=" ")
        for j in range((n + 1) - i):
            print("", end="#")
        print("", end="\n")


if __name__ == '__main__':
    staircase(4)

''' ---- Output ----

       #
      ##
     ###
    ####

'''