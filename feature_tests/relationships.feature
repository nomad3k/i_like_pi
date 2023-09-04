Feature: Product Relationships

    Scenario: Add a relationship

        Given Product "NRLF"
          And Product "BaRS"
         When I add a relationship where "BaRS" DependsUpon "NRLF"
         Then Product "BaRS" has the following relationships:
            | target | type        | status   |
            | NRLF   | DependsUpon | Proposed |
          And Product "NRLF" has no relationships

    Scenario: Approve a relationship

        Given Product "NRLF"
          And Product "BaRS"
          And "BaRS" DependsUpon "NRLF"
         When I approve "BaRS" relationship with "NRLF"
         Then the operation is successful
          And Product "BaRS" has the following relationships:
            | target | type        | status   |
            | NRLF   | DependsUpon | Approved |
          And Product "NRLF" has no relationships

    Scenario: Approve a relationship with requirements

        Given we use test dataset "PI/2023"
          And Product "NRLF"
          And Product "NRLF" has requirements when another Products DependsUpon it:
            | scope        |
            | snomed_codes |
          And Product "BaRS" with properties:
            | property    | value |
            | snomed_code | 123   |
            | snomed_code | 456   |
            | snomed_code | 789   |
          And "BaRS" DependsUpon "NRLF"
         When I approve "BaRS" relationship with "NRLF"
         Then the operation was successful
         Then Product "BaRS" has the following relationships:
            | target | type        | status   |
            | NRLF   | DependsUpon | Approved |

    Scenario: Cannot approve a relationship that does not meet requirements

        Given we use test dataset "PI/2023"
          And Product "NRLF"
          And Product "NRLF" has requirements when another Products DependsUpon it:
            | scope        |
            | snomed_codes |
          And Product "BaRS"
          And "BaRS" DependsUpon "NRLF"
         When I approve "BaRS" relationship with "NRLF"
         Then the operation was unsuccessful
          And the error states:
            | property  | value                          |
            | type      | RelationshipRequirementsNotMet |
            | message   | "snomed_code is required"      |
         Then Product "BaRS" has the following relationships:
            | target | type        | status   |
            | NRLF   | DependsUpon | Proposed |
