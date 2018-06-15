import java.util.Scanner;
import java.time.*;

public class Solution {

    public static String getDay(String dy, String mon, String yr) {
        int day = Integer.parseInt(dy);
        int month = Integer.parseInt(mon);
        int year = Integer.parseInt(yr);
        LocalDate date = LocalDate.of(year, month, day);
        return date.getDayOfWeek().name();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }
}