# Each Tag Counts
## Overview
### Folder Structure

```
.gitignore
data/
    logs.txt (sample log file)
    lookup_table.txt 
    protocol_map.txt 
README.md
results/
    logs_report.txt (output file)
tag_a_log/
    __init__.py
    app.py (entry point)
    parser.py (extracting data from log files)
    process.py (processing data and generating reports)
    table_loader.py (loading lookup table, and protocol code to name mapping)
    utils.py (helper functions)
```

### Assumptions
- The program is compatible with [flow log version 2](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html). Internally, it uses spaces as delimiters and processes files that do not contain headers. It attempts to parse the **6th** column as `dstport` and the **7th** column as `protocol` (using a 0-based index). To ensure proper functionality, any log file must adhere to these specifications.
- Generally, the program assumes that the files are well-formed and do not contain any errors. It just skips any lines that are empty or do not contain the expected number of columns.

## Installation

No external dependencies are required. The program is written in Python 3.10 but should be compatible with any version of Python 3.

## Usage

### Running the Program
To run the program, navigate to the directory containing the repository and execute the following command to see available options:

```bash
python3 -m tag_a_log.app --help
```

or to run the program with the sample log file:

```bash
python3 -m tag_a_log.app data/logs.txt
```


## DESIGINIG FOR PRODUCTION

- **Log Format Consistency**: It's important to understand the log formats we are receiving and their consistency. This will determine whether it is beneficial to use a more flexible parser like regex.

- **Seperation of Concern**: Data should first be cleaned and then processed by the counter. This will make the code more modular and easier to maintain.

- **Precomputing Lookup Tables**: Depending on the consistency of our requirements and the frequency of function execution, precomputing the lookup table can be advantageous.

- **File Streaming**: The necessity of streaming files depends on their size and needs to be tested.

- **Performance Considerations**: If performance is a critical concern, using a compiled, strongly-typed language like Java or C++ might be more efficient.

- **Testing**: The program should include comprehensive testing to ensure reliability and correctness.

- **Logging**: Proper logging should be implemented to help with debugging and monitoring.

- **Error Handling**: The program should be able to handle errors gracefully and provide meaningful feedback to the user.

- **Configuration**: The program should be configurable to allow for easy changes to parameters like file paths, log formats, etc.