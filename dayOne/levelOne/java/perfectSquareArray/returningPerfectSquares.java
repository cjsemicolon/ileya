public class returningPerfectSquares {

    public static int getTheNumberOfPerfectSquares(int[] numbers) {
    
        int count = 0;
        
        for(int element : numbers){

            int squareRoot = (int)Math.sqrt(element);

            if(squareRoot * squareRoot == element) {

                count++;    

            }

        }
        
        return count;    

    }

    public static int[] returnPerfectSquares(int[] numbers) {

        int count = getTheNumberOfPerfectSquares(numbers);

        int[] perfectSquares = new int[count];

        int index = 0;

        for(int element : numbers) {

            int squareRoot = (int)Math.sqrt(element);
        
            if(squareRoot * squareRoot == element) {

                perfectSquares[index] = element;

                index++;    

            }

        }

    return perfectSquares;
        
    }



}
