# Car Dealership

## Description

   The Car Dealership app is a console-based application that facilitates the purchasing of cars. An employee can add cars to the lot and manage offers for those cars, while a customer can view the cars on the lot and make offers.
	
## Purpose

   We want to see that you can meet deadlines and that you can code. You are expected to complete the following requirements and give a 5 minute presentation of your project to our QC team.

## Requirements
1. Functionality should reflect the below user stories.
2. All Business Logic is modularized into its own package.
3. Data is stored in a mongo database.
4. Data Access is performed through the use of PyMongo.
   1. All Data Access is performed within its own package.
   2. Your mongo collections include at least one unique index.
5. All user input is received using the input() function
6. Data is modeled in Python using classes
7. Error's are handled
8. Logging is implemented
9. Unit testing is performed for your modules.
   1.  python -m unittest
10. PyLint score of 9/10 minimum
    1.  pylint app


## User Stories
Total Points: 25 Points

* As a user, I can login.
	* 2 points
* As an employee, I can add a car to the lot.
	* 3 points
* As a customer, I can view the cars on the lot.
	* 1 point
* As a customer, I can make an offer for a car.
	* 3 points
* As an employee, I can accept or reject a pending offer for a car.
	* 2 points
* As the system, I update a car to an owned state when an offer is accepted.
	* 2 points
* As the system, I reject all other pending offers for a car when an offer is accepted.
	* 3 points
* As a user, I can register for a customer account.
	* 3 points
* As an employee, I can remove a car from the lot.
	* 2 points
* As a customer, I can view the cars that I own.
	* 1 point
* As a customer, I can view my remaining payments for a car.
	* 1 point
* As an employee, I can view all payments.
	* 1 point
* As the system, I can calculate the monthly payment.
	* 1 point