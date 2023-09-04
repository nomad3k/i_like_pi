Feature: Confirm the standard test datasets

    Scenario: 2023

        Given we use test dataset "PI/2023"
         Then no Products exist
          And 3 Scopes exist
          And Scope "identifiers" exists:
            | attribute    | type   | multiple |
            | product_id   | string | false    |
          And Scope "basic" exists:
            | attribute    | type   | multiple |
            | name         | string | false    |
            | description  | string | false    |
          And Scope "snomed_codes" exists:
            | attribute    | type   | multiple |
            | snomed_code  | string | true     |
