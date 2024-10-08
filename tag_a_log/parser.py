import csv
from typing import Generator
from .utils import wrap_with_try_csv


DES_PORT_INDEX = 6
PROTOCOL_INDEX = 7
SRC_IP_INDEX = 3
DST_IP_INDEX = 4
@wrap_with_try_csv
def parse_log_cols(filename: str) -> Generator:
    """
    Read flow log data from a space-separated file without a header using a generator to handle large files.

    Parameters:
        filename (str): The path to the file containing flow logs.

    Yields:
        list[int]: A list containing the destination port, protocol, source IP, and destination IP.

    Example:
        The function expects a file with space-separated values like the following:
        2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
        - The 4th column (10.0.1.201) represents the source IP.
        - The 5th column (198.51.100.2) represents the destination IP.
        - The 7th column (49153) represents the destination port.
        - The 8th column (6) represents the protocol.
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if len(row) > PROTOCOL_INDEX:
                yield [int(row[DES_PORT_INDEX]), int(row[PROTOCOL_INDEX]), row[SRC_IP_INDEX], row[DST_IP_INDEX]]
            else:
                # TODO: Log a warning for rows with missing columns.
                pass
        