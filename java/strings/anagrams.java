import java.io.*;
import java.util.*;

public class Solution {
    static boolean isAnagram(String a, String b) {
    char[] wordA = a.toLowerCase().toCharArray();
    char[] wordB = b.toLowerCase().toCharArray();
    Arrays.sort(wordA);
    Arrays.sort(wordB);
    return Arrays.equals(wordA, wordB);

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
