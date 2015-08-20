from django.db import models, IntegrityError


class Node(models.Model):
    uni_prot_ac = models.CharField(max_length=50, unique=True)
    gene_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return 'Node:uni_prot_ac<{uni_prot_ac}>, gene_name<{gene_name}>'.format(uni_prot_ac=self.uni_prot_ac, gene_name=self.gene_name)

    @staticmethod
    def get_or_create_node_safely(query_uni_prot_ac, query_gene_name):
        try:
            node = Node.objects.get(uni_prot_ac=query_uni_prot_ac)

            if node.gene_name != query_gene_name:
                raise IntegrityError

            return node

        except Exception:
            pass

        try:
            node = Node.objects.get(gene_name=query_gene_name)

            if node.uni_prot_ac != query_uni_prot_ac:
                raise IntegrityError

            return node

        except Exception:
            pass

        node = Node(uni_prot_ac=query_uni_prot_ac, gene_name=query_gene_name)
        node.save()
        return node
