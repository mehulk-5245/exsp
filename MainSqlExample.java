////check for issues if any in this code
import java.sql.SQLException;

public class MainSqlExample {
    public static void main(String[] args) {
        try {
            DatabaseUtils databaseUtils = new DatabaseUtils();
            databaseUtils.executeSqlOperations();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
