public boolean[][] getVisited(int n, int m) {
    boolean[][] visited = new boolean[m][n]; // Initialize a new boolean matrix

    // Nested loop to initialize all elements to false
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            visited[i][j] = false; // Set each element to false
        }
    }

    return visited; // Return the initialized boolean matrix
}


// ----------------------------------------------------------

// to optimize this we will use Arraty.fill() for filling each row

import java.util.Arrays;

public boolean[][] getVisited(int n, int m) {
    boolean[][] visited = new boolean[m][n]; // Initialize a new boolean matrix

    // Fill the entire matrix with false values
    for (boolean[] row : visited) {
        Arrays.fill(row, false);
    }

    return visited; // Return the initialized boolean matrix
}


// ----------------------------------------------------------

/**
 The method utilizing Arrays.fill() is already quite efficient for initializing a 2D boolean array with false values. However, if you're looking for even more efficiency, 
 you might consider using java.util.BitSet instead of a 2D boolean array.

BitSet represents a set of bits or flags, and it can be more memory-efficient than a 2D boolean array, 
especially if the matrix is sparse (contains mostly false values).
 */

import java.util.BitSet;

public BitSet getVisited(int n, int m) {
    int size = n * m;
    BitSet visited = new BitSet(size);
    visited.set(0, size, false); // Set all bits to false
    return visited;
}
