class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
        int n = matrix.size();
        int l = 0, r = n - 1;

        while (l < r){

            for (int i = 0; i < (r-l); i++){
                int top = l, bottom = r;
                int topLeft = matrix[top][l+i];

                // replace the top left with the bottom left
                matrix[top][l+i] = matrix[bottom-i][l];
                matrix[bottom-i][l] = matrix[bottom][r-i];
                matrix[bottom][r-i] = matrix[top+i][r];
                matrix[top+i][r] = topLeft;
            }

            l += 1;
            r -= 1;
        }
        
        return;
    }
};
