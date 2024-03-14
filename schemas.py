from marshmallow import Schema, fields

class UserUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    user_role = fields.Str()
    registration_date = fields.DateTime()
    user_email = fields.Str()
    password_hash = fields.Str(required=True, load_only=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    user_role = fields.Str(required=True)
    registration_date = fields.DateTime(required=False)
    user_email = fields.Str(required=True)
    password_hash = fields.Str(required=True, load_only=True)


class PatientSchema(Schema):
    id = fields.Int(dump_only=True)
    date_of_birth = fields.DateTime(required=False)
    gender = fields.Str(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)
class PatientUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    date_of_birth = fields.DateTime()
    gender = fields.Str()
    address = fields.Str(required=True)

class TestUpdateSchema(Schema):
    test_name = fields.Str()
    description = fields.Str()
    recommended_interval = fields.Str()
class ResultsSchema(Schema):
    id = fields.Int(dump_only=True)
    patient_id = fields.Int(dump_only=True)
    test_id = fields.Int(dump_only=True)
    date_taken = fields.Str(required=True)
    result_pdf_path = fields.Str(required=True)
    status = fields.Str(required=True)
class ResultsUpdateSchema(Schema):
    date_taken = fields.Str()
    result_pdf_path = fields.Str()
    status = fields.Str()
class TestSchema(Schema):
    id = fields.Int(dump_only=True)
    test_name = fields.Str(required=True)
    description = fields.Str(required=True)
    recommended_interval = fields.Str(required=True)
