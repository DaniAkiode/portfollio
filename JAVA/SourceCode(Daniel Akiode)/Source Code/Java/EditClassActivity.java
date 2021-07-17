package TDCollections.premix;
//Import

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

//EditClassActivityClass
public class EditClassActivity extends AppCompatActivity {
    //Declare Variable
    private Button btnSave, btnDelete, btnTimer;
    private EditText editable_task;

    DatabaseTaskHelper mDTH;
    PointTaker PT;

    private String choosenTask;
    private int choosenID;



    //Create activity
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_class);//Set View to Layout
        //Set Variable to Id from layout
        btnSave = findViewById(R.id.btnSave);
        btnDelete = findViewById(R.id.btnDelete);
        btnTimer = findViewById(R.id.btnTimer);
        editable_task = findViewById(R.id.editable_task);
        mDTH = new DatabaseTaskHelper(this);
        PT = new PointTaker(this);
        //Set recieve intent to get intent from previous class
        Intent receivedIntent = getIntent();


        //Set Variables to data from previous class
        choosenID = receivedIntent.getIntExtra("id",-1);
        choosenTask = receivedIntent.getStringExtra("Tasks");
        //Set the text
        editable_task.setText(choosenTask);
        //Set Button to OnClickListener
        btnSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String task = editable_task.getText().toString();
                if(!task.equals("")){//If string doesn not equal nothing then call updateTask(task,choosenID, choosenTask) from the Database Task Helper.
                    mDTH.updateTask(task,choosenID,choosenTask);
                    toastMessage("Task Updated");//Display Message

                }else{//Otherwise
                    toastMessage("You must enter a new task");//Display Message
                }

            }
        });
        //Set Button to OnClickListener
        btnDelete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mDTH.deleteTask(choosenID,choosenTask);//Call Function from DataBase Task Helper
                editable_task.setText("");//Set text to nothing






                toastMessage("removed from database"); //Display message
            }
        });
        //Set Button to OnClickListener
        btnTimer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(EditClassActivity.this, AlarmActivity.class);// Set intent to new intent
                startActivity(intent); //Start new activity
            }
        });




    }


    ///Function for displaying message
    private void toastMessage(String message){
        Toast.makeText(this,message, Toast.LENGTH_SHORT).show();
    }
}
