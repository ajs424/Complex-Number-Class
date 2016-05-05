# Complex-Number-Class

Designed and implemented a class in Java, C++, and Python that represents complex numbers. The class supports important operations in addition, subtraction, multiplication and division. 

Being that the Java lanaguage does not allow operator overloading/ friend functions, the Java version will not include as many functions as the C++ and Python versions. However, I did override the toString() method in this version.

For the C++ and Python versions I implemented the following functions for each operation. In these functions op is one of +, -, *, or / :

op: Complex × Complex → Complex

op: Complex × double → Complex

op: double × Complex → Complex

I defined a constructor as well as overloaded the assignment operator so these versions can perform implicit conversions from doubles to Complex. The stream insertion operator << has also been overloaded to print objects of the proper type. In addition, the Python version contains functions that allow conversion from complexes to strings.

This repository includes:

-a Complex.java file that is the Java implementation

-a Main.java file that instantiates and tests all methods of the Complex class

-a complex.h file that contains the declaration of the complex class

-a complex.cc file that contains the implementations of method and functions declared in the complex class

-a main.cc that instantiates complex numbers and tests all methods and functions

-a complex.py file.

MainExample.java, mainExample.cc, rational.cc, rational.h, and rational.py were all used as example files.
