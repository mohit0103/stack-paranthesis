#include <iostream>
using namespace std;
int top;
void check (char str[], int n, char stack[])
{
    for(int i=0; i<n; i++){
        if (str[i] == '(')
        {
            top = top + 1;
            stack [top] = '(';
        }
        if (str[i] == ')' && stack[top] == '(')
        {
            top = top - 1;
        }
    }
    if (top == -1)
    cout<<"string is balanced"<<endl;
    else
    cout<<"string is unbalanced"<<endl;
}
int main()
{
    char str[] = {'(','a','+','(','b','-','c',')',')'};
    char str1[] = {'(','(','a','+','b',')'};
    char stack [20];
    top =-1;
    check (str, 9, stack);
    top =-1;
    check (str1, 6, stack);
    return 0;
    }
