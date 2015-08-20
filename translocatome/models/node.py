from django.db import models


class UniProtAc(models.Model):
    value = models.CharField(max_length=50, unique=True)


class GeneName(models.Model):
    value = models.CharField(max_length=50, unique=True)


class Node(models.Model):
    uni_prot_ac = models.ForeignKey(UniProtAc)
    gene_name = models.ForeignKey(GeneName)

    @staticmethod
    def get_by_uniprot_ac(uniprot_ac):
        uni_prot_ac_obj = UniProtAc.objects.get_by_secondary_key(value=uniprot_ac)
        return Node.objects.get_by_secondary_key(uniprot_ac=uni_prot_ac_obj)

    @staticmethod
    def get_by_gene_name(gene_name):
        gene_name_obj = GeneName.objects.get_by_secondary_key(value=gene_name)
        return Node.objects.get_by_secondary_key(gene_name=gene_name_obj)

    @classmethod
    def create_if_not_exists(cls, uniprot_ac, gene_name):
        try:
            # TODO @fodma1: Throw error, if they are not the same
            uniprot_ac_obj = cls.get_by_uniprot_ac(uniprot_ac)
            cls.get_by_gene_name(gene_name)
            return Node.objects.get_by_secondary_key(uniprot_ac=uniprot_ac_obj)
        except Exception:
            uniprot_ac_obj = UniProtAc(value=uniprot_ac)
            uniprot_ac_obj.save()

            gene_name_obj = GeneName(value=gene_name)
            gene_name_obj.save()

            node = Node(uniprot_ac=uniprot_ac_obj, gene_name=gene_name_obj)
            node.save()
            return node
