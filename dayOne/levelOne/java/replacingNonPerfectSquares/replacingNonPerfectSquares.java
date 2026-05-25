public class replacingNonPerfectSquares {

    public static int[] replaceNonPerfectSquares(int[] numbers) {

        int[] replacedNonPerfectSquares = new int[numbers.length];

        for(int element = 0; element < numbers.length; element++) {

            int squareRoot = (int)Math.sqrt(numbers[element]);

            if(squareRoot * squareRoot == numbers[element]) {

                replacedNonPerfectSquares[element] = numbers[element];

            }

            else{

                replacedNonPerfectSquares[element] = -1;    
                    
            }

        }
    
        return replacedNonPerfectSquares;

    }

}
