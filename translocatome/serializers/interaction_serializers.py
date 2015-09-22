from rest_framework import serializers
from translocatome.models import Interaction
from translocatome.models.interaction import BiologicalProcess

class InteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interaction
        fields = ('id', 'source_node', 'target_node', 'meta_data', 'interaction_type', 'edge_type', 'directness', 'effect_all', 'effect_final', 'biological_process', 'score', 'int_abrev', 'is_in_full', 'is_in_medium', 'is_in_small', 'is_in_skeleton',)
        depth = 1

    def data_with_fields(self):
        return {
            'data': self.data,
            'fields': self.get_form_fields()
        }

    def get_form_fields(self):
        model_fields = self.Meta.model._meta.fields
        # model_field_names = self.Meta.model._meta.get_all_field_names()
        # model_fields_by_get = [getattr()]
        form_fields = []

        field_types = [field.get_internal_type() for field in self.Meta.model._meta.fields]

        char_fields = [field for field in model_fields if field.get_internal_type() == 'CharField']
        choice_fields = [field for field in model_fields if field.get_internal_type() == 'PositiveSmallIntegerField']
        # many_to_many_fields = [field for field in model_fields if field.get_internal_type() == 'ManyToManyField']
        boolean_fields =[field for field in model_fields if field.get_internal_type() == 'BooleanField']

        for field in char_fields:
            form_fields.append({
                'key': field.attname,
                'type': 'input',
                'templateOptions': {
                    'label': field.verbose_name,
                },
            })

        for field in choice_fields:
            form_fields.append({
                'key': field.attname,
                'type': 'select',
                'templateOptions': {
                    'options': [{'name': choice[1], 'value': choice[0]} for choice in field.choices],
                    'label': field.verbose_name,
                }
            })

        for field in boolean_fields:
            form_fields.append({
                'key': field.attname,
                'type': 'checkbox',
                'templateOptions': {
                    'label': field.verbose_name,
                },
            })

        # for field in many_to_many_fields:
        #     values = BiologicalProcess.objects.values('value')
        #     form_fields.append({
        #         'key': field.attname,
        #         'type': 'tag',
        #         'templateOptions': {
        #             'label': field.verbose_name,
        #             'tags': values
        #         },
        #     })

        relate_many_to_many_fields = self.Meta.model._meta.get_all_related_many_to_many_objects()

        # form_fields.append({
        #     'key': self.Meta.model._meta.get_all_related_many_to_many_objects()
        #
        # })

        return form_fields
