Scenario: Search product by name
  Given the following products
    | name       | category  | available |
    | TestProduct | Electronics | True      |
  When I search for product with name "TestProduct"
  Then I should see a list containing "TestProduct"
