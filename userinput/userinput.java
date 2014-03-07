import java.util.Scanner;
public class userinput {
	public static void main(String args[]) {
		System.out.print("Input: ");
		Scanner scan = new Scanner(System.in);
		String input = scan.nextLine();
		scan.close();
		System.out.println("You entered, \"" + input + "\"");
	}
}