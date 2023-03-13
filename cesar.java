public class cesar {
    public static void main(String[] args){
        String input = ";\\r6TXfTe~r[bjrTeXrlbhrWb\\aZ2rHf\\aZrUeb^XarVelcgb~r[h[2r;TccXafrgbrg[XrUXfgrbYrhf!!!rAXkgrg\\`XrTebhaW~rgelr48F $%+r\\ar:T_b\\fr6bhagXer@bWXsss";

        char Ar[] = input.toCharArray();
        System.out.println(((char)(Ar[0]+-1)));

        //Ranges for the cipher
        int alphastart = 32;
        int alphaend = 126;
        

        for(int k = alphastart; k<alphaend;k++){
            for ( int i = 0; i<Ar.length; i++) {
                Ar[i] = (char) ((int)k+1);
            }
            System.out.print("\n line "+ k);
            for (int i = 0; i < Ar.length; i++) {
                System.out.print(Ar[i]);
            }
        }



    }
    

}
