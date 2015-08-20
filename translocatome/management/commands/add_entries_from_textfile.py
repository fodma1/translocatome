from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from translocatome.consts import field_name_to_index
from translocatome.models import Node, Interaction, Meta

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    option_list = BaseCommand.option_list + (
        make_option('--input_file_name'),
    )

    @staticmethod
    def parse_line(line):
        return line.strip().split('\t')

    @staticmethod
    def convert_line_to_data(line):
        data = {}
        for i in range(len(line)):
            data[field_name_to_index[i]] = line[i]
        return data

    def handle(self, *args, **options):
        file_name = options['input_file_name']

        with open(file_name, 'r') as input_file:
            self.parse_line(input_file.readline())

            for i in range(15):
                line = self.parse_line(input_file.readline())
                data = self.convert_line_to_data(line)

                source_uniprot_ac = data['Source_UniProtAC']
                source_gene_name = data['Source_GeneName']

                source_node = Node.create_if_not_exists(source_uniprot_ac, source_gene_name)

                print source_node

