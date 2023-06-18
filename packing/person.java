package packing;


class Poly{
    public String name;
    public String age;
    public void info(String name,int age){
        System.out.println(name+' '+age);
    }
    public void info(String name){
        System.out.println(name);
    }
    public void info(int age){
        System.out.println(age);
    }
}
public class person {
    public static void main(String[] args) {
        Poly p1=new Poly();
        p1.info("ravi",20);
        Poly p2=new Poly();
        p2.info("ravi");
        Poly p3=new Poly();
        p3.info(20);
    }
}
