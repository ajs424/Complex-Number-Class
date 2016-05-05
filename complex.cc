#include "complex.h"

ostream &operator<<(ostream &out, const Complex &c)
{
  if (c.real == 0 && c.virl == 0) {
    out << 0;
  } else if (c.real == 0) {
    out << c.virl << "j";
  } else if (c.virl == 0) {
    out << c.real;
  } else if (c.virl > 0) {
    if (c.virl == 1) {
      out << c.real << "+j";
    } else {
      out << c.real << "+" << c.virl << "j";
    }
  } else {
    if (c.virl == -1) {
      cout << c.real << "-j";
    } else {
      out << c.real << c.virl << "j";
    }
  }
  return out;
}

Complex::Complex(double real, double virl) :
  real(real), virl(virl)
{
}

Complex::Complex(double real) :
  real(real), virl(0)
{
}

Complex::~Complex()
{
}

    // operator overloading
Complex Complex::operator+(const Complex &that) const
{
  return Complex(this->real + that.real, this->virl + that.virl);
}

Complex Complex::operator-(const Complex &that) const
{
  return Complex(this->real - that.real, this->virl - that.virl);
}

Complex Complex::operator*(const Complex &that) const
{
  double real = this->real * that.real - this->virl * that.virl;
  double virl = this->real * that.virl + this->virl * that.real;
  return Complex(real, virl);
}

Complex Complex::operator/(const Complex &that) const
{
  Complex result = *this * Complex(that.real, -that.virl);
  double abs = that.real * that.real + that.virl * that.virl;
  result.real /= abs;
  result.virl /= abs;
  return result;
}

Complex operator+(const double x, const Complex &that)
{
  return that + x;
}

Complex operator-(const double x, const Complex &that)
{
  return Complex(x) - that;
}

Complex operator*(const double x, const Complex &that)
{
  return that * x;
}

Complex operator/(const double x, const Complex &that)
{
  return Complex(x) / that;
}

double Complex::getReal() const
{
  return real;
}

double Complex::getVirl() const
{
  return virl;
}

