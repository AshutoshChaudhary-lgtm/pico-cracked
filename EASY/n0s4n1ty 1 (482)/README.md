# n0s4n1ty 1 (Easy) 482

## Description
This challenge involves exploiting a PHP web shell to execute arbitrary commands on the server. The provided PHP script accepts a `cmd` parameter via a GET request and executes it on the server.

## Solution
The solution is implemented in the [`shell.php`](shell.php) file. This script allows users to pass system commands through the URL and execute them on the server.

### Code Explanation
The PHP script performs the following steps:
1. Checks if the `cmd` parameter is present in the query string.
2. Retrieves the value of the `cmd` parameter.
3. Executes the command using the `system()` function.
4. Displays the output in a preformatted text block.

### Usage
1. Host the `shell.php` file on a web server.
2. Access the shell via a browser or a tool like `curl`:
    ```bash
    curl "http://<server_address>/shell.php?cmd=<command>"
    ```
    Replace `<server_address>` with the server's address and `<command>` with the desired command to execute.

#### Example
To list files in the server's directory:
```bash
curl "http://<server_address>/shell.php?cmd=ls"
```

### Disclaimer
This solution is provided for educational purposes only. Ensure you have proper authorization before testing or deploying this script.