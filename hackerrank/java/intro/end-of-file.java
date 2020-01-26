import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<String>();
        while(scan.hasNext()) {
            lines.add(scan.nextLine());
        }
        for (int i = 0; i < lines.size(); i++) {
            System.out.printf("%d %s\n", i + 1, lines.get(i));
        }
    }
}