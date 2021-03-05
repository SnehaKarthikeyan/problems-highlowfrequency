# problems-highlowfrequency

Question:

Given a number N and array of N integers, print the highest and the lowest frequency of the given array.
Input Size : |N| <= 1000000

Input Description: 

The first line contains an integer N. The second line contains N space-separated integers, which denotes array elements.

Output Description: 

Print the highest and the lowest frequency of the array separated by a space.

Hints:

Count the frequency of each elements in the array and print the highest and the lowest frequency of the array.

Sample Input:

19\n
2 6 2 2 7 6 2 5 3 6 6 2 4 6 2 2 9 6 2

Sample Output:

1 8

Explanation:

From the given array, the lowest frequency is 1 and the highest frequency 8.

Testcase 1:

Input:

37\n
56 78 67 22 43 54 66 87 67 11 25 45 55 67 11 73 67 34 56 78 67 22 43 54 66 87 67 23 45 68 11 73 67 34 56 78 67 

Output:

1 8

Testcase 2:

Input:

57\n
22 43 54 66 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 22 43 54 66 23 45 68 11 25 45 55 67 11 73 67 34 56 78 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 22

Output:

2 10

Testcase 3:

70\n
12 34 3 43 2 4 51 6 12 34 3 43 2  5 34 78 66 45 78 93 78 66 45 78 93 22 6 45 23 56 79 99 54 51 6 12 34 3 43 2  5 34 78 66 45 78 93 22 6 12 34 3 43 2  5 34 78 66 45 78 93 78 66 45 78 93 22 6 45 54 

Output:

1 10

Testcase 4:

Input:

44\n
4 3 33 56 1 6 12 34 3 33 56 78 3 12 45 98 3 22 56 3 78 90 4 51 6 12 34 3 33 56 78 3 12 45 98 3 22 56 3 78 90 43 11 25 

Output:

1 9

Testcase 5:

62\n
1125 1173 1251 1334 2112 5126 3378 5651 6722 1903  4456 7457 1125 1173 1251 1334 2112 5126 3378 5651 6722 2112 5144 3443 9722 1173 1251 1334 5126 3378 5651 6722 1903  4456 7457 1125 1173 1251 2112 5126 3378 5651 6722 1903  4456 5111 2112 4445 1227 7457 1125 1173 1251 2112 5126 3378 5651 6722 1173 1251 1334 2112 

Output:

1 7


