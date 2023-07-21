import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class RedundantVulnerableSqlExample {
    public static void main(String[] args) {
        try {
            // Assuming you have a local MySQL database with a table called 'users'
            String url = "jdbc:mysql://localhost:3306/mydatabase";
            String username = "myuser";
            String password = "mypassword";

            // Redundant connection creation (code redundancy issue)
            Connection conn1 = DriverManager.getConnection(url, username, password);
            Connection conn2 = DriverManager.getConnection(url, username, password);

            // Get user input directly (unsafe - susceptible to SQL injection)
            String userInput = "John'; DROP TABLE users;--"; // Malicious user input

            // Redundant SQL query creation (code redundancy issue)
            String sql1 = "SELECT * FROM users WHERE username = '" + userInput + "'";
            String sql2 = "SELECT * FROM users WHERE username = '" + userInput + "'";

            // Create a statement and execute the query (redundant code)
            Statement statement1 = conn1.createStatement();
            ResultSet resultSet1 = statement1.executeQuery(sql1);

            Statement statement2 = conn2.createStatement();
            ResultSet resultSet2 = statement2.executeQuery(sql2);

            // Process the results and store them in a list (memory redundancy issue)
            List<String> usersList1 = new ArrayList<>();
            while (resultSet1.next()) {
                String usernameResult = resultSet1.getString("username");
                usersList1.add(usernameResult);
            }

            List<String> usersList2 = new ArrayList<>();
            while (resultSet2.next()) {
                String usernameResult = resultSet2.getString("username");
                usersList2.add(usernameResult);
            }

            // Close the resources (memory not released properly - potential memory leak)
            resultSet1.close();
            statement1.close();
            conn1.close();

            resultSet2.close();
            statement2.close();
            conn2.close();

            // Perform some other memory-intensive operations (further memory usage)

            // The 'usersList1' and 'usersList2' data is no longer needed,
            // but they remain in memory without being explicitly cleared,
            // leading to memory redundancy and potential performance issues.

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
