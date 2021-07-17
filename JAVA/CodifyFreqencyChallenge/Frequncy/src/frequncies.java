import java.util.*;
import java.io.*;

public class frequncies {
	public static void main(String[] args) throws IOException {
		
		int NoOfChar = 0; // Set number of characters to 0 
		Scanner ReadFile = null; // Initialise ReadFile variable 
		try {
			//Read the txt file 
			Scanner txtFile = new Scanner (new File("readfile.txt"));
			ReadFile = txtFile;
			
		} catch(FileNotFoundException e) {
			//Display if the file does not exist 
			System.out.println("File does not exist");
		}
		
		while(ReadFile.hasNextLine()) {
			String CurrLine = ReadFile.nextLine(); //set current line to 
			int length = CurrLine.length();// Length of the line in the file 
			boolean DivFound = true;//Set Division found between characters true
			boolean CharFound = false; //Set Characters found to false
			
			HashMap<Character, Integer> HM = new HashMap<Character, Integer>();//Initialise HashMap to story the character and the number of occurances. 
			int count;
			char Char;
			
			for(int i = 0; i < length; i++) {
				Char = CurrLine.charAt(i);
				//Counting the characters 
				if(Char == ' ') {//If the character is a blank space. 
					 DivFound= true;
					 CharFound = false;
				}else {
					CharFound = true;
					NoOfChar++//Increment by 1 
					;//(Dyck, 2020)
				}
				//Finding the frequency of the characters 
				//If the HashMap contains the characters then increment the count replace with the character and the number of occurrence. Otherwise add the character ans 1 
				if(HM.containsKey(Char) && Char != ' ') {
					count = HM.get(Char);
					count++;
					HM.replace(Char, count);
				} else {
					HM.put(Char,1);//(Birajdar, 2020)
				}
			}
			//Display list
			System.out.println(HM);
			
			
		}
		ReadFile.close();
	
		//Display number of Characters 
		System.out.println("Number of Characters:" + NoOfChar);
		

	} 

}

/*Birajdar, C., 2020. Java Program to find the occurrence count of each character in the string using the HashMap. [image] Available at: <https://www.youtube.com/watch?v=cpoo3l3IyLM&ab_channel=ChandrashekharBirajdarChandrashekharBirajdar> [Accessed 1 June 2021].*/
//Dyck, B., 2020. Java - Reading Files: Getting Number of Lines, Number of Characters, or Number of Words. [video] Available at: <https://www.youtube.com/watch?v=pi7eOUSObk0&ab_channel=BrianDyckBrianDyck> [Accessed 1 June 2021].
