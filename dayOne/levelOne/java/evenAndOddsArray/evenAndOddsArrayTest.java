import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class evenAndOddsArrayTest {

    @Test
    public void testTheEvenElementsCount(){

        int[] input = {1,3,2,4,5,6,7,8}; 
        int expected = 4;
        int actual = evenAndOddsArray.checkLengthOfEvenArray(input);
        assertEquals(expected, actual);

    }

    @Test
    public void testTheOddElementsCount(){

        int[] input = {1,3,2,4,5,6,7,8}; 
        int expected = 4;
        int actual = evenAndOddsArray.checkLengthOfOddArray(input);
        assertEquals(expected, actual);

    }

    @Test
    public void testTheSortingOfEvenElements(){

        int[] input = {1,3,2,4,5,6,7,8}; 
        int[] expected = {2,4,6,8};
        int[] actual = evenAndOddsArray.collectEvenElements(input);
        assertArrayEquals(expected, actual);

    }

    @Test
    public void testTheSortingOfOddElements(){

        int[] input = {1,3,2,4,5,6,7,8}; 
        int[] expected = {1,3,5,7};
        int[] actual = evenAndOddsArray.collectOddElements(input);
        assertArrayEquals(expected, actual);

    }

    @Test
    public void testTheReturnOfSplitArray(){

        int[] input = {1,3,2,4,5,6,7,8}; 
        int[][] expected = {{2,4,6,8},{1,3,5,7}};
        int[][] actual = evenAndOddsArray.splitArray(input);
        assertArrayEquals(expected, actual);

    }

}
