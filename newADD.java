import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class SQLEX {
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

            // SQL Resource not closed properly (resource leak issue)
            Statement statement3 = conn1.createStatement();
            ResultSet resultSet3 = statement3.executeQuery("SELECT COUNT(*) AS totalUsers FROM users");
            if (resultSet3.next()) {
                int totalUsers = resultSet3.getInt("totalUsers");
                System.out.println("Total users: " + totalUsers);
            }

            // Unclosed resources (potential memory leak)
            // ResultSet resultSet2 and statement2 are not closed.

            // Perform some other CPU-intensive operations (inefficient CPU usage)

            // The 'usersList1' and 'usersList2' data is no longer needed,
            // but they remain in memory without being explicitly cleared,
            // leading to memory redundancy and potential performance issues.

            // Password displayed in logs (security vulnerability)
            System.out.println("Database password: " + password);

            // Poor exception handling (inefficient and potentially insecure)
            try {
                // Some operation that might throw an exception
                throw new SQLException("Some SQL Exception");
            } catch (SQLException e) {
                // Empty catch block (no proper error handling)
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
