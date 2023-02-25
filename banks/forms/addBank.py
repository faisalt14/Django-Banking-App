from django import forms


class AddBankForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=100, required=True)
    inst_num = forms.CharField(max_length=100, required=True)
    swift_code = forms.CharField(max_length=100, required=True)

    def clean(self):
        data = super().clean()

        name = data.get('name', '')
        description = data.get('description', '')
        inst_num = data.get('inst_num', '')
        swift_code = data.get('swift_code', '')

        if name is None or name == "":
            self.add_error('name', "This field is required")
        elif len(name) > 100:
            self.add_error('name',
                           "Ensure this value has at most 100 characters (it has <" + str(len(name)) + ">)")

        if description is None or description == "":
            self.add_error('description', "This field is required")
        elif len(description) > 100:
            self.add_error('description',
                           "Ensure this value has at most 100 characters (it has <" + str(len(description)) + ">)")

        if inst_num is None or inst_num == "":
            self.add_error('inst_num', "This field is required")
        elif len(inst_num) > 100:
            self.add_error('inst_num',
                           "Ensure this value has at most 100 characters (it has <" + str(len(inst_num)) + ">)")

        if swift_code is None or swift_code == "":
            self.add_error('swift_code', "This field is required")
        elif len(swift_code) > 100:
            self.add_error('swift_code',
                           "Ensure this value has at most 100 characters (it has <" + str(len(swift_code)) + ">)")

        return data
