package hola;

import java.util.Scanner;

public class GiftsNoRand {

	/* This program accepts as input names separated by commas(,) and outputs a possible order of
	 * giving gifts between each name such that no person leaves without a gift. The output order
	 * is fixed with no randomization yet. 
	 * */
	public static void main(String[] args) {
		System.out.println("Dame los nombres separados por comas: ");
		Scanner input = new Scanner(System.in);
		String names = input.nextLine();
		String[] tokens = new String[names.length()];
		tokens = names.split(",");
		
		if (tokens.length%2 == 0)
			for(int i=0; i+1<tokens.length; i+=2) {
				System.out.println(tokens[i]+"->"+tokens[i+1]+"\n");
				System.out.println(tokens[i+1]+"->"+tokens[i]+"\n");
			} 
		else {
			System.out.println(tokens[tokens.length-1]+"->"+tokens[0]+"\n");
			for(int i=0; i+1<tokens.length; i++) 
				System.out.println(tokens[i]+"->"+tokens[i+1]+"\n");
		}
			
		}
	}