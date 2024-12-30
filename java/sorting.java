import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[][] arr = {{5, 2}, {1, 9}, {3, 7}, {1, 5}};
        
        // Sorting based on the first element
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> list = new ArrayList<>();
        list.add(new int[]{5, 2});
        list.add(new int[]{1, 9});
        list.add(new int[]{3, 7})
        list.add(new int[]{1, 5});
        
        // Sorting based on the first element
        Collections.sort(list, (a, b) -> Integer.compare(a[0], b[0]));

        // Printing sorted array
        for (int[] pair : arr) {
            System.out.println(Arrays.toString(pair));
        }
    }
}

/*
Arrays.sort(arr, (a, b) -> Integer.compare(b[0], a[0]));

Collections.sort(list, (a, b) -> Integer.compare(b[0], a[0]));

*/