import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class palindromicArrayTest {

    @Test
    public void testThecheckIfArrayIsAPalindromeFunctionWithAPalindrome(){

        int[] input = {45, 0, 8, 0, 45};

        boolean expected = true;

        boolean actual = palindromicArray.checkIfArrayIsAPalindrome(input);

        assertEquals(expected, actual);


    }

    @Test
    public void testThecheckIfArrayIsAPalindromeFunctionWithANonPalindrome(){

        int[] input = {3, 0, 8, 0, 45};

        boolean expected = false;

        boolean actual = palindromicArray.checkIfArrayIsAPalindrome(input);

        assertEquals(expected, actual);
    
    }


} 
