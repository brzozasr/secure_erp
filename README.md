# Secure ERP

## Story
You are working at an enterprise solution company. A new client approaches you for an ERP software they need for the administration of their daily operations. Naturally, you have multiple complex solutions for this job.

The problem is that the client is extremely suspicious about cloud technologies and the web in general. They say that what is on the net, or just on a computer that is connected to the Internet, is already compromised, and at least four countries' secret services come and go there regularly.

So they want to see a solution that is super secure: a short and clean codebase that works on local files, strictly on offline computers. It is your team's job to create such an application from scratch.

They require a highly modularized structure where the code for different content areas are separated, and every user and file I/O operations go through one and only one channel. You decide to create a variant of the MVC (model-view-controller) architecture for terminal and local data files.

As the client wouldn't provide any real data, only the general structure, you had to create some dummy data for the development.

#### What are you going to learn?
- modular design, MVC pattern
- searching, filtering, and transforming data
- clean code
- conform to requirements
- collaborate with your team

#### Tasks

###### CRM module
Implement the CRM module with basic and special operations.
- (1-4) Provide basic CRUD operations.
- (5) Get the emails of subscribed customers.

###### Sales module
Implement the Sales module with basic and special operations.
- (1-4) Provide basic CRUD operations.
- (5) Get the transaction that made the biggest revenue.
- (6) Get the product that made the biggest revenue altogether.
- (7) Count number of transactions between two given dates.
- (8) Sum the price of transactions between two given dates.

###### HR module
Implement the HR module with basic and special operations.
- (1-4) Provide basic CRUD operations.
- (5) Return the names of the oldest and the youngest employees as a tuple.
- (6) Return the average age of employees.
- (7) Return the names of employees having birthdays within the two weeks starting from the given date.
- (8) Return the number of employees with at least the given clearance level.
- (9) Return the number of employees per department in a dictionary (like {'dep1': 5, 'dep2': 11}).

#### General requirements
- You mustn't use any external modules except for those already in the files.
- Only model files import data_manager, and model files don't import the view at all.

#### Hints
- This project contains many similar requirements, try to unite as many common parts as possible!
- Do not spend much time on input checking. This time it is not a problem if a badly formatted data breaks your code.



#### Story
You are working at an enterprise solution company. A new client approaches you for an ERP software they need for the administration of their daily operations. Naturally, you have multiple complex solutions for this job.

The problem is that the client is extremely suspicious about cloud technologies and the web in general. They say that what is on the net, or just on a computer that is connected to the Internet, is already compromised, and at least four countries' secret services come and go there regularly.

So they want to see a solution that is super secure: a short and clean codebase that works on local files, strictly on offline computers. It is your team's job to create such an application from scratch.

They require a highly modularized structure where the code for different content areas are separated, and every user and file I/O operations go through one and only one channel. You decide to create a variant of the MVC (model-view-controller) architecture for terminal and local data files.

As the client wouldn't provide any real data, only the general structure, you had to create some dummy data for the development.

#### What are you going to learn?
- modular design, MVC pattern
- searching, filtering, and transforming data
- clean code
- conform to requirements
- collaborate with your team

#### Tasks

###### CRM module
Implement the CRM module with basic and special operations.
- (1-4) Provide basic CRUD operations.
- (5) Get the emails of subscribed customers.

###### Sales module
Implement the Sales module with basic and special operations.
- (1-4) Provide basic CRUD operations.
- (5) Get the transaction that made the biggest revenue.
- (6) Get the product that made the biggest revenue altogether.
- (7) Count number of transactions between two given dates.
- (8) Sum the price of transactions between two given dates.

###### HR module
Implement the HR module with basic and special operations.
- (1-4) Provide basic CRUD operations.
- (5) Return the names of the oldest and the youngest employees as a tuple.
- (6) Return the average age of employees.
- (7) Return the names of employees having birthdays within the two weeks starting from the given date.
- (8) Return the number of employees with at least the given clearance level.
- (9) Return the number of employees per department in a dictionary (like {'dep1': 5, 'dep2': 11}).

#### General requirements
- You mustn't use any external modules except for those already in the files.
- Only model files import data_manager, and model files don't import the view at all.

#### Hints
- This project contains many similar requirements, try to unite as many common parts as possible!
- Do not spend much time on input checking. This time it is not a problem if a badly formatted data breaks your code.
