# PIE TIME (EASY)

## What's this challenge about?

This challenge asks you to work with a special kind of program called a Position Independent Executable (PIE). Because PIE is enabled, the program's memory addresses change every time it runs. Your goal is to figure out the *current* address of a hidden function called `win()` and send that address back to the server to get the flag.

## How to solve it

We've created a Python script, [`win_addr.py`](win_addr.py), that does the heavy lifting for you. It automatically figures out the `win()` function's address and sends it off.

### How the script works

Here's a breakdown of what the Python script does:

1.  **Connects:** It connects to the challenge server running on the network.
2.  **Finds `main()`:** It reads the server's welcome message to find the current memory address of the `main()` function.
3.  **Calculates Base Address:** Using the known, fixed offset of `main()` within the program, it calculates the program's base memory address for this specific run.
4.  **Finds `win()`:** Knowing the base address and the fixed offset of the `win()` function, it calculates the exact memory address of `win()`.
5.  **Gets the Flag:** It sends the calculated `win()` address back to the server and prints the response, which should contain the flag!

### What you'll need

*   Python 3
*   The `pwntools` library (you can install it by running `pip install pwntools` in your terminal)

### How to run it

1.  Make sure you have Python 3 and `pwntools` installed.
2.  Open your terminal and run the script like this:
    ```bash
    python3 win_addr.py
    ```

### Example Output

When you run the script successfully, you should see something like this:

*   The address of `main()` that the script found.
*   The calculated base address and the address of `win()`.
*   The server's response after receiving the `win()` address, which hopefully includes the flag!

### Disclaimer

This script and explanation are for educational purposes only. Please make sure you have permission before running this against any system you don't own or have explicit authorization to test.