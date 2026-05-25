import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class returningPerfectSquaresTest {

    @Test
    public void testThatTheGetTheNumberOfPerfectSquaresFunctionWorks(){

        int[] input = {4, 7, 9, 10, 16, 18};

        int expected = 3;

        int actual = returningPerfectSquares.getTheNumberOfPerfectSquares(input);

        assertEquals(expected, actual);

    }

    @Test
    public void testThatReturningPerfectSquaresFunctionWorks(){

        int[] input = {4, 7, 9, 10, 16, 18};

        int[] expected = {4, 9, 16};

        int[] actual = returningPerfectSquares.returnPerfectSquares(input);

        assertArrayEquals(expected, actual);

    }

}
