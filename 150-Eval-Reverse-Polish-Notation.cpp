/*
Problem:
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
*/

/* 
Explanation:
Even though this is a Medium problem on LeetCode, this is problem is not very difficult.
It largely is requires knowledge on Reverse Polish Notation form and an of understanding how they relate
to Stack data stuctures.

To solve this problem, simply iterate through each token. 
If the token is a number, convert it from a string to a integer and add it to the stack.
If it is one of the operands, pop two integers from the stack, complete the operation, and add
the resulting operation. The whole operation of Reverse Polish Notation functions as a simple stack!

Time Complexity: 0(n)

*/

#include <string>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for(auto& t : tokens) 
            if(t == "+" || t == "-" || t == "*" || t == "/") {
                int op1 = s.top(); 
                s.pop();
                int op2 = s.top(); 
                s.pop();
                if(t == "+") op1 = op2 + op1;
                if(t == "-") op1 = op2 - op1;
                if(t == "/") op1 = op2 / op1;
                if(t == "*") op1 = op2 * op1;   
                s.push(op1);
            }
            else s.push(stoi(t));    // stoi - converts from string to int     
        return s.top(); 
    }
};
