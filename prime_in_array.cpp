i#include<iostream>
using namespace std;
int main()
{
	int a[20],i,j,f,n;
	cout<<"enter elements"<<endl;
	for(i=0;i<20;i++)
    {
    	cin>>a[i];
	}
	for(i=0;i<20;i++)
	{
		n=a[i];
		f=0;
		for(j=2;j<n;j++)
		{
			if(n%j==0)
			{
				f=1;
				break;
			}
			
		}
		if(f==0)
			cout<<n<<"is prime"<<endl;
	}
	return 0;
	
}

