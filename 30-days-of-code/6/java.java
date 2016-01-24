import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String s = "#";
        for(int i = 0; i < n; i++){
            System.out.printf("%"+n+"s\n",s);
            s+="#";
        }
    }
}
