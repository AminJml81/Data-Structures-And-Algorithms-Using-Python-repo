package MyProjects;
public class GuessNum {

    public static void main(String[] args)
    {

      //  int abcde


          for(int number=10000;number<=99999;number++)
          {
            int a=number/10000,b=((number%10000)/1000),c=(((number%10000)%1000)/100),d=((((number%10000)%1000)%100)/10),e=((((number%10000)%1000)%100)%10);
            
            if (    ((a+b+c+d+e)==30) &&((e+c)==14) && ( ((a==(2*b)-1) )) && ( d==(b+1))  &&((b+c)==10))   {
                     System.out.println("The Secret Number is: "+number);    
                                                                                                             }
                else
                {
                    System.out.println(number+" "+a+" "+b+" "+c+" "+d+" "+e+" "+"False");
                    number++;
                }

        }
        

    }

}
