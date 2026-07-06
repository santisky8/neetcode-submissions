class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        # Define the map of each closing bracket
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # If the stack is empty or does'nt match requriements, it's invalid
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop() # Perfect match gets removed from the stack

            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matching
        return not stack
