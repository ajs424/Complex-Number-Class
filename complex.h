#ifndef _COMPLEX_H
#define _COMPLEX_H

#include <iostream>
using namespace std;

class Complex {
  private:
    double real;
    double virl;

  public:
    Complex(double real, double virl);
    // this constructor will converts a double to Complex implictly
    Complex(double real);
    ~Complex();

    // operator overloading
    Complex operator+(const Complex &that) const;
    Complex operator-(const Complex &that) const;
    Complex operator*(const Complex &that) const;
    Complex operator/(const Complex &that) const;
    

    friend Complex operator+(const double x, const Complex &that);
    friend Complex operator-(const double x, const Complex &that);
    friend Complex operator*(const double x, const Complex &that);
    friend Complex operator/(const double x, const Complex &that);

    friend ostream &operator<<(ostream &out, const Complex &c);

    double getReal() const;
    double getVirl() const;
};


#endif

