
//#create a function that collects password and the shift
//#initialize a variable to collect the encrypted password
//#loop through password to verify if a character is an alphabet
//#convert the letter to its ascii value
//#shift the ascii value by shift amount
//#if you run out of alphabets start from the begining
//#convert shifted ascii value back to alphabet
//#add shifted alphabet to the encrypted password variable

public class ceaserCipherEncryption {

    public static String encryption(String password, int shift) {

        String encryptedPassword = "";

        for (char character : password.toCharArray()) {

            if (Character.isLetter(character)) {

                char firstLetter;

                if (Character.isLowerCase(character)) {
                    firstLetter = 'a';
                } else {
                    firstLetter = 'A';
                }

                int position = character - firstLetter;

                int newPosition = (position + shift) % 26;

                char encryptedCharacter = (char) (newPosition + firstLetter);

            
                encryptedPassword += encryptedCharacter;

            } else {

                encryptedPassword += character;
            }
        }

        return encryptedPassword;
    }

}

