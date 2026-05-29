import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ceaserCipherEncryptionTest {

    @Test
    public void testFunctionEncryptsLowercaseLetters() {

        String password = "dog";
        int shift = 3;

        String expected = "grj";

        String actual = ceaserCipherEncryption.encryption(password, shift);

        assertEquals(expected, actual);
    }

    @Test
    public void testEncryptsUppercaseLetters() {

        String password = "DOG";
        int shift = 3;

        String expected = "GRJ";

        String actual = ceaserCipherEncryption.encryption(password, shift);

        assertEquals(expected, actual);
    }

    @Test
    public void testWrapsAroundAlphabet() {

        String password = "XYZ";
        int shift = 3;

        String expected = "ABC";

        String actual = ceaserCipherEncryption.encryption(password, shift);

        assertEquals(expected, actual);
    }

    @Test
    public void testKeepsNumbersAndSymbols() {

        String password = "Dog123!";
        int shift = 3;

        String expected = "Grj123!";

        String actual = ceaserCipherEncryption.encryption(password, shift);

        assertEquals(expected, actual);
    }

    @Test
    public void testDecryptsWithNegativeShift() {

        String password = "Grj";
        int shift = -3;

        String expected = "Dog";

        String actual = ceaserCipherEncryption.encryption(password, shift);

        assertEquals(expected, actual);
    }
}
