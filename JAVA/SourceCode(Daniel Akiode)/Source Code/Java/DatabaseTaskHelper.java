package TDCollections.premix;
//import
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

///Database TaskHelper extends to SQliteOpenHelper

public class DatabaseTaskHelper extends SQLiteOpenHelper {
    //Declare Columns
    private static final String TAG = "DatabaseTaskHelper";
    private static final String TASK_TABLE = "task_table";
    private static final String COL3 = "id";
    private static final String COL4 = "Tasks";
    private static final String COL5 =  "Points";

    /// Starts Class
    public DatabaseTaskHelper(Context context) {super (context, TASK_TABLE, null, 1);}

    /// Creates Table
    @Override
    public void onCreate(SQLiteDatabase db) {
        String BuildTable2 = "CREATE TABLE " + TASK_TABLE + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, " + COL4 + " TEXT, " + COL5 + " INTEGER ) ";
        db.execSQL(BuildTable2);

    }

    /// Drop if the table exists

    @Override
    public void onUpgrade(SQLiteDatabase db, int i, int il) {
        db.execSQL("DROP TABLE IF EXISTS " + TASK_TABLE );
        onCreate(db);


    }

    /// Adds Tasks into the Table

    public boolean addTasks(String item2) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues2 = new ContentValues();
        contentValues2.put(COL4, item2);

        Log.d(TAG, "addData Adding " + item2 + "to" + TASK_TABLE);

        long result = db.insert(TASK_TABLE, null, contentValues2);

        if (result == -1){
            return false;
        }else{
            return true;
        }

    }


    /// Gets the Data from the table
    public Cursor getTasks() {
        SQLiteDatabase db = this.getWritableDatabase();
        String query = "SELECT * FROM " + TASK_TABLE;
        Cursor data = db.rawQuery(query, null);
        return data;
    }

    /// Gets Task ID from Table
    public Cursor getTaskID(String task){
        SQLiteDatabase db = this.getWritableDatabase();
        String query = "SELECT " + COL3 + " FROM " +  TASK_TABLE + " WHERE " + COL4 + " = '" + task + "'";
        Cursor data = db.rawQuery(query, null);
        return data;
    }

    // Updates Task in the Table

    public void updateTask(String newTask, int id, String OldTask){
        SQLiteDatabase db = this.getWritableDatabase();
        String query = "UPDATE " + TASK_TABLE + " SET " + COL4 + " = '" + newTask + "' WHERE " + COL3 + "='" + id + "'" + " AND " + COL4 + " = '" + OldTask + "'";
        Log.d(TAG, "updateName: query: " + query);
        Log.d(TAG, "updateName: Setting name to " + newTask);
        db.execSQL(query);
    }

    //Delete task from table

    public void deleteTask(int id, String task){
        SQLiteDatabase db = this.getWritableDatabase();
        String query ="DELETE FROM " + TASK_TABLE + " WHERE " + COL3 + " = '" + id + "'" + " AND " + COL4 + " = '" + task + "'";
        Log.d(TAG, "deleteTask: query:" + query);
        Log.d(TAG, "deleteTask: Deleting " + task + "from database");
        db.execSQL(query);
    }






}
