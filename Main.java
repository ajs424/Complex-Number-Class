
public class Main {

  public static void main(String[] args) {

    Complex a = new Complex(1, 2);
    Complex b = new Complex(3, 4);

    System.out.printf("a = %s\n", a);
    System.out.printf("b = %s\n", a);

    // operators
    System.out.printf("a + b = %s\n", a.add(b));
    System.out.printf("a - b = %s\n", a.subtract(b));
    System.out.printf("a * b = %s\n", a.multiply(b));
    System.out.printf("a / b = %s\n", a.divide(b));

    System.out.printf("a + 1 = %s\n", a.add(1));
    System.out.printf("a - 1 = %s\n", a.subtract(1));
    System.out.printf("a * 2 = %s\n", a.multiply(2));
    System.out.printf("a / 2 = %s\n", a.divide(2));


  }
}

