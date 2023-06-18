class Shape{
    String color; 
}
class Triangle extends Shape{
    public void print(){
        System.out.println(color);}
}

public class inheritance {
    public static void main(String[] args) {
        Triangle t1=new Triangle();
        t1.color="red";
        t1.print();
        
    }
}
