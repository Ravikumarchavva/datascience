import java.util.Scanner;
public class strings {
   public static void main(String args[]) {
    // String firstname="ravi";
    
    // String lastname="ravi";
    
    // String name=firstname+" "+lastname;
    // System.out.println(firstname.compareTo(lastname));
    // String name="ravi";
    // String n=name.substring(0,2);
    StringBuilder sb=new StringBuilder("ravi");
    System.out.println(sb.charAt(0));
    sb.setCharAt(3, 'p');
    System.out.println(sb);
    sb.insert(0, 'i');
    System.out.println(sb);
}
}
