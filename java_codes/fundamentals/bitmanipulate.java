public class bitmanipulate {
    public static int getBit(int num,int pos) {
    int bitmask=1<<pos;
    int a=num & bitmask;
    return a;
    }
    public static int setBit(int num,int pos) {
        int bitmask=1<<pos;
        int a=bitmask | num;
        return a;
    }
    public static int clearBit(int num,int pos) {
        int bitmask=1<<pos;
        int a=~bitmask & num;
        return a;
    }
    public static int updateBit(int num,int pos,int value) {
        int bitmask=1<<pos;
        if(value==1){
            int a=bitmask | num;
            return a;
        }
        else{
            int a=~bitmask & num;
            return a;
        }
    }
    public static void main(String args[]) {
        int x=5; //0101
        int ans=getBit(x,1);
        System.out.println(ans);
        ans=setBit(x,1);
        System.out.println(ans);
        ans=clearBit(x, 0);
        System.out.println(ans);
        ans=updateBit(x, 1,1);
        System.out.println(ans);        
    }
}
