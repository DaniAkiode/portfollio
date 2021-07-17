package TDCollections.premix;
//Imports
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
//MenuActivity Class
public class MenuActivity extends AppCompatActivity {
    //Create Activity
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
        // Set variable to  find view by id from layout
        Button LoadSavedListBtn = findViewById(R.id.LoadSavedListBtn);
        //Set Button to OnClickListener
        LoadSavedListBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent startIntent = new Intent(getApplicationContext(), ViewTheToDoLists.class); // Set intent new intent
                startActivity(startIntent);// Start new Activity
            }
        });

        // Set variable to  find view by id from layout
        Button CreateNewListBtn = findViewById(R.id.CreateNewListBtn);
        //Set Button to OnClickListener
        CreateNewListBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent startIntent = new Intent(getApplicationContext(), DateActivity.class);// Set intent new intent
                startActivity(startIntent);// Start new Activity
            }
        });

    }
}
