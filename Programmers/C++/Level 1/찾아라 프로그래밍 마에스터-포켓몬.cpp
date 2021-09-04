#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 1;
    int nums_full = nums.size();
    int nums_half = nums_full/2;
    
    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(),nums.end()),nums.end());
    
    int nums_unique = nums.size();
    if (nums_unique >= nums_half)
        answer = nums_half;
    else
        answer = nums_unique;
    
    return answer;
}
