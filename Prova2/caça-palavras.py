class Solution(object):
   def exist(self, board, word):
      n =len(board)
      m = len(board[0])
      for i in range(n):
         for j in range(m):
            if word[0] == board[i][j]:
               if self.find(board,word,i,j):
                  return True
      return False
   def find(self, board,word,row,col,i=0):
      if i== len(word):
         return True
      if row>= len(board) or row <0 or col >=len(board[0]) or col<0 or word[i]!=board[row][col]:
         return False
      board[row][col] = '*'
      res = self.find(board,word,row+1,col,i+1) or self.find(board,word,row-1,col,i+1) or self.find(board,word,row,col+1,i+1) or self.find(board,word,row,col-1,i+1)
      board[row][col] = word[i]
      return res
ob1 = Solution()

palavra= str(input(""))
print(ob1.exist([['A', 'T', 'O', 'L', 'E', 'P', 'S', 'J'],['B', 'J', 'L', 'U', 'T', 'M', 'S', 'I'],
 ['A', 'I', 'U', 'R', 'O', 'U', 'P', 'A'],
 ['C', 'L', 'T', 'S', 'M', 'A', 'T', 'E'], 
 ['A', 'J', 'L', 'O', 'A', 'R', 'M', 'A'],
 ['T', 'J', 'L', 'O', 'T', 'M', 'S', 'I'],
 ['E', 'J', 'L', 'V', 'E', 'M', 'S', 'I'],
 ['T', 'J', 'L', 'O', 'T', 'I', 'M', 'E']], palavra))
