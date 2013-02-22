package hola;

import java.util.Scanner;

public class NameCross {

	/* This program accepts as input any string and outputs a cross using each character in the string.
	 * I called it NameCross because I initially used names as test input.
	 * 
	 */
	public static void main(String[] args) {
		System.out.println("Dame el nombre: ");
		Scanner input = new Scanner(System.in);
		String size = input.nextLine();
		
		if (size.length()%2==0)
			size = size + ".";
		
		char[][] X = new char[size.length()][size.length()];
		
		for(int i = 0 ; i < size.length() ; i++) {
			for(int j=0 ; j < size.length(); j++) {
				X[i][j] = ' ';
			}
		}
		for(int i = 0 ; i < size.length() ; i++) {
			X[i][i] = size.charAt(i);
			X[i][size.length()-i-1] = size.charAt(i);
		}
		
		for(int i = 0 ; i < size.length(); i++) {
			for(int j=0 ; j < size.length(); j++) {
				System.out.print(X[i][j]);
			}
			System.out.print('\n');
		}
	}

}
