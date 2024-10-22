@when('I search for product with name "{name}"')
def step_impl(context, name):
    context.response = context.client.get(f"/products?name={name}")
