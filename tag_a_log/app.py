from .parser import parse_destination_port_and_protocol
from .table_loader import create_lookup_table,create_protocol_map
from .process import count_port_protocol,count_tags, generate_report
def main():
    protocol_names = create_protocol_map('data/protocol_map.txt') 
    lookup_table = create_lookup_table('data/lookup_table.txt')
    logs_info = parse_destination_port_and_protocol('data/logs.txt')
    ports_protocols_counts = count_port_protocol(logs_info, protocol_names) 
    tags_counts = count_tags(ports_protocols_counts, lookup_table)
    generate_report(tags_counts, ports_protocols_counts, 'results/report.txt')

    



if __name__ == '__main__':
    main()

