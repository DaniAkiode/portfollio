package TDCollections.premix;
//Imports
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

//DataActivity extends from AppCompatActivity
public class DateActivity extends AppCompatActivity {
    //Declare Variables
    DatabaseHelper DBHelper;
    Button SaveBtn;
    EditText NameEditText;
    //Create Activity
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_date);
        // Set variables to id from layout
        NameEditText = findViewById(R.id.NameEditText);
        SaveBtn = findViewById(R.id.SaveBtn);
        DBHelper = new DatabaseHelper(this);

        //Set button to onClickListener
        SaveBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String newEntry = NameEditText.getText().toString(); // Set newEntry to user input from NameEditText
                if (NameEditText.length() !=0){// If length of NameEditText is not zero then it would call the AddData(newEntry)
                    AddData(newEntry);
                    NameEditText.setText(""); //Set text to ""
                } else{ //otherwise
                    Toast.makeText(DateActivity.this,"Put Something in this field",Toast.LENGTH_LONG).show(); //Display message in toast
                }

                Intent intent = new Intent(DateActivity.this,ViewTheToDoLists.class) ; // Set intent to a new intent from this page to the To-Do-List page
                startActivity(intent); //Start next Activity
            }
        });
    }

    //Adds data to the database
    public void AddData(String newEntry){
        boolean insertData = DBHelper.addData(newEntry);// Set insertData to call the function adddata in the Database Helper

        if (insertData==true){ //if data has been inserted
            Toast.makeText(DateActivity.this,"Data Entered",Toast.LENGTH_LONG).show();//Display Message
        }else{// otherwise
            Toast.makeText(DateActivity.this,"Add A Name",Toast.LENGTH_LONG).show(); //Display Message
        }

    }
}
