class FieldValidator():

    @classmethod
    def validate_digit(self, field: str, field_name: str):
        while not field.isdigit():
            field = input(f'field \'{field_name}\' must be digits only. New input:')

        field = int(field)
        return field

