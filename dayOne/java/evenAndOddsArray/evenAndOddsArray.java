import java.util.Arrays;

public class evenAndOddsArray {

    public static int checkLengthOfEvenArray(int[] numbers) {

        int evenElementsCount = 0;
        for(int element : numbers){
            
            if(element % 2 == 0){
        
                evenElementsCount++;

            } 

        }

        return evenElementsCount;
    }

    public static int checkLengthOfOddArray(int[] numbers) {

        int oddElementsCount = 0;
        for(int element : numbers){
            
            if(element % 2 != 0){
        
                oddElementsCount++;

            } 

        }

        return oddElementsCount;
    }

    public static int[] collectEvenElements(int[] numbers) {
        
        int count = checkLengthOfEvenArray(numbers);

        int[] evenElements = new int[count];

        int evenIndex = 0;

        for(int element : numbers) {
        
            if(element % 2 == 0) {
        
                evenElements[evenIndex] = element;
                evenIndex++;

            }   

        }    
    
        return evenElements;

    }

    public static int[] collectOddElements(int[] numbers) {
        
        int count = checkLengthOfOddArray(numbers);

        int[] oddElements = new int[count];

        int oddIndex = 0;

        for(int element : numbers) {
        
            if(element % 2 != 0) {
        
                oddElements[oddIndex] = element;
                oddIndex++;

            }   

        }    
    
        return oddElements;

    }

    public static int[][] splitArray(int[] numbers) {

        int[] evenElements =   collectEvenElements(numbers); 

        int[] oddElements =   collectOddElements(numbers);    

        int[][] splitArray = {evenElements, oddElements};
        return splitArray;

    }

}
