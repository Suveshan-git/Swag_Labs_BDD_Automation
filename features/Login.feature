Feature: Login
    Scenario Outline: Login successfully with the valid credentials
        Given I launched the Chrome browser
        When I open the SwagLabs page
        And enter the "<username>" and "<password>"
        And click the Login button
        Then I should land on the Products page

        Examples:
        |username|password|
        |standard_user|secret_sauce|
        |locked_out_user|secret_sauce|
        |problem_user|secret_sauce|
        |performance_glitch_user|secret_sauce|

