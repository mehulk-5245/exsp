//check for issues if any in this code
import java.sql.*;

public class DatabaseUtils {
    private static final String URL = "jdbc:mysql://localhost:3306/mydatabase";
    private static final String USERNAME = "myuser";
    private static final String PASSWORD = "mypassword";

    public void executeSqlOperations() throws SQLException {
        
        Connection conn1 = DriverManager.getConnection(URL, USERNAME, PASSWORD);
        Connection conn2 = DriverManager.getConnection(URL, USERNAME, PASSWORD);

        // Get user input directly 
        String userInput = "John'; DROP TABLE users;--"; 

        
        String sql1 = "SELECT * FROM users WHERE username = '" + userInput + "'";
        String sql2 = "SELECT * FROM users WHERE username = '" + userInput + "'";

        // Create a statement and execute the query 
        Statement statement1 = conn1.createStatement();
        ResultSet resultSet1 = statement1.executeQuery(sql1);

        Statement statement2 = conn2.createStatement();
        ResultSet resultSet2 = statement2.executeQuery(sql2);

        // Process the results and store them in a list 
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

        // SQL Resource not closed properly 
        Statement statement3 = conn1.createStatement();
        ResultSet resultSet3 = statement3.executeQuery("SELECT COUNT(*) AS totalUsers FROM users");
        if (resultSet3.next()) {
            int totalUsers = resultSet3.getInt("totalUsers");
            System.out.println("Total users: " + totalUsers);
        }

        

        
        System.out.println("Database password: " + PASSWORD);

        
        try {
            // Some operation that might throw an exception
            throw new SQLException("Some SQL Exception");
        } catch (SQLException e) {
            // Empty catch block (no proper error handling)
        }
    }
}
