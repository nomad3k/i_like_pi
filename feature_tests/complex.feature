Given public Scope identifiers:
    | attribute             | type   | optional | multiple |
    |-----------------------|--------|----------|----------|
    | product_id            | string | false    | false    |
    | accredited_system_id  | string | false    | false    |
  And public Scope basic:
    | attribute             | type   | optional | multiple |
    |-----------------------|--------|----------|----------|
    | short_name            | string | false    | false    |
    | long_name             | string | false    | false    |
    | description           | string | false    | false    |
    | purpose               | string | false    | false    |
  And public Scope connection_details:
    | attribute             | type   | optional | multiple |
    |-----------------------|--------|----------|----------|
    | name                  | string | false    | false    |
    | url                   | string | false    | false    |
  And private Scope contact_details:
    | attribute             | type   | optional | multiple |
    |-----------------------|--------|----------|----------|
    | primary_contact_name  | string | false    | false    |
    | primary_contact_email | string | false    | false    |
    | primary_contact_tel   | string | false    | false    |
  And private Scope snomed_codes:
    | attribute             | type   | optional | multiple |
    |-----------------------|--------|----------|----------|
    | snomed_codes          | string | false    | true     |
  And Product nrl is keyed using identifiers:
    | key                   | value                     |
    |-----------------------|---------------------------|
    | product_id            | "XXX-YYY-ZZZ"             |
    | accredited_system_id  | "12345678"                |
  And Product nrl has scopes:
    | scope              | multiple |
    |--------------------|----------|
    | basic              | false    |
    | connection_details | true     |
    | contact_details    | false    |
    | snomed_codes       | false    |
  And Product nrl has basic Scope:
    | name         | value                     |
    |--------------|---------------------------|
    | product_id   | "XXX-YYY-ZZZ"             |
    | short_name   | "NRL"                     |
    | long_name    | "National Record Locator" |
    | description  | "Lorem Ipsum Solar..."    |
    | purpose      | "Lorem Ipsum Solar..."    |
  And Product nrl has snomed_codes Scope:
    | name         | value                     |
    |--------------|---------------------------|
    | snomed_codes | "12345"                   |
    | snomed_codes | "67890"                   |
 When I validate NRL
 Then the result is Fail
  And the scope validation is:
    | scope              | valid   | message                                         |
    |--------------------|---------|-------------------------------------------------|
    | basic              | true    | OK                                              |
    | connection_details | false   | One or more connection_details must be supplied |
    | contact_details    | false   | One or more properties is missing               |
    | snomed_codes       | true    | OK                                              |
