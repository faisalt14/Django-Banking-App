# Django Banking Application  

## Overview  

This Django project represents a simple banking application, designed to provide initial experience in backend development. It consists of two core apps: Accounts and Banks, each containing two models: Bank and Branch.  

## Bank Model
•	**Name**: A string (max 100 characters, required).
•	**Swift Code**: A string (max 100 characters, required).
•	**Institution Number**: A string (max 100 characters, required).
•	**Description**: A string (max 100 characters, required).
•	**Owner**: Reference to a Django User instance.
•	**Branches**: Related set of branches.


## Branch Model
•	**Name**: A string (max 100 characters, required).
•	**Transit Number**: A string (max 100 characters, required).
•	**Address**: A string (max 100 characters, required).
•	**Email**: Validated email address, default: admin@utoronto.ca.
•	**Capacity**: Non-negative integer (optional).
•	**Last Modified**: Timestamp for last modification.


## Data Validation and Resilience
Both the frontend and backend implementations include checks for mandatory fields and validation requirements. In cases of errors, the form retains correctly entered information to avoid the need for redundant data entry.  

## Documentation
For a comprehensive list of endpoints, descriptions, HTTP methods, and payloads, refer to the docs/endpoint-doc.pdf file in this repository.




