
public class Complex {

  private final double real;
  private final double virl;

  public Complex(double real, double virl) {
    this.real = real;
    this.virl = virl;
  }

  public double getReal() {
    return real;
  }

  public double getVirl() {
    return virl;
  }

  public Complex add(Complex that) {
    return new Complex(this.real + that.real, this.virl + that.virl);
  }

  public Complex subtract(Complex that) {
    return new Complex(this.real - that.real, this.virl - that.virl);
  }

  public Complex multiply(Complex that) {
    double real = this.real * that.real - this.virl * that.virl;
    double virl = this.real * that.virl + this.virl * that.real;
    return new Complex(real, virl);
  }

  public Complex divide(Complex that) {
    Complex result = this.multiply(new Complex(that.real, -that.virl));
    double abs = that.real * that.real + that.virl * that.virl;
    return new Complex(result.real / abs, result.virl / abs);
  }

  public Complex add(double that) {
    return this.add(new Complex(that, 0));
  }

  public Complex subtract(double that) {
    return this.subtract(new Complex(that, 0));
  }

  public Complex multiply(double that) {
    return this.multiply(new Complex(that, 0));
  }

  public Complex divide(double that) {
    return this.divide(new Complex(that, 0));
  }

  @Override
  public String toString() {
    Complex c = this;
    if (c.real == 0 && c.virl == 0) {
      return "0";
    } else if (c.real == 0) {
      return "" + c.virl + "j";
    } else if (c.virl == 0) {
      return "" + c.real;
    } else if (c.virl > 0) {
      if (c.virl == 1) {
        return "" + c.real + "+j";
      } else {
        return "" + c.real + "+" + c.virl + "j";
      }
    } else {
      if (c.virl == -1) {
        return "" + c.real + "-j";
      } else {
        return "" + c.real + c.virl + "j";
      }
    }
  }
}
