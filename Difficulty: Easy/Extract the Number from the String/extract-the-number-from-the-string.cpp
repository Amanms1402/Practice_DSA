//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    long long ExtractNumber(string sentence) {
        long long int result = 0;
        bool flag = 0;
        bool has9 = 0;
        long long int temp = 0;
        for(char i:sentence){
            if (i>=48 && i<=57 && !flag)
            {
                flag = 1;
                has9 = 0;
                temp = 0;
            }
            else if(i<48 || i>57 && flag){
                flag = 0;
                if(!has9 && temp > result) result = temp;
            }
            if(flag) {
                if (i == 57) has9 = 1;
                temp = temp*10 + i%48;
            }
        }
        if (!has9 && temp > result) result = temp;
        return (result == 0)? -1 : result;
    }
};

//{ Driver Code Starts.
int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    string tc;
    getline(cin, tc);
    t = stoi(tc);
    while (t--) {
        string s;
        getline(cin, s);

        Solution ob;
        cout << ob.ExtractNumber(s) << "\n";
    }

    return 0;
}

// } Driver Code Ends