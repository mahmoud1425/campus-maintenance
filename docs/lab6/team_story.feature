
Feature: Campus Maintenance Reporter

  Scenario: Reporter submits a maintenance report
    Given the reporter is logged in
    When the reporter submits a report with a title, description, and category
    Then the report should be saved with status "New"
    And a confirmation message should be displayed

  Scenario: Dispatcher assigns a report to a technician
    Given a maintenance report with status "New" exists
    When the dispatcher assigns the report to a technician
    Then the report status should become "Assigned"
    And the assigned technician should appear in the report details

  Scenario: Technician updates report status and adds a comment
    Given a maintenance report is assigned to a technician
    When the technician changes the status to "In Progress" and adds a comment
    Then the new status should be recorded
    And the comment should be visible to the reporter
    And the status change should record its time and author
