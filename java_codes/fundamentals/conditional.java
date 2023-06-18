import java.util.Scanner;

public class conditional{
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    System.out.println("enter age");
    int age=sc.nextInt();
    if(age>18){
        System.out.println("adult");
    }
    else if(age<=18 && age >=13){
        System.out.println("teen");
    }
    else{
        System.out.println("child");
    }
}


}