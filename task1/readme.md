# Task 1
**Imagine the following situation:** <br>
You are joining a cross-functional team which builds a
front-end application using REST APIs. You are a first QA engineer and need to establish a
QA process in the team.
1. What would you do in your first few days of work? Where would you start?
2. Which process would you establish around testing new functionality?
3. Which techniques or best practices in terms of code architecture and test design would
you use in your automated tests? <br>

# Conventions
- FE: Front End
- Module: Set of code for defined functionality. [Login module, Home Screen module, etc..] 
- CI/CD: Continuous Integration & Continuous Delivery

# Establishing QA Process 

## Answers
1. First few days I would execute pointer 1 & 2
    - Set the goals
    - Get to know Front-end application and design.
2. I would consider pointer 3, 4, & 5 for establishing the process
    - Hire QA specialists. 
    - Set the QA Road map along with the product road map.
    - Educate the QA team.
3. I would implement 
    - Sprint with Scrum & Retrospect for better QA process as mentioned collectively in pointers 1 to 8.
    - Enforcing design practices and code review for automated code.
    - Preference to Quality of code over quantity. 
    - Monitor test coverage each release and improvise.
  

## Below are the set of pointers that I would consider to establish the QA process.

1. Set the goals
    - To release defect-free builds.
    - To reduce development cost by contributing QA/USER perspective at the designing stage.
    - To improve UX.
    - To reduce repeated manual efforts in testing. 
    - Test documentation.
    - To have different kinds of automated test suites.  
    - Set standards for manual & automated test cases.
    - Plan CI/CD implementations. 
    - Pick a set of tools.
    - Plan and implement Test Frameworks. 
    - Set Workflow - QA Activities for the sprint.
    - Set test artifacts.
    - Set standards for reporting failures.
    
2. Get to know Front-end application and design.
    - Discuss with the Project Manager/Owner and get to know business logic.
    - Develop the application understanding from the consumer point of view.
    - Read the docs.
    - Get to know REST API and FE module mappings.
    - Let know the FE team about QA activities and QA involvement in design & sprint activities. 
 
3. Hire QA specialists. 
    - Manual
    - Automation

4. Set QA Road map along with the product road map.
    - Get to know the product road map.
    - Design the QA road map.
        - Automation 
        - Manual

5. Educate the QA team.
    - About the application.
    - About Rest APIs and Its integration with the FE application.
    - About the Importance of Http Error codes.
    - About the QA standards. 
    - About Sprint activities.
    - About release & hotfix builds. 
    - Pick tools
        - Test Plan and Test Cases tools
        - Test Automation tools
        - Test coverage tools
        - Reporting tools
        - Tools for docs & presentation. 
        - Project Management tool for automation. 
    - Divide the roles.
        - Manual Testing 
        - Automation Testing
    - Explain QA activities.
        - Manual
            - Involve in re/design meetings.
            - Create test plans, test cases, and discuss with team and developers.
            - Create data as required.
            - Start testing along with the developer when his feature branch is stable. (Integration tests)
            - Test E2E cases when the feature is good to merge. (System Testing) 
            - Create bugs & follow a bug life cycle.
        - Automation (Cross-Browser Regression/Performace)
            - Involve in re/design meetings.
            - Awareness about the importance of framework design, implementation, and future-proofing code.
            - Add Utils as and when required.
            - Create and categorize test plans, test cases, and its implementation. (Smoke/Integration/System tests)
            - Discuss with the team and developers.
            - Implement with mock data or place holders.
            - Start testing with the developer when his feature branch is stable.
            - Execute the whole set of tests and send them for Code Review.
            - Address review comments and merge them into the QA repository. 
        - General 
            - Daily scrum
            - Create Manual & Automation test environments.
            - Discuss test coverage
            - Discuss the importance of negative test cases.
            - Implement & Monitor CI/CD jobs on a daily basis.
            - Set schedules for test frameworks
            - Report failure. 

6. Managing build releases.
    - At the end of the sprint, branch off develops into the release branch.
    - Approve defect free build.
    - Test release docs.
    - Test upgrade docs.
    - Document known issues.
    - Plan hotfix as required. 

7. Activate the QA team in the sprint.
    - Set up artifacts, docs, tools, and repositories. 
    - Let know how and when to use them in the sprint. 

8. Retrospect with team after every release and improve the team and development. 