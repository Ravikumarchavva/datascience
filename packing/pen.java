class MakePen{
    String color;
    String type;
    public void write() {
        System.out.println(this.color+" "+this.type);
    }
    //constructor
    MakePen(String color,String type) {
        this.color=color;
        this.type=type;
    }
    //copy constructor
    MakePen(MakePen mp){
        this.color=mp.color;
        this.type=mp.type;
    }
    MakePen(){
        
    }
}
public class pen {
    public static void main(String[] args) {
        MakePen pen1=new MakePen("blue","gel");
        pen1.write();
        MakePen pen2=new MakePen(pen1);
        pen2.write();
    }
}
