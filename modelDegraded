import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

 

public class MoreIssuesSqlExample {
    public static void main(String[] args) {
        try {
            // Assuming you have a local MySQL database with a table called 'users'
            String url = "jdbc:mysql://localhost:3306/mydatabase";
            String username = "myuser";
            String password = "mypassword";

 

          
            Connection conn1 = DriverManager.getConnection(url, username, password);
            Connection conn2 = DriverManager.getConnection(url, username, password);

 

            
            String userInput = "John'; DROP TABLE users;--"; // Malicious user input

 

            
            String sql1 = "SELECT * FROM users WHERE username = '" + userInput + "'";
            String sql2 = "SELECT * FROM users WHERE username = '" + userInput + "'";

 

            
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

 

          
            Statement statement3 = conn1.createStatement();
            ResultSet resultSet3 = statement3.executeQuery("SELECT COUNT(*) AS totalUsers FROM users");
            if (resultSet3.next()) {
                int totalUsers = resultSet3.getInt("totalUsers");
                System.out.println("Total users: " + totalUsers);
            }

 

            
            System.out.println("Database password: " + password);

 

            
            try {

                throw new SQLException("Some SQL Exception");
            } catch (SQLException e) {

            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
