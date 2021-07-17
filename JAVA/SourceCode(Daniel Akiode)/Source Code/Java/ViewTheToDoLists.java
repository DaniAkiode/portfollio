package TDCollections.premix;
//import

import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

//ViewTheToDoLists Class
public class ViewTheToDoLists extends AppCompatActivity {
    //Declare Variables
    private static final  String TAG = "ViewTheToDoLists";

    DatabaseHelper DBHelper;

    private ListView mListView;

    //Create Activity
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.viewlists_layout);
        //Set Variable to find view by id
        mListView = findViewById(R.id.ListView);
        //Set Variable to New DatabaseHelper
        DBHelper = new DatabaseHelper(this);

    }
    //This function refresh list when populated
    @Override
    protected void onPostResume() {
        super.onPostResume();
        populateListView(); //Call Function
    }

    //This function would populated the list view
    private void populateListView() {
        Log.d(TAG, "populateListView: Display data in the ListView ");//Display on logcat

        Cursor data = DBHelper.getContents();//Set data to call the function
        ArrayList<String> ListOnList = new ArrayList<>(); //Set Variable to new Array List
        while(data.moveToNext()){
            ListOnList.add(data.getString(1));
        }
        ListAdapter adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, ListOnList); //Set adapter to layout
        mListView.setAdapter(adapter);

        mListView.setAdapter(new ArrayAdapter<>(this, R.layout.listrow, R.id.textView2, ListOnList)); //Set adapter to layout
        //Set ListView to onItemClickListener
        mListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString(); //Declare and set string to get the item at position i
                Log.d(TAG, "onItemClick: You Clicked On " + item); //Display on logcat

                Cursor data = DBHelper.getItemID(item);//Call function in Database Helper

                int ItemID = -1; //Set Variable to -1
                while(data.moveToNext()){
                    ItemID = data.getInt(0);
                }

                if(ItemID > -1){ //If ItemID is over -1 then the app would transition to a new Activity
                    Log.d(TAG, "OnItemClick: The ID is, " + ItemID);
                    Intent CheckScreenIntent = new Intent(ViewTheToDoLists.this, CheckBoxActivity.class );
                    CheckScreenIntent.putExtra("ID",ItemID);
                    CheckScreenIntent.putExtra("ITEM", item);
                    startActivity(CheckScreenIntent);
                }
                else{ //Otherwise
                    toastMessage("No ID associated with that name"); //Display Message
                }


            }
        });

    }

    private void toastMessage(String message){
        Toast.makeText(this,message, Toast.LENGTH_LONG).show();
    }
}
