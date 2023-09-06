#include <iostream>

using namespace std;

int main()
{
	int num[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int arrSize = sizeof(num)/sizeof(num[0]);
	
	cout << "The size of array is: " <<arrSize;
	return 0;
}
