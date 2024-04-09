//Matt Goldfarb 113346370
import java.util.Scanner;
public class TicTacToe {
	//This Boolean method determines is someone has won or not by using if statements and loops to determine if a row/column/diagonal/minor diagonal has all X's or O's. A GRID_SIZE integer is used with a count function to determine if it has all X or O
	public static boolean True(char[][] a) {
		//apply loops for different grid size
		int count = 0;
		int count1 = 0;
		for (int i=0; i<GRID_SIZE;i++) {
				if (a[i][i]=='X') {
					count+=1;}	
				else if (a[i][i]=='O') {
					count1+=1;}	
				else {
					count +=0;
					count1 +=0;}
		}
		if (count==GRID_SIZE) {
			System.out.println("Player 1 wins");
		return false;}
		if (count1==GRID_SIZE) {
			System.out.println("Player 2 wins");
		return false;}
	
		int count3=0;
		int count4=0;
		for (int i=GRID_SIZE-1, i1=0; i1<(GRID_SIZE);i1++) {
			if (a[i1][i-i1]=='X') {
				count3+=1;}	
			else if (a[i1][i-i1]=='O') {
				count4+=1;}	
			else {
				count3+=0;
				count4+=0;}
		}
		if (count3==GRID_SIZE) {
			System.out.println("Player 1 wins");
			return false;}
		if (count4==GRID_SIZE) {
			System.out.println("Player 2 wins");
			return false;}
		
		int count5=0;
		int count6=0;
		for (int i=0; i<GRID_SIZE;i++) {
			for (int j=0;j<GRID_SIZE;j++) {
				if (a[i][j]=='X') {
					count5+=1;}	
				else if (a[i][j]=='O') {
					count6+=1;}	
				else {
					count5+=0;
					count6+=0;}
		}
			if (count5==GRID_SIZE) {
				break;}
			else if (count6==GRID_SIZE) {
				break;
			}
			else {
				count5=0;
				count6=0;}
		}
		if (count5==GRID_SIZE) {
			System.out.println("Player 1 wins");
			return false;}
		if (count6==GRID_SIZE) {
			System.out.println("Player 2 wins");
			return false;}
		
		int count7=0;
		int count8=0;
		for (int j=0; j<GRID_SIZE;j++) {
			for (int i=0;i<GRID_SIZE;i++) {
				if (a[i][j]=='X') {
					count7+=1;}	
				else if (a[i][j]=='O') {
					count8+=1;}	
				else {
					count7+=0;
					count8+=0;}
		}
			if (count7==GRID_SIZE) {
				break;}
			else if (count8==GRID_SIZE) {
				break;
			}
			else {
				count7=0;
				count8=0;}
		}
		if (count7==GRID_SIZE) {
			System.out.println("Player 1 wins");
			return false;}
		if (count8==GRID_SIZE) {
			System.out.println("Player 2 wins");
			return false;}
		else {
			return true;}
	}
	public static int GRID_SIZE = 3;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[][] a1 = new char[GRID_SIZE][GRID_SIZE];
		True(a1);
		Boolean Player1=true;
		int count = 0;
		do  {
			if (Player1==true) {
				Scanner input = new java.util.Scanner(System.in);
				System.out.print("Enter number for row: ");
				int r = input.nextInt();
				System.out.print("Enter number for column: ");
				int c = input.nextInt();
				if (r>=GRID_SIZE || c>=GRID_SIZE ||r<0||c<0) {
					System.out.println("Not valid, try again");
					Player1=!Player1;
				}
				else if (a1[r][c]=='X'||a1[r][c]=='O') {
					System.out.println("Not valid, try again");
					Player1=!Player1;
				}
				else {
					a1[r][c] = 'X';
					}
			}
			else {
				Scanner input = new java.util.Scanner(System.in);
				System.out.print("Enter number for row: ");
				int r1 = input.nextInt();
				System.out.print("Enter number for column: ");
				int c1 = input.nextInt();
				if (r1>=GRID_SIZE || c1>=GRID_SIZE || c1<0 || r1<0) {
					System.out.println("Not valid, try again");
					Player1=true;
				}
				else if (a1[r1][c1]=='X'||a1[r1][c1]=='O') {
					System.out.println("Not valid, try again");
					Player1=true;
				}
				else {
					a1[r1][c1] = 'O';
					}
			}
		Player1=!Player1;
		for (int i=0; i<GRID_SIZE;i++) {
			System.out.print("|");
			for (int j=0; j<GRID_SIZE;j++) 
				System.out.print(a1[i][j]+ "|");
				System.out.println();
			}
			count++;
		} while (True(a1)&&count<9);
		if (count==9) {
			System.out.println("Draw");
		}
	}
}