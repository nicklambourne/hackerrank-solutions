import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        System.out.println(A.length() + B.length());
        System.out.println(B.compareTo(A) < 0 ? "Yes" : "No");
        System.out.printf("%s %s", A.substring(0,1).toUpperCase() + A.substring(1), B.substring(0,1).toUpperCase() + B.substring(1));
    }
}



