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

3.  Metrics (At least two Sonarqube)

-   Duplication
-   Security
-   Reliability

4.  Clean Code Development

-   Naming convention
-   No side effect functions
-   Exception handling
-   Unit tests
-   Useless comments

 5. Build management with Pybuilder

 6. DSL (Domain Specific Language)

 7. CI/CD (Continuous Integration and Continuous Delivery with Travis)

 8. Functional Programming

-   High order function
-   Side effects free function
-   Final data structure
-   Anonymous function
-   Closures

9. How to run the recommender system server?



1 Introduction:
=============

This Project is a content-based recommender system for news articles. The goal of this recommender system is to give the user a choice of news articles what they want to read. This recommender system checks what a user is currently reading in terms of news articles and recommend semantically top three similar articles on the basis of common nouns.

2 UML(Unified Modeling Language):
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




3 Metrics:
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

4 Clean code development:
=======================

Clean code means that code which is easy to understand and easy to change. Easy to understand the flow of entire application, easy to understand role and responsibility of each class, easy to understand what each method does , what is the purpose of expression and variable and easy to fix bugs.

### 1. **Naming convention:**

Proper naming convention is very important in clean code development. Easy readable to user.

![Naming Convention](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/namingconvention.png)

![Naming convention](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/namec1.png)

![Naming convention](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/namec2.png)

![Naming convention](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/cleanedtextvariabele.png)

![Naming convention](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/commonwordsvariable.png)

![Naming convention](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/texttokenvariable.png)


### 2. **No side effect :**

In programming, side effect is when a function or expression modify state of a variable from outside its scope(local environment).Mostly without side effect functions have used in this project code.

![No side effect](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/sideeffectpos.png)

![No sideefect](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/nosideefectfun.png)

### 3. **Exception Handling:**

Wherever necessary exception handling blocks have been added to ensure that no run time errors are thrown. Here used exception handling in this project code to catch value error exception. If url found what to do and if not found what to do then, for this purpose exception handling used .

![Exception Handling](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/exceptionhandling.png)

### 4. **Unit tests:**

Make sure each piece of code is doing what you expect it to do. Following is an example of unit test which used for this recommender system.

![Unit test](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/newunittests.png)

### 5. **Useless comment:**

It’s important to write clean and simple code that can be easily understood by others. Like obvious names to variables, define explicit functions and comments. But in this project code, avoided useless comments because clear name for variables and functions have been used. Everyone can easily understand from variables and functions names what are these functions doing.

![Useless comments](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/uselesscomments.png)

5 Build Management with Pybuilder:
================================

In this recommender system , Pybuilder has been used with build management. Pybuilder is a project management tool for python. It organizes code with a consistent directory structure (for source code, scripts and tests), manages unit testing, code coverage and can easily package your code. Here is the Build.py file which consist main description for this project.

![Build Management](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/newbuildpy.png)

After runing the pybuilder(pyb) with unit tests, it shows in below image that build successful.

![Build Management Successed](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/buildsucces.png)


6 CI/CD (Continuous Integration and Continuous Delivery with Travis):
===================================================================

Continuous integration and Contentious delivery pipeline of this project is based on Git, Travis CI and Heroku. When you made any modification in source code, Travis CI will activate , which will check a set of tests for a successful Integration of new coded added. After successful Integration, Travis CI will deploy source code on production server at Heroku.

Here it is travis.yml file(added to the repository, It tells to Travis CI what to do.

![Travisyml file](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/travisyml.png)

Check build status, it is pass or fail. See output in below figures.

![Travis](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/passtravis.png)

![output travis](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/newtravis.png)

7 DSL(Domain specific language):
==============================

Domain specific language is a computer language specialized to a particular application(to meet a specific need). Domain specific languages are distinguished from general purpose languages like C++, java, python etc. Popular examples of DSL are SQL, HTML, XML, UML etc. In this project I had used “regular expression” and “HTML” as a DSL. Following are the examples:

### 1. Regular expression:

A regular expression is a sequence of character that helps you match or find other strings or set of strings, using a specialized syntax held in pattern. Regular expression used as a DSL in this project code. Regular expression used to remove special characters from text.

![Regular expression](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/newregularexpre.png)

### 2. HTML:

HTML is standard markup language which is using to create and design web page .

Here it is used as DSL because HTML has a specific domain, It is only using for web pages. I used HTML to make front web page for my recommender system where user can enter url and recommender system recommending top 3 articles.

![HTML](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/newhtml.png)

8 Functional Programming:
=======================

Functional programming is a programming paradigm of writing code. Functional programming allows you to write more compressed, predictable code and it’s easy to test. Following few examples of functional programming have been used in pet project code.

### 1. High order function:

A high order function is a function that take function as a parameter or an argument or returns a function. High order function is in contrast to first order function which don’t take a function as an argument or return a function as output. High order functions like map I have used in project code.
            
**A function which takes another function as an input(map):**
Map function applied a passed-in function to each item in an iterable object and return a list containing all function call result. Here is an example from project code shows in below figure

![High order function](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/getnounfunc.png)

![High order function](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/getnounmap.png)

**A function which returns another function:**
I have used a nested function in this project which return another function. The outer function ```get_parsed_text()``` takes raw text as input and clean it using its own code as well as that of the inner function ```Remove_special_char()```. ```Remove_special_char()``` removes special character from text and return processed text. I first call the outer function ```get_parsed_text()``` with raw content as an input parameter and it return the ```Remove_special_char``` function as a return value. I than call function ```Remove_special_char()``` which has access to the alread processed text in ```get_parsed_text()``` and remove the special characters from the text and return the clean text. This functionality is shown in the following two code snippets.

![Function](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/functionasaparameter.png)

![Function](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/functionreturn.png)


### 2. **Side effects free function:**

Side effect are operation that change the global state of a variable or expression. All assignment and input/output operators considered side effects. Here I used function programming in project code, which has no side effect and mostly in functional programming , function have no side effects. Following is an example of side effect free function.

![Side effect](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/namingconvention.png)

![Side effect](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/sideeffectpos.png)



### 3. **Final data structure:**

Some variables have been made immutable in project code.

![Final DS](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/finalds.png)



### 4. **Anonymous function:**

Lambda is an anonymous function. Lambda function used when we don’t want to write full function like def . A lambda function can take any number of arguments but can only have one expression. Assign the lambda expression to a variable, it works like python function. Lambda function used in this project code.

![Anonymous function](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/lambdafunc.png)

### 5. **Closure:**

A closure is a function object that remembers values in enclosing scope even if they are not present in memory. I have used Python closure in project code, you can see an example in below figure.

![Function as a parameter](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/closurescreenshot.png)


9 How to run the recommender system server?:
=======================
How to run this code.
1. **Install requirements:**
     ```Install requirements.txt```
2. **Run server:**
    To run server, use the following command: ```python /newsrecommender/src/main/python/recommender_server.py```
3. **Access web server:**
   You can access web server on ```127.0.0.1:5000/newsrecommender``` or at the address shown to you when you run the server. The port might be different. Once you access this address, you will be offered a page where you can enter a url (url for the currently read article by a user). Once you send that url to this web server, it will return top three articles. At this stage, I have kept it very simple with naive names. At a later stage, I intend to include articles title instead of just simple hyper links. Following will be the screens which a user will see as its user journey.

![Before enter url](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/beforeinput%20url.png)

![Enter url](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/enterurl.png)

![Top 3 articles](https://raw.githubusercontent.com/Ziasafi/newsrecommender/master/images/top3articles.png)

