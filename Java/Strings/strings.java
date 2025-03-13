import java.util.*;

public class Strings {

    public static void printLetters(String str) {
        for(int i=0; i<str.length(); i++) {
            System.out.print(str.charAt(i) + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        String name;
        name = sc.nextLine();
        System.out.println(name);

        String fullName = "Tony Stark";
        System.out.println(fullName.length());
        printLetters(fullName);
        sc.close();


    }
}
