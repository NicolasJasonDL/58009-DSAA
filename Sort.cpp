#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
	int num[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int x = sizeof(num)/sizeof(num[0]);
	
	sort (num, num + x, greater<int>());
	
	cout<<"Array after sorting in descending order: \n";
	
	for (int i = 0; i< x; ++i)
	cout<< num[i] << " ";
	
	
	
	return 0;
}
