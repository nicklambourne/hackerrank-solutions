import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        int halfLength;
        if (A.length() % 2 == 0) {
            halfLength = A.length() / 2;
        } else {
            halfLength = (int) Math.ceil(A.length()/2);
        }
        for (int i = 0; i <= halfLength; i++) {
            String start = A.substring(i, i+1);
            String end = A.substring(A.length()-i-1, A.length()-i);
            // System.out.printf("%s == %s\n", start, end);
            if (!start.equals(end)) {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }
}



