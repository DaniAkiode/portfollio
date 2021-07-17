package TDCollections.premix;

//Imports

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
//DatabaseHelper class extends to SQLiteOpenHelper
public class DatabaseHelper extends SQLiteOpenHelper {

    //Declare Columns
    public static final String TO_DO_LIST = "ToDoLisT";
    public static final String COL1 = "ID";
    public static final String COL2 = "ITEM1";

    //Starts database helper
    public DatabaseHelper (Context context) {super (context, TO_DO_LIST, null, 1);}



    //Creates Table
    @Override
    public void onCreate(SQLiteDatabase db) {

        String BuildTable = "CREATE TABLE " + TO_DO_LIST + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, " + COL2 + " TEXT)";
        db.execSQL(BuildTable);

    }
    //Drops table if it exists
    @Override
    public void onUpgrade(SQLiteDatabase db, int i, int il) {
        db.execSQL("DROP TABLE IF EXISTS " + TO_DO_LIST);
        onCreate(db);
    }
    //Adds data in the database
    public boolean addData(String item1){
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COL2, item1);

        long result = db.insert(TO_DO_LIST, null, contentValues);

        if (result == -1){
            return false;
        } else {
            return true;

        }
    }

    //Gets Data from the table

    public Cursor getContents() {
        SQLiteDatabase db = this.getWritableDatabase();
        Cursor data = db.rawQuery("SELECT * FROM " + TO_DO_LIST, null);
        return data;
    }
    // Get item ID
    public Cursor getItemID(String item) {
        SQLiteDatabase db = this.getWritableDatabase();
        String query = "SELECT " + COL1 + " FROM " + TO_DO_LIST + " WHERE " + COL2 + " = '" + item + "'";
        Cursor data = db.rawQuery(query, null);
        return data;
    }

}
