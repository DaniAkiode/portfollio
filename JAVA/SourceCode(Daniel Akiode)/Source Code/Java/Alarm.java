package TDCollections.premix;
////Imports Contents and Widgets
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Vibrator;
import android.widget.Toast;
//The alarm class will extend to the BroadcastReciver to get the alarm
public class Alarm extends BroadcastReceiver {
    @Override

    //Display message and vibrates phone for 1000 milliseconds the function is called
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context, "ALARM.......", Toast.LENGTH_LONG).show();
        Vibrator v = (Vibrator)context.getSystemService(context.VIBRATOR_SERVICE);
        v.vibrate(1000);

    }
}
