#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return 0;

        sort(nums.begin(), nums.end());
        int count = 0;

        // Fix the largest side at index k
        for (int k = n - 1; k >= 2; --k) {
            int i = 0, j = k - 1;
            while (i < j) {
                if (nums[i] + nums[j] > nums[k]) {
                    count += (j - i);
                    --j;
                } else {
                    ++i;
                }
            }
        }

        return count;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 2, 3, 4}; // Example input
    int result = sol.triangleNumber(nums);
    cout << "Number of valid triangles: " << result << endl;
    return 0;
}
