import org.junit.Test;
import static org.junit.Assert.*;

public class CalculatorTest {
    
    private Calculator calculator;
    
    @Test
    public void testAdd() {
        calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }
    
    @Test
    public void testSubtract() {
        calculator = new Calculator();
        int result = calculator.subtract(5, 2);
        assertEquals(3, result);
    }
    
    @Test
    public void testMultiply() {
        calculator = new Calculator();
        int result = calculator.multiply(4, 3);
        assertEquals(12, result);
    }
    
    @Test
    public void testDivide() {
        calculator = new Calculator();
        int result = calculator.divide(10, 2);
        assertEquals(5, result);
    }
    
    @Test
    public void testAddWithNegativeNumbers() {
        calculator = new Calculator();
        int result = calculator.add(-2, -3);
        assertEquals(-5, result);
    }
    
    @Test
    public void testSubtractWithNegativeNumbers() {
        calculator = new Calculator();
        int result = calculator.subtract(-5, -2);
        assertEquals(-3, result);
    }
    
    @Test
    public void testMultiplyWithNegativeNumbers() {
        calculator = new Calculator();
        int result = calculator.multiply(-4, -3);
        assertEquals(12, result);
    }
    
    @Test
    public void testDivideWithNegativeNumbers() {
        calculator = new Calculator();
        int result = calculator.divide(-10, -2);
        assertEquals(5, result);
    }
}
