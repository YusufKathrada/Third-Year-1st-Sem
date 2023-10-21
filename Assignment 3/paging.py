# KTHYUS001
# Yusuf Kathrada
# CSC3002F
# OS Assignment 1: Memory Management

# ---------------------------------------
# Important notes:

# Generate random page-refrence string, page numbers range from 0-9, user can input size of page refrence
# Apply to each alg, record num page faults
# page frames can vary from 1-7

# ---------------------------------------


import sys
import array
from random import randrange
from queue import Queue

# Function that generates a random page reference


def random_ref_string(page_ref_size):
    ref_string = []
    for i in range(page_ref_size):
        ref_string.append(randrange(10))
    return ref_string


def FIFO(frame_size, page_ref):

    current_pages = set()

    # store pages in queue (FIFO)
    pages_queue = Queue()

    page_faults = 0

    for i in range(len(page_ref)):

        # If set frame not full
        if (len(current_pages) < frame_size):

            # check that page not in current set already
            if (page_ref[i] not in current_pages):

                current_pages.add(page_ref[i])

                page_faults += 1

                # Add the current page to the queue
                pages_queue.put(page_ref[i])

        # if frame full need to implement FIFO
        else:

            # Check that page not in current set already
            if (page_ref[i] not in current_pages):

                front_val = pages_queue.queue[0]

                # get front/first value in queue
                pages_queue.get()

                # remove value in front of queue
                current_pages.remove(front_val)

                # add new value
                current_pages.add(page_ref[i])

                pages_queue.put(page_ref[i])

                page_faults += 1

    return page_faults


def LRU(frame_size, page_ref):

    current_pages = set()

    # dict to store least recently used page index
    index = {}

    page_faults = 0

    for i in range(len(page_ref)):

        # If set frame not full
        if (len(current_pages) < frame_size):

            # check that page not in current set already
            if (page_ref[i] not in current_pages):

                current_pages.add(page_ref[i])

                page_faults += 1

            # current page index
            index[page_ref[i]] = i

    # if frame full need to implement LRU
        else:
            # Check that page not in current set already
            if (page_ref[i] not in current_pages):

                lru = float('inf')

                for p in current_pages:
                    if (index[p] < lru):
                        lru = index[p]
                        val = p

                current_pages.remove(val)

                current_pages.add(page_ref[i])

                page_faults += 1

        index[page_ref[i]] = i

    return page_faults


def OPT(frame_size, page_ref):
    # int array of frame size
    current_pages = array.array('i', [-1] * frame_size)

    # find when there is a hit, subtract that from len(page_ref) to find page faults
    page_hit = 0

    # check if page in frame
    for i in range(len(page_ref)):
        page_found = False
        for n in range(frame_size):
            if (current_pages[n] == page_ref[i]):
                page_hit += 1
                page_found = True
                break

        if (page_found):
            continue

        # check if frame is full
        empty_fr = False
        for x in range(frame_size):
            if (current_pages[x] == -1):
                current_pages[x] = page_ref[i]
                empty_fr = True
                break

        if (empty_fr):
            continue

        # find replacement page
        far = -1
        replaceInd = -1

        # find farthest page to be used
        for y in range(frame_size):
            counter = i + 1
            while (counter < len(page_ref)):
                if (current_pages[y] == page_ref[counter]):
                    if (counter > far):
                        far = counter
                        replaceInd = y
                    break
                counter += 1
            if (counter == len(page_ref)):
                replaceInd = y
                break
        # replace page at replaceInd
        current_pages[replaceInd] = page_ref[i]

    page_faults = len(page_ref) - page_hit
    return page_faults


def just_for_testing(p):
    list_to_string = ' '.join([str(elem) for elem in p])

    return list_to_string


def main():
    # ...TODO...
    frame_size = int(sys.argv[1])

    # get input from user on the size of the page reference
    page_ref_size = int(input("Enter the page reference size: \n"))
    pages = random_ref_string(page_ref_size)
    print(f"The random page reference of size {page_ref_size} is: {pages}\n")

    # DELETE
    # print(just_for_testing(pages))

    print("FIFO", FIFO(frame_size, pages), "page faults.")
    print("LRU", LRU(frame_size, pages), "page faults.")
    print("OPT", OPT(frame_size, pages), "page faults.")
    # Where size = frame size, pages = page reference


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of page frames]")
    else:
        main()
