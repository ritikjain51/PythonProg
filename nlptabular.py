# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:35:21 2019

@author: ATUL SHARMA
"""

def editDist(str1, str2, m, n):
    #for making the table
	dp = [[0 for x in range(n+1)] for x in range(m+1)] 

	for i in range(m+1): 
		for j in range(n+1): 
 
			if i == 0: 
				dp[i][j] = j
			elif j == 0: 
				dp[i][j] = i 

			elif str1[i-1] == str2[j-1]: 
				dp[i][j] = dp[i-1][j-1] 
			else: 
				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert 
								dp[i-1][j],	 # Remove 
								dp[i-1][j-1]) # Replace 

	return dp[m][n] 

str1 = "sunday"
str2 = "saturday"

print(editDist(str1, str2, len(str1), len(str2)))