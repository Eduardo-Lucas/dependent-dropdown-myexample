from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from .models import BusinessLine, ProfitCenter, Project


class BusinessLineForm(forms.ModelForm):
    class Meta:
        model = BusinessLine
        fields = ('description', )


class ProfitCenterForm(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s estão duplicados.",
            }
        }

        model = ProfitCenter
        fields = ('businessline', 'description', )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'businessline', 'profitcenter', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profitcenter'].queryset = ProfitCenter.objects.none()

        if 'businessline' in self.data:
            try:
                businessline_id = int(self.data.get('businessline'))
                self.fields['profitcenter'].queryset = ProfitCenter.objects.filter(businessline_id=businessline_id).\
                    order_by('description')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty ProfitCenter queryset
        elif self.instance.pk:
            self.fields['profitcenter'].queryset = self.instance.businessline.profitcenter_set.order_by('description')
