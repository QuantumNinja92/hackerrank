import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i = 0; i < t; i++){
        int a = sc.nextInt();
        int b = sc.nextInt();
        int n = sc.nextInt();
        String back = ""; // the String that will be printed and we will concatinate over it along the way
        int incre = a; // the incremental variable that will keep the last value in the series
        for(int j = 0; j < n; j++){
            incre = incre + ((int)Math.pow(2,j)*b);
            back = back + incre;
            if(j != n-1){
                back = back + " ";
            }
        }
        System.out.println(back);
        }
    }
}