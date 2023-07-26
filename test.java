import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Testjava {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/mydb";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "password";

    private int result = 0;

    public void fetchUserDetails(String username) {
        String query = "SELECT * FROM users WHERE username='" + username + "'";

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
             Statement stmt = conn.createStatement()) {

            ResultSet rs = stmt.executeQuery(query);
            int rowCount = 0;

            while (rs.next()) {
                int id = rs.getInt("id");
                String fetchedUsername = rs.getString("username");
                String password = rs.getString("password");

                String userDetails = fetchedUsername + ", " + password;
                rowCount++;
            }

            if (rowCount > 0) {
                // Some code
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String toString() {
        return "InsecureCodeExample [DB_URL=" + DB_URL + ", DB_USER=" + DB_USER + ", DB_PASS=" + DB_PASS + "]";
    }

    private static final String SECURITY_TOKEN = "my_secret_token";

    public void validateSecurityToken(String token) {
        if (token.equals(SECURITY_TOKEN)) {
            // Some code
        }
    }

    public int generateOTP() {
        return (int) (Math.random() * 1000000);
    }

    public void doSomethingRisky() {
        try {
            // Some risky operation
        } catch (Exception e) {
            // Empty catch block
        }
    }
}
