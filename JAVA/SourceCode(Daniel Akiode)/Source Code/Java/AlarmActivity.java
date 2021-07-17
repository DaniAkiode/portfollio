package TDCollections.premix;
//Imports

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


//Public class AlarmActivity extends to AppCompatActivity
public class AlarmActivity extends AppCompatActivity {

    //Declare Variables
    Button btnSet;
    EditText EtTkAlarm;
    //Function OnCreate create the Activity
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_alarm);// Set activity to the activity_alarm layout

        //Set Variables to id in the layout
        btnSet = findViewById(R.id.btnSet);
        EtTkAlarm = findViewById(R.id.EtTkAlarm);

        //Set button to onClickListener
        btnSet.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(EtTkAlarm.length() == 0) {
                    toastMessage("Please Enter a Number");
                } else {
                    int clock = Integer.parseInt(EtTkAlarm.getText().toString());//Sets Integer clock to intput from user
                    Intent intent = new Intent(AlarmActivity.this, Alarm.class); // Set intent from AlarmActivity to Alarm to get information
                    PendingIntent PI = PendingIntent.getBroadcast(getApplicationContext(),0, intent, 0); //Gets broadcast from pending intent (Alarm)
                    AlarmManager ALM = (AlarmManager)getSystemService(ALARM_SERVICE); //Gets alarm service from Alarm Manager that would count down the integer to 0
                    ALM.set(AlarmManager.RTC_WAKEUP, System.currentTimeMillis()+clock*1000,PI); //Converts millseconds to seconds.
            }}
        });


    }
    private void toastMessage(String message){
        Toast.makeText(this,message, Toast.LENGTH_LONG ).show();
    }
}

