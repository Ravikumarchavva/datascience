abstract class Animal{
    abstract void walk();
}
class Horse extends Animal{
    public void walk() {
        System.out.println("4 legs");
    }
}
class chick extends Animal{
    public void walk() {
        System.out.println("2 legs");
    }
}
interface Anime{
    void fly();
}
class tom implements Amine{
        public void walk() {
            System.out.println("4 legs");
        }
}
public class abs {
    public static void main(String[] args) {
        Horse h=new Horse();
        h.walk();
    }
}
