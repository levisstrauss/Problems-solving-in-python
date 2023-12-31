"""
Given an array, colors, which contains a combination
of the following three elements:

    - 0 (Representing red)
    - 1 (Representing white)
    - 2 (Representing blue)

Sort the array in place so that the elements of the same
color are adjacent, with the colors in the order of red, white, and blue.

Note: The function should only return the modified colors array.

The time complexity here is O(N) and the space complexity is O(1).

Note:

    Set th fast and slow pointers to the head of the linked list.
    Traverse the linked list by moving the slow pointer one node forward
    and the fast pointer two nodes forward. Once the fast pointer reaches
    the last node, the slow pointer has reached the middle of the linked list.

"""


def sort_colors(colors):
    # Initialize the red, white, and blue pointers
    red, white, blue = 0, 0, len(colors) - 1

    while white <= blue:
        # If the white pointer is pointing to red
        if colors[white] == 0:
            # Swap the values if the red pointer is not pointing to red
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]

            # Increment both the red and white pointers
            white += 1
            red += 1

        # If the white pointer is pointing to white, no swapping is required
        # Just increment the white pointer
        elif colors[white] == 1:
            white += 1

        # If the white pointer is pointing to blue
        else:
            # Swap the values if the blue pointer is not pointing to blue
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]

            # Decrement the blue pointer
            blue -= 1

    return colors


# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        print(i + 1, ".\tcolors:", inputs[i].copy(),
              "\n\n\tThe sorted array is:", sort_colors(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()