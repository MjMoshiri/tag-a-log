from typing import Dict, Generator, List
from collections import defaultdict
def count_port_protocol(logs_info: Generator, protocol_names: List) -> Dict:
    """
    Count the number of logs for each destination port and protocol combination.

    Parameters:
        logs_info (Generator[List[int]]): A generator of lists with the destination port and protocol.
        Returns:
        Dict[tuple[int,int], int]: A dictionary with the destination port and protocol as the key and the count as the value.
    """
    port_protocol_count = defaultdict(int)
    for port, protocol in logs_info:
        port_protocol_count[(port, protocol_names[protocol])] += 1
    return port_protocol_count

def count_tags(port_protocol_dict: Dict, lookup_table: Dict) -> Dict:
    """
    Count the number of logs for each tag.

    Parameters:
        port_protocol_dict (Dict[tuple[int, str], int]): A dictionary with the destination port and protocol as the key and the count as the value.
        lookup_table (Dict[tuple[int, str], str]): A dictionary with the destination port and protocol as the key and the tag as the value.

    Returns:
        Dict[str, int]: A dictionary with the tag as the key and the count as the value.
    """
    tag_count = defaultdict(int)
    for (port, protocol), count in port_protocol_dict.items():
        tag = lookup_table.get((port, protocol), "UNTAGGED")
        tag_count[tag] += count
    return tag_count

def generate_report(tags_counts: Dict, port_protocol_counts: Dict, report_file: str):
    """
    Generate a report with the tag counts and port/protocol counts.

    Parameters:
        tags_counts (Dict[str, int]): A dictionary with the tag as the key and the count as the value.
        port_protocol_counts (Dict[tuple[int, str], int]): A dictionary with the destination port and protocol as the key and the count as the value.
        report_file (str): The path to the file where the report will be saved.
    """
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