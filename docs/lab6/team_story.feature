Feature: Campus Maintenance Reporter

  Scenario: Reporter submits a maintenance report
    Given the reporter is logged in
    When the reporter submits a report with a title, description, and category
    Then the report should be saved with status "New"
    And a confirmation message should be displayed

  Scenario: Reporter submits a report without a description
    Given the reporter is logged in
    When the reporter submits a report with an empty description
    Then the report should be refused
    And an error message "Description is required" should be displayed

  Scenario: Dispatcher assigns a report to a technician
    Given a maintenance report with status "New" exists
    When the dispatcher assigns the report to a technician
    Then the report status should become "Assigned"
    And the assigned technician should appear in the report details
    