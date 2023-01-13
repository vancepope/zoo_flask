## Zoo Flask
 - Built with Flask utilizing Elephant SQL

<details>
<summary> :clipboard: Click here to test plan</summary>
<br />

1. Purpose
    - The purpose of our tests are to help develop an application that will be able to ensure animals can be assigned to enclosures without the presence of harm, provide and maintain a better quality of life to enable researchers more conclusive data for their studies. At this stage of the project, we will begin by utilizing the process of test driven developement to solidify the functionality and stability of the application.

2. Scope
    - The scope of this application will be to test the following methods:
        - connection
        - create_enclosures
        - create_animals
        - add_enclosure
        - add_animal
        - display_animals
3. Inputs
    1. Enclosures
        - Name
    2. Animals
        - Name
        - Quantity
        - Enclosure Id
        - Enclosure Name (Foreign Key)
    
4. Outputs
    - A report in the form of an HTML file will be generated to display test results.
    - Tests will also be logged to a .log file

5. Assumptions
    - As a developer, I should be able to create a connection to an ElephantSQL database
    - As a developer, I should be able to create a table in the database and return a string that notifies me of its creation.
    - As a developer, I should be able to insert data into tables in the database and return an object containing the data
    - A report detailing each specific test along with its inputs and expected outputs should be generated
    - A log file detailing each process of the application and tests should be generated
    - As a developer, I should be able to display a list of animals that would contain data such as:
        - Id
        - Name
        - Quantity
        - Enclosure Id
        - Enclosure Name

6. Summary
    - Feature: Database
    - Environment: Development 
    - Duration: 2 hours 
    - Coverage: 95% 
    - Results: Pass

7. Test Cases
    - connection should return rows greater than 0, which would mean we have successfuly connected to the database.
        - Passed
    - create_animals method will return > 0 
        - Passed
    - create_enclosures method will return > 0 
        - Passed
    - add_enclosure will return a length of 1
        - Note: a 'dupe' variable will be used to check database for duplicates and not insert if such duplicate exists.
        - Passed
    - add_animal will return a length of 1
        - Note: a 'dupe' variable will be used to check database for duplicates and not insert if such duplicate exists.
        - Passed
    - display_animals will return a list and a length > 0
        - Passed

8. Conclusion
    - According to the test results, the database feature is functioning as expected. No issues were encountered during testing.


</details>