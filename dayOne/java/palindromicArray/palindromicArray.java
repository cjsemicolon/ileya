public class palindromicArray {

    public static boolean checkIfArrayIsAPalindrome(int[] numbers) {

        int begining = 0;
        int end = numbers.length - 1;

        while (begining < end) {

            if (numbers[begining] != numbers[end]) {
                return false;
            }

            begining++;
            end--;
        }

        return true;
    }

}
