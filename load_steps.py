@given('the following products')
def step_impl(context):
    for row in context.table:
        Product(name=row['name'], category=row['category'], available=row['available']).save()
