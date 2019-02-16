Content based news recommender system

Advance Software Engineering

Zia Muhammad

Matriculation no:886084

Data science 1<sup>st</sup> semester

Contents
========

1.  Introduction
2.  UML (Unified Model Language)

-   Use case diagram
-   Activity diagram
-   Sequence diagram

1.  Metrics (At least two Sonarqube)

-   Duplication
-   Security
-   Reliability

1.  Clean Code Development

-   Naming convention
-   No side effect functions
-   Exception handling
-   Unit tests
-   Useless comments

 5. Build management with Pybuilder

 6. DSL (Domain Specific Language)

 7. CI/CD (Continuous Integration and Continuous Delivery with Travis)

 8. Functional Programming

-   Final data structure
-   Side effects free functional
-   Higher order functional
-   Clojures/Anonymous function
-   Function as a parameter and return values

Introduction:
=============

This Project is a content-based recommender system for news articles. The goal of this recommender system is to give the user a choice of news articles what they want to read. This recommender system checks what a user is currently reading in terms of news articles and recommend semantically top three similar articles on the basis of common nouns.

UML(Unified Modeling Language):
===============================

UML is a standardized modeling language consisting of an integrated set of diagram, developed to help system and software developers for specifying , visualizing, constructing and documenting the artifacts of software system as well as for business modeling and other non software system.

Following are the UML diagrams for content based news recommender system.

### 1. Use case UML diagram:
Use case diagram of the recommender system as shown in below fig-1.
![Use case UML Diagram](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/usecase%20UML.jpg)


### 2. Activity UML Diagram :
Activity UML diagram of the recommender system as shown in below fig-2.
![Activity UML Diagram](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/activity%20uml.jpg)


### 3. Sequence UML diagram:
Sequence UML diagram of the recommender system as shown in below fig-3.
![Sequence UML Diagram](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/sequenceUML.jpg)




Metrics:
========

In software development, a metric is the measurement of a program’s performance or efficiency. For code analysis and review, Sonarqube is the probably best static code analyzer. Its easy to find bugs, code smell and security vulnerabilities. Sonarqube offers report on code issues, duplication(lines, blocks), code coverage, reliability, security , unit tests, complexity , comments and bugs.

### 1. Duplication Metrics:

There are no duplication(line duplication, files duplication, blocks duplication) in project code.
![Duplication metrics](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/duplication.PNG)

### 2. Security Metrics:

Security metrics find vulnerabilities and new vulnerabilities in source code.
![Security metrics](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/security.png)

### 3. Reliability Metrics:

Reliability metric analyze new bugs(number of news bugs issues in source code.
![Reliability metrics](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/reliability.png)

Clean code development:
=======================

Clean code means that code which is easy to understand and easy to change. Easy to understand the flow of entire application, easy to understand role and responsibility of each class, easy to understand what each method does , what is the purpose of expression and variable and easy to fix bugs.

### 1. **Naming convention:**

Proper naming convention is very important in clean code development. Easy readable to user.

### 2. **No side effect :**

In programming, side effect is when a function or expression modify state of a variable from outside its scope(local environment).Mostly without side effect functions have used in this project code.

### 3. **Exception Handling:**

Wherever necessary exception handling blocks have been added to ensure that no run time errors are thrown. Here used exception handling in this project code to catch value error exception. If url found what to do and if not found what to do then, for this purpose exception handling used .

### 4. **Unit tests:**

Make sure each piece of code is doing what you expect it to do. Following is an example of unit test which used for this recommender system.

### 5. **Useless comment:**

It’s important to write clean and simple code that can be easily understood by others. Like obvious names to variables, define explicit functions and comments. But in this project code, avoided useless comments because clear name for variables and functions have been used. Everyone can easily understand from variables and functions names what are these functions doing.

Build Management with Pybuilder:
================================

In this recommender system , Pybuilder has been used with build management. Pybuilder is a project management tool for python. It organizes code with a consistent directory structure (for source code, scripts and tests), manages unit testing, code coverage and can easily package your code. Here is the Build.py file which consist main description for this project.

After runing the pybuilder(pyb) with unit tests, it shows in below image that build successful.

CI/CD (Continuous Integration and Continuous Delivery with Travis):
===================================================================

Continuous integration and Contentious delivery pipeline of this project is based on Git, Travis CI and Heroku. When you made any modification in source code, Travis CI will activate , which will check a set of tests for a successful Integration of new coded added. After successful Integration, Travis CI will deploy source code on production server at Heroku.

Here it is travis.yml file(added to the repository, It tells to Travis CI what to do.

Check build status, it is pass or fail. See output in below figures.

DSL(Domain specific language):
==============================

Domain specific language is a computer language specialized to a particular application(to meet a specific need). Domain specific languages are distinguished from general purpose languages like C++, java, python etc. Popular examples of DSL are SQL, HTML, XML, UML etc. In this project I had used “regular expression” and “HTML” as a DSL. Following are the examples:

### 1. Regular expression:

A regular expression is a sequence of character that helps you match or find other strings or set of strings, using a specialized syntax held in pattern. Regular expression used as a DSL in this project code. Regular expression used to remove special characters from text.

### 2. HTML:

HTML is standard markup language which is using to create and design web page .

Here it is used as DSL because HTML has a specific domain, It is only using for web pages. I used HTML to make front web page for my recommender system where user can enter url and recommender system recommending top 3 articles.

Functional Programming:
=======================

Functional programming is a programming paradigm of writing code. Functional programming allows you to write more compressed, predictable code and it’s easy to test. Following few examples of functional programming have been used in pet project code.

### 1. **Final data structure:**

Some variables have been made immutable in project code.

### 2. **Side effects free function:**

Side effect are operation that change the global state of a variable or expression. All assignment and input/output operators considered side effects. Here I used function programming in project code, which has no side effect and mostly in functional programming , function have no side effects. Following is an example of side effect free function.

### 

### 

### 

### 3)High order function:

A high order function is a function that take function as a parameter or an argument or returns a function. High order function is in contrast to first order function which don’t take a function as an argument or return a function as output. High order functions like map and filter have used in project code. Map function applied a passed-in function to each item in an iterable object and return a list containing all function call result. Here map function takes get\_common\_words() function and a list, return as a result common nouns list.

### 4. **Clojures/Anonymous function:**

Lambda is an anonymous function. Lambda function used when we don’t want to write full function like def . A lambda function can take any number of arguments but can only have one expression. Assign the lambda expression to a variable, it works like python function. Lambda function used in this project code.

### 5. **Function as a parameter and return value:**

Take a function as a parameter and return value has also used in this project code.

It is an example of high order function, here “get\_token()” is a normal function, takes a function “get\_parts\_of\_speech()” as a input and as a result return a function.
