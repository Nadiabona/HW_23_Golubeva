from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_COMMANDS = ('filter', 'unique', 'limit', 'map', 'sort', 'regex')

class RequestSchema(Schema):
    cmd = fields.Str(required = True)# провалидировали типы, что придут только строчки
    value = fields.Str()
    file_name = fields.Str()


    @validates_schema
    def check_all_cmd_valid(self, values : dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS :
            raise ValidationError('"cmd" contains invalid value')#в values леит содержиморе всей схемы


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many = True) #то есть там лежит список схем, и каждая схема будет валидироваться по отдельностии
