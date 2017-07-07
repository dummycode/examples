import java.util.Calendar;
import java.util.GregorianCalendar;

public class Problem19 {
    public static void main(String args[]) {
    	int total = 0;
        Calendar calendar = new GregorianCalendar(1901, 0, 1);
        while (calendar.before(new GregorianCalendar(2000, 11, 30))) {
	        calendar.add(Calendar.MONTH, 1);
	        if (calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
	        	total++;
	        }
        }
        System.out.println(total);
    }
}
