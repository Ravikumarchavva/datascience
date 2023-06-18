import java.util.Scanner;

public class switching {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter a number in (1,2,3) :");
        int key=sc.nextInt();
        switch (key) {
            case 1:
                System.out.println("hello");
                break;
            case 2:
                System.out.println("namaste");
                break;
            case 3:
                System.out.println("banjour");
                break;
            default:
            System.out.println("NOT VALID NUMBER");
                break;
        }
    }
}
