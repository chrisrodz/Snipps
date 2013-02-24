/* Christian A. Rodriguez
	CODE2040 Coding Exam, a simple chess game.
	12/3/2012 */

#include <string>
#include <ctype.h>
#include <iostream>
#include <iomanip>
using namespace std ;

void displayBoard(char board[][9]);
    /*----------------------------------------------------------------------
      Displays the game board. Iterates through the board array, displaying
      each game piece
    -----------------------------------------------------------------------*/
    
void movePiece(char board[][9], string start, string end);
    /*----------------------------------------------------------------------
      Moves the piece in position start to position end in the board. If there
      is no piece in start, or either positions are invalid outputs an error
      message.
    -----------------------------------------------------------------------*/

int main() {
	// Initialised game board
	char board[9][9] = { {'\0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'},
						{'1', 'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'},
						{'2', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
						{'3', '-', '-', '-', '-', '-', '-', '-', '-'},
						{'4', '-', '-', '-', '-', '-', '-', '-', '-'},
						{'5', '-', '-', '-', '-', '-', '-', '-', '-'},
						{'6', '-', '-', '-', '-', '-', '-', '-', '-'},
						{'7', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
						{'8', 'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'}} ;
	
	char choice ; 		// Control variable for game loop
	string start, end ; // Strings that indicate each game move
	
	while(tolower(choice) != 'n') {
		
		// Display the board to the user 
		displayBoard(board) ;
		
		// Receive the game move to execute
		cout << "\nMove which piece: " ;
		cin >> start ;
		cout << "To what space: " ;
		cin >> end ;
		
		// Execute the game move
		movePiece(board, start, end) ;
		
		// Ask the user if he wants to repeat
		cout << "\nGo again?(Y/N) " ;
		cin >> choice ;
	}
	
	cout << "Thank you for playing chess." << endl ;
	
	return 0 ;		
}


// Implementation of displayBoard()
void displayBoard(char board[][9]) {
	cout << endl ;
	for(int i = 0 ; i < 9 ; i++) { 
		for(int j = 0 ; j < 9 ; j++)
			cout << board[i][j] << " " ;
		cout << endl ;
	}
}

// Implementation of movePiece()
void movePiece(char board[][9], string start, string end) {
	
	// Conditions checked on both moves:
	// 1. The first character is a lowercase letter
	// 2. the second character is a digit from 1 to 8
	if(start[0] < 97 || start[0] > 122 || start[1] < 48 || start[1] > 56) {
		cout << "Invalid move. Please try again." << endl ;
		return ;
	} else if(end[0] < 97 || end[0] > 122 || end[1] < 48 || end[1] > 56) {
		cout << "Invalid move. Please try again." << endl ;
		return ;
	}
	
	// Assign the piece in position start to a temporary variable
	char piece ;
	piece = board[start[1]-48][start[0]-96] ;
	
	// Check if there is a valid piece in that space, if there isn't then return.
	if(piece == '-') {
		cout << "No piece in space " << start << " please try again." << endl ;
		return ;
	}
	
	// If there is a valid piece in the space move it to position end, and replace
	// position start with '-' to indicate no piece in that position
	board[start[1]-48][start[0]-96] = '-' ;
	board[end[1]-48][end[0]-96] = piece ;
	
	// Display the game board after the piece has executed
	displayBoard(board) ;
	
	return ;
}