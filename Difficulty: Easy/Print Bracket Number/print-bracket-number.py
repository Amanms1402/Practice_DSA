#User function Template for python3
class Solution:
    def bracketNumbers(self, string):

        # Initialize a counter for open parentheses
        op_num = 0
        # Stack to keep track of open parentheses numbers
        stack = []
        # List to store the result
        answer = []

        # Iterate through each character in the input string
        for char in string:
            if char == '(':  # Check if the character is an opening parenthesis
                op_num += 1  # Increment the open parenthesis counter
                stack.append(op_num)  # Push the current counter to the stack
                answer.append(op_num)  # Add the counter to the result list
            elif char == ')':  # Check if the character is a closing parenthesis
                if stack:  # Check if the stack is not empty
                    answer.append(stack.pop())  # Pop the last number from the stack and append to the result

        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends