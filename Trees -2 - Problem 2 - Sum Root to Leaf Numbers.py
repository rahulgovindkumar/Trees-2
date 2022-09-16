"""
 FAANMG Problem #47 {Medium}

129. Sum Root to Leaf Numbers

Time Complexity : O(N)

Space Complexity : O(H)


Did this code successfully run on Leetcode : Yes
  
Iterative Approach

We are using 2 Stack to store the node and the current number generated

Outer loop will run untill root is not null or the stack is not empty

inside trhe loop we will keep on going to root.left
  - gemenrate the number by currNum*10 + the value
  - push the number and the node to the stack
  
pop the statck values : node and the curr Number

if its the leaf node then add it to teh result
and move to root.right





@name: Rahul Govindkumar_RN27JUL2022
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        st = collections.deque()
        
        numSt = collections.deque()
        
        currNum = 0
        result =0
        
        while( root or st):
            
            while(root):
                currNum = currNum * 10 + root.val
                
                st.append(root)
                numSt.append(currNum)
                
                root = root.left
                
            #Pop the stack
            
            root = st.pop()
            
            currNum = numSt.pop()
            
            if(root.left is None and root.right is None):
                result += currNum
            
            root =root.right
        
        
        return result
            
            
"""
 FAANMG Problem #47 {Medium}

129. Sum Root to Leaf Numbers

Time Complexity : O(N)

Space Complexity : O(H)


Did this code successfully run on Leetcode : Yes
  
Recursive Approach






@name: Rahul Govindkumar_RN27JUL2022
"""
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __int__(self):
        self.result = 0
    
    def helper(self,root, currNum):
        
        #base
        if(root is None):
            return
        
        #logic
        
        currNum = (currNum*10 + root.val)
        #check leaf
        if(root.left is None and root.right is None):
            self.result = self.result + currNum
            
        
        self.helper(root.left , currNum)
        self.helper(root.right, currNum)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        self.helper(root,0)
        
        return self.result
            
            
        
        
        