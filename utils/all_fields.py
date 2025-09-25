def all_fields(model):
  """ Reutrns all the name field"""
  return [field.name for field in model._meta.fields]

