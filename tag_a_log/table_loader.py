import csv
from typing import Dict
from collections import defaultdict
from .utils import wrap_with_try_csv


@wrap_with_try_csv
def create_lookup_table(filename: str) -> defaultdict:
    """
    Read a lookup table file with destination port, protocol, and tag columns.

    Parameters:
        filename (str): The path to the file containing the lookup table.

    Returns:
        defaultdict[tuple[int, str], str]: A defaultdict with the destination port and protocol as the key and the tag as the value.

    Example:
        The function expects a file with comma-separated values like the following:
        dstport,protocol,tag
        25,tcp,sv_P1
        68,udp,sv_P2
        23,tcp,sv_P1
        31,udp,SV_P3
        443,tcp,sv_P2
        22,tcp,sv_P4
        3389,tcp,sv_P5
        0,icmp,sv_P5
        110,tcp,email
        993,tcp,email
        143,tcp,email
    """
    lookup_table = defaultdict(lambda: "UNTAGGED")
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 3:
                lookup_table[(int(row[0]), row[1].upper())] = row[2].upper()
            else:
                # TODO: Log a warning for rows with missing columns.
                pass
    return lookup_table

@wrap_with_try_csv
def create_protocol_map(filename: str) -> defaultdict:
    """
    Read a protocol map file with protocol code and the corresponding name.

    Parameters:
        filename (str): The path to the file containing the lookup table.

    Returns:
        defaultdict[int, str]: A defaultdict with the protocol code as the key and the protocol name as the value.

    Example:
        The function expects a file with comma-separated values like the following:
        protocol,tag
        1,icmp
        6,tcp
        17,udp
    """
    protocol_list = defaultdict(lambda: "UNKNOWN_PROTOCOL")
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) > 1:
                protocol_list[int(row[0])] = row[1].upper()
            else:
                # TODO: Log a warning for rows with missing columns.
                pass
    return protocol_list
        