import java.lang.reflect.Array;
import java.util.ArrayList;

public class RSAAttack {
    public static void main(String[] args) {
        long N = 4294967317L;
        int c = 17;
        int e =(int) Math.pow(2.0, 16.0)+1;
        System.out.println(e);
        ArrayList<Long> a = new ArrayList<Long>();
        a = trialDivision(N);
        long p = a.get(0);
        long q = a.get(1);
        System.out.println(p + " " + q);
        extendedEuclidian(e,(p-1)*(q-1));
        //gfg(e,(p-1)*(q-1));

        System.out.println("result ? " +Math.pow(17.0, -1971987327.0));

    }
    private static void gfg(long a, long b){
        long x = 0, y = 1, lastx = 1, lasty = 0, temp;
        while (b != 0)
        {
            long q = a / b;
            long r = a % b;
  
            a = b;
            b = r;
  
            temp = x;
            x = lastx - q * x;
            lastx = temp;
  
            temp = y;
            y = lasty - q * y;
            lasty = temp;           
        }
      System.out.println("GCD "+a+" and its Roots  x : "+ lastx +" y :"+ lasty);
      
    }

    private static void extendedEuclidian(long a, long b) {
        long rPrime = a;
        long r = b;
        long sPrime = 1;
        long s = 0;
        long tPrime = 0;
        long t = 1;
        
        while(r != 0){
            long qvotient = Math.abs(rPrime/r);
            
            
            
            long rTemp = r;
            r = rPrime -(qvotient*r);
            rPrime = rTemp;

            long sTemp = s;
            s = sPrime -(qvotient*s);
            sPrime = sTemp;

            long tTemp = t;
            t = tPrime -(qvotient*t);
            tPrime = tTemp;

        }
        long d = rPrime;
        long x = tPrime;
        long y = sPrime;
        System.out.println("Answer ??? =("+d+","+x+","+y+")");
        d = ((y % b)+b)%b;
        System.out.println(y);
        System.out.println(b);
        System.out.println(d);
        System.out.println("???" + y % b);
    }
    public static ArrayList<Long> trialDivision(Long N){
        ArrayList<Long> a = new ArrayList<Long>();
        long f = 2;
        while(N>1){
            if(N%f == 0){
                a.add(f);
                N /= f;

            }else{
                f+=1;
            }
        }
        if(N!=1){
            a.add(N);
        }
        return a;
    }
}
