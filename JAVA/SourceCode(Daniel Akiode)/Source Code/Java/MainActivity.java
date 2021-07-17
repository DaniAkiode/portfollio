package TDCollections.premix;
//Import
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
//Main Activity Class
public class MainActivity extends AppCompatActivity {

    //Creates Activity class
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //Declare and set button to find the View by ID from the Activity layout
        Button StartBtn = findViewById(R.id.StartBtn);
        //Set Button to OnClickListener
        StartBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent startIntent = new Intent(getApplicationContext(), MenuActivity.class); // Set intent new intent
                startActivity(startIntent);// Start new Activity
            }
        });
    }
}
