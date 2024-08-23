from typing import Generator, List
from collections import defaultdict
import os

def count_metrics(logs_info: Generator, protocol_names: List) -> defaultdict:
    """
    Count the number of logs for each destination port, protocol, source, and destination combination.

    Parameters:
        logs_info (Generator[Tuple[int, int, int, int]]): A generator of tuples with the destination port, protocol, source, and destination.
        protocol_names (List[str]): A list of protocol names indexed by protocol number.
        
    Returns:
        Tuple[defaultdict[tuple[int, str], int], defaultdict[tuple[int, int, int, str], int]]: 
        A tuple of two defaultdicts:
            - The first defaultdict has the destination port and protocol as the key and the count as the value.
            - The second defaultdict has the source, destination, port, and protocol as the key and the count as the value.
    """
    port_protocol_count = defaultdict(int)
    src_dst_count = defaultdict(int)
    for port, protocol , src, des in logs_info:
        port_protocol_count[(port, protocol_names[protocol])] += 1
        src_dst_count[(src, des, port, protocol_names[protocol])] += 1
    return port_protocol_count , src_dst_count

def count_tags(port_protocol_dict: defaultdict, lookup_table: defaultdict) -> defaultdict:
    """
    Count the number of logs for each tag.

    Parameters:
        port_protocol_dict (defaultdict[tuple[int, str], int]): A defaultdict with the destination port and protocol as the key and the count as the value.
        lookup_table (defaultdict[tuple[int, str], str]): A defaultdict with the destination port and protocol as the key and the tag as the value.

    Returns:
        defaultdict[str, int]: A defaultdict with the tag as the key and the count as the value.
    """
    tag_count = defaultdict(int)
    for (port, protocol), count in port_protocol_dict.items():
        tag = lookup_table[(port, protocol)]
        tag_count[tag] += count
    return tag_count

def generate_report(tags_counts: defaultdict, port_protocol_counts: defaultdict, src_dst_counts: defaultdict, report_file: str):
    """
    Generate a report with the tag counts and port/protocol counts.

    Parameters:
        tags_counts (defaultdict[str, int]): A defaultdict with the tag as the key and the count as the value.
        port_protocol_counts (defaultdict[tuple[int, str], int]): A defaultdict with the destination port and protocol as the key and the count as the value.
        report_file (str): The path to the file where the report will be saved.
    """
    os.makedirs(os.path.dirname(report_file), exist_ok=True)
    with open(report_file, "w") as report:
        report.write("Tag Counts:\n")
        report.write("Tag,Count\n")
        for tag, count in tags_counts.items():
            report.write(f"{tag},{count}\n")
        report.write("\n")
        report.write("Port/Protocol Combination Counts:\n")
        report.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            report.write(f"{port},{protocol},{count}\n")
        report.write("\n")
        report.write("Source/Destination Counts:\n")
        report.write("Source,Destination,Port,Protocol,Count\n")
        for (src, des, port, protocol), count in src_dst_counts.items():
            report.write(f"{src},{des},{port},{protocol},{count}\n")
        report.write("\n")