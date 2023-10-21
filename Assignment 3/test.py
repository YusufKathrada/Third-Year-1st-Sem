import array


def OPT(pg, fn):
    """
    Function to find the optimal page replacement
    using the optimal page replacement algorithm
    """
    # Create an array for given number of
    # frames and initialize it as empty.
    fr = array.array('i', [-1] * fn)
    pn = len(pg)

    # Traverse through page reference array
    # and check for miss and hit.
    hit = 0
    for i in range(pn):
        # Page found in a frame : HIT
        found = False
        for j in range(fn):
            if fr[j] == pg[i]:
                hit += 1
                found = True
                break

        if found:
            continue

        # Page not found in a frame : MISS

        # If there is space available in frames.
        emptyFrame = False
        for j in range(fn):
            if fr[j] == -1:
                fr[j] = pg[i]
                emptyFrame = True
                break

        if emptyFrame:
            continue

        # Find the page to be replaced.
        farthest = -1
        replaceIndex = -1
        for j in range(fn):
            k = i + 1
            while (k < pn):
                if fr[j] == pg[k]:
                    if k > farthest:
                        farthest = k
                        replaceIndex = j
                    break
                k += 1
            if k == pn:
                replaceIndex = j
                break
        fr[replaceIndex] = pg[i]

    print("No. of hits =", hit)
    print("No. of misses =", pn - hit)


if __name__ == "__main__":
    pg = [0, 1, 0, 6, 0, 3, 6, 2]
    fn = 3
    OPT(pg, fn)
