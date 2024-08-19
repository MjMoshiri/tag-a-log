import argparse
import logging
import csv
from .parser import parse_destination_port_and_protocol
from .table_loader import create_lookup_table, create_protocol_map
from .process import count_port_protocol, count_tags, generate_report
def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Process log files and generate reports.')
    parser.add_argument('log_file', help='Path to the log file')
    parser.add_argument('--protocol_map', default='data/protocol_map.txt', help='Path to the protocol map file (default: data/protocol_map.txt)')
    parser.add_argument('--lookup_table', default='data/lookup_table.txt', help='Path to the lookup table file (default: data/lookup_table.txt)')
    parser.add_argument('--output', default='', help='Path to the output report file (default: results/<log_file>_report.txt)')
    return parser.parse_args()

def process_log_file(log_file, protocol_mapping_file, lookup_table_file, output):
    """
    Process the log file and generate a report.
    
    Parameters:
        log_file (str): Path to the log file.
        protocol_mapping_file (str): Path to the protocol mapping file which maps protocol codes to names.
        lookup_table_file (str): Path to the lookup table file which maps destination ports and protocols to tags.
        output (str): Path to the output report file.
    """
    try:
        protocol_names = create_protocol_map(protocol_mapping_file)
        lookup_table= create_lookup_table(lookup_table_file)
        logs_info = parse_destination_port_and_protocol(log_file)
        ports_protocols_counts = count_port_protocol(logs_info, protocol_names)
        tags_counts = count_tags(ports_protocols_counts, lookup_table)
        generate_report(tags_counts, ports_protocols_counts, output)
    except FileNotFoundError as e:
        logging.error(e)
    except csv.Error as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)

def main():
    args = parse_arguments()
    if not args.output:
        args.output = 'results/' + args.log_file.split('/')[-1].split('.')[0] + '_report.txt'
    process_log_file(args.log_file, args.protocol_map, args.lookup_table, args.output)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()