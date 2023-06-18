import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        System.out.println("enter 2 numbers : ");
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        System.out.println("enter your choice : 1.add 2.sub 3.mul 4.div 5.mod");
        int c=sc.nextInt();
        switch (c) {
            case 1:
                System.out.println("add is "+(a+b));
                break;
            case 2:
                System.out.println("sub is "+(a-b));
                break;
            case 3:
                System.out.println("mul is "+(a*b));
                break;
            case 4:
                System.out.println("div is "+(a/b));
                break;
            case 5:
                System.out.println("mod is "+(a%b));
                break;
            default:
                System.out.println("enter a valid operation");
        }
    }
}
