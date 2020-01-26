import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int last = a;
            for (int j=0; j < n; j++) {
                last += (int) java.lang.Math.pow(2, j) * b;
                if (j == n-1) {
                    System.out.printf("%d\n", last);
                } else {
                    System.out.printf("%d ", last);
                }
            }
        }
        in.close();

    }
}