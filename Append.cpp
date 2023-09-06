#include <iostream>
#include <vector>

using namespace std;
 
int main()
{
	
    vector<int> num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
	int x = 27;
 
    num.push_back(x);
 
    for (int &i: num) 
	{
        cout << i << " ";
    }
 
    return 0;
}
