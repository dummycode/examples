public class Factorial {
    public static void main(String args[]) {
        if(args.length == 1)
            System.out.println(getFactorial(Integer.parseInt(args[0])));
        else 
            System.out.println("Invalid arguments");
    }
    static int getFactorial(int i) {
        if(i < 1)
            return 1;
        else
            return i *= getFactorial(i - 1);
    }
}
