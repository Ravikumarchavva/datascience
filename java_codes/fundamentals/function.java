import java.util.Scanner;

public class function {
    public static int factorial(int i) {
        int a=1;
        while (i>0){
            a*=i;
            i--;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int INT=sc.nextInt();
        int b=factorial(INT);
        System.out.println(b);
    }
}
