import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static String evaluate(int n) {
        if (n % 2 == 1) {
            return "Weird";
        } else if ((n >= 2 && n <= 5) || (n > 20)) {
            return "Not Weird";
        } else {
            return "Weird";
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        System.out.println(evaluate(N));
        scanner.close();
    }
}
