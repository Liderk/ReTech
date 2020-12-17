from rest_framework import serializers

from todo.models import Company, Task


class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    task = serializers.CharField(max_length=250)

    class Meta:
        model = Task
        fields = ('id', 'name', 'task')

    def validate(self, attrs):
        user = self.context['request'].user
        company = Company.objects.get(name=user.account.company_access)
        attrs['company'] = company
        return attrs
