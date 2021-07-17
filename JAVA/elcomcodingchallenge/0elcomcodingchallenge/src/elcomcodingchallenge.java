import java.util.*;
import java.io.*;
public class elcomcodingchallenge {
	public static void main(String[] args) throws IOException{ //IOException occurs when the Input/Output operation fails
		int NoOfLines = 0; //Variable NoOfLines stores the number of lines in a file  
		int NoOfWords = 0; //Variable NoOfWords stores the number of words in the file 
		float AWL = 0.000f;// Variable AWL stores the Average Word Length in the file.
		
		Scanner file = null; //variable file initially stored as null but will eventually store the text file  
		
		try {
			Scanner textFile = new Scanner(new File("src/MQ.txt")); //Variable textFile searches and store the text document the MQ.txt
			file = textFile; //Set file to textFile, file now stores the text file MQ.txt 
		}
		//Handle used if the text file is not found
		catch(FileNotFoundException e){
			System.out.println("file does not exist");
		}
		
		while(file.hasNextLine()) {//loop until the file has no lines left
			String currentLine = file.nextLine();//Set variable currentline to scan on the current line in the file including the spaces  
			int length = currentLine.length(); //set length to the length of the current line
			boolean DivFound = true; // set DivFound to true as there are not words on the file yet
			//Loop until i is greeter than length 
			for (int i = 0; i < length; i++) { 
				//if the character at position i is blank then set DivFound to by true. If Five found is true then increment number of words to 1 then set DivFound to false.  
				if (currentLine.charAt(i) == ' ') {
					DivFound = true;
					//CharFound = false;
				}
				else if (DivFound){
					NoOfWords++;
					DivFound = false;
				}
				
 			}
			NoOfLines++;//Increment number of lines by 1 once the first line as been scanned. 
		}
		file.close();//Close the file once the loop is done
		
		AWL = NoOfWords/NoOfLines; //Calculate the average word length by Dividing the Number of words by the number of lines 
		
		System.out.println("Number of Words: " + NoOfWords);//Display the number of words
		System.out.println("Number of Lines: " + NoOfLines);//Display the number of lines 
		System.out.println("Average Word Length: " + AWL);//Display the Average Mean Length

	}
}
