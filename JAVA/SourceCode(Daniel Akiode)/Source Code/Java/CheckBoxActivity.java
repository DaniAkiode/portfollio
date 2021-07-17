package TDCollections.premix;
//Imports

import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

//CheckBoxActivity Class

public class CheckBoxActivity extends AppCompatActivity {
    //Declare Variables
    private static final String TAG = "CheckBoxActivity";

    DatabaseTaskHelper DTH;
    private Button AddTaskBtn;
    private EditText TaskName;
    private ListView tListView;
    CheckBox mCheckBox;
    private Button BackButton;
    TextView ResultView;
    CheckboxAdapter dataAdapter;
    int points;

    ///private String selectedList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_check_box);
        //Set Variables to View By Id
        TaskName = findViewById(R.id.TaskName);
        AddTaskBtn = findViewById(R.id.AddTaskBtn);
        tListView = findViewById(R.id.CheckBoxView);
        ResultView = findViewById(R.id.txtPoints);
        BackButton = findViewById(R.id.btnBackB);

        //Set Variables to New DatabaseTaskHelper
        DTH =  new DatabaseTaskHelper(this);


        //Set button to onClickListener
        AddTaskBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String newEntry = TaskName.getText().toString(); //Set String to Input from user
                if (TaskName.length() !=0) { //If length of variable is not 0 then
                    AddTasks(newEntry); // Call function
                    TaskName.setText("");// Set Text to nothing
                }else{
                    toastMessage("You must put something in the text field!"); //Display Message
                }

                Intent intent = new Intent(CheckBoxActivity.this,CheckBoxActivity.class); // Set intent to New Intent, this would refresh the Activity once the user has added a Task.
                startActivity(intent);
            }
        });
        //Set button to onClickListener
        BackButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(CheckBoxActivity.this, ViewTheToDoLists.class); // Set intent to new intent, CheckBoxActivity to ViewTheToDoLists
                startActivity(intent);
            }
        });

    }
    //This function would add the new task into the lists
    public void AddTasks(String newEntry){
        boolean insertData = DTH.addTasks(newEntry);

        if (insertData) {
            toastMessage("Data Successfully Inserted ");//Display Message
        } else {
            toastMessage("Something went wrong ");// Display Message
        }
    }
    //Refreshes list view when populated
    @Override
    protected void onPostResume() {
        super.onPostResume();
        populateCheckView(); //Call function
    }

    //this function adds points every time checkBox is ticked
    public void AddPoints(int points) {

        points =+ 10;

        Log.d(TAG,"3.Number Of Points:" + points);

        //ResultView.setText(points + "");
        //Log.d(TAG,"4.Number Of Points:" + points);


    }
    //this function Takes Away points every time checkBox is un ticked

    //CheckboxAdapter Class
    private class CheckboxAdapter extends ArrayAdapter<String>
    {
        //Declare List
        private ArrayList<String> TaskList;

        //Starts Class
        public CheckboxAdapter(Context context, int textViewResourceId, ArrayList<String>TaskList)
        { super(context, textViewResourceId, TaskList);
            this.TaskList = new ArrayList<String>();
            this.TaskList.addAll(TaskList);
        }

        //ViewHolder Class
        private class ViewHolder {

            CheckBox check;
        }

        //GetView Method
        @Override
        public View getView(int position, View convertView, ViewGroup parent) {

            ViewHolder holder = new ViewHolder(); // Set holder to new View Holder
            if (convertView==null) // If view is not set
            {
                LayoutInflater vi = (LayoutInflater)getSystemService(Context.LAYOUT_INFLATER_SERVICE); //Set Vi to get system service from layout inflater service
                convertView = vi.inflate(R.layout.inner_checkview, null);//Set ConvertView to inflated layout

                holder.check = convertView.findViewById(R.id.checkBox1); //Set to Checkbox1 in inflated layout

                convertView.setTag(holder);

                //Set Checkbox to on click listener
                final ViewHolder finalHolder = holder;
                holder.check.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        if(finalHolder.check.isChecked()) {///If the check box is checked

                            points += 10; //Add ten points

                            Log.d(TAG, "1.Number Of Points:" + points);
                            ResultView.setText(points + "");//display


                        }else{

                            points -= 10; //Take away

                            Log.d(TAG, "1.Number Of Points:" + points);
                            ResultView.setText(points + "");//display

                        }
                    }


                });
            }else{
                holder = (ViewHolder) convertView.getTag();
            }

            String string = TaskList.get(position);
            holder.check.setText(string + "");//Displays the tasks




            return convertView;
        }
    }




    //populateCheckView method
    private void populateCheckView(){
        Log.d(TAG, "populateCheckView: Display Data in the CheckboxView ");//Display Message in Logcat

        Cursor data = DTH.getTasks();// set data to function from Database TaskHelper
        ArrayList<String>TaskList = new ArrayList<>(); // Set TaskList to array list
        while(data.moveToNext()){
            TaskList.add(data.getString(1));
        }
        ListAdapter adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1,  TaskList); // Set List adapter to ArrayAdapter
        tListView.setAdapter(adapter);

        tListView.setAdapter(new ArrayAdapter<>(this, R.layout.listrow, R.id.textView2, TaskList)); // Set List adapter to ArrayAdapter

        tListView.setAdapter(new ArrayAdapter<>(this, R.layout.inner_checkview, R.id.checkBox1, TaskList)); // Set List adapter to ArrayAdapter

        dataAdapter = new CheckboxAdapter(this, R.layout.inner_checkview, TaskList);// Set dataAdapter to CheckBoxAdapter
        tListView.setAdapter(dataAdapter);



        //Set ListView to On Item Click listener
        tListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                String task = adapterView.getItemAtPosition(i).toString(); // Set String to get the string at the position
                Log.d(TAG, "onItemClick: You Clicked on " + task); //Display Message in Logcat

                Cursor data = DTH.getTaskID(task); // Set Data to get the task ID from Database Helper
                int taskID = -1; // Set taskId to -1
                while(data.moveToNext()){
                    taskID = data.getInt(0);
                }
                if(taskID > -1) { // If task id is greater then -1 then
                    Log.d(TAG, "onItemClick: The ID is: " + taskID); //Display Message Logcat
                    Intent editTaskScreenIntent = new Intent(CheckBoxActivity.this, EditClassActivity.class); // Set intent to new intent CheckBoxActivity to EditClassActivity
                    editTaskScreenIntent.putExtra("id", taskID);
                    editTaskScreenIntent.putExtra("Tasks", task);
                    startActivity(editTaskScreenIntent);
                }
                else{
                    toastMessage("No ID associated with that name"); // Display Message
                }
            }
        });



    }

    // Method for Toast Message
    private void toastMessage(String message){
        Toast.makeText(this,message, Toast.LENGTH_LONG ).show();
    }
}
