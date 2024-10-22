# 0x03-log_parsing 
 


## Read Input:
 The script reads lines from standard input (stdin) that follow a specific format with an IP address, date, request type, status code, and file size.

## Process Lines:

 For every valid line, it extracts the file size and status code.

## Count and Sum:
 It keeps a running total of file sizes and counts occurrences of each status code (200, 301, 400, 401, 403, 404, 405, 500).

## Print Statistics:

 After every 10 lines or when interrupted (with CTRL + C), it prints:

The total file size so far.
The number of occurrences of each status code (only if it has been seen).

## Output Format:

 The status codes are printed in ascending order, and only those that appear at least once are shown.

Ignore Invalid Lines: Any line not matching the expected format is skipped.

