# -*- coding: utf-8 -*-
"""Tugas DDP 6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gs2sFLZYGmH0wZCsT-G6oq92uOlT8Zpv
"""

numbers = [
 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]
i = 0
while i <= len(numbers):
  if numbers[i] % 2 !=0:
    print(numbers[i])
  if numbers[i] == 553:
    break
  i += 1

x = 0
for i in range(1,20,2):
  x = x + i
print(x)

for m in range(0,int(input())):
  for p in range(0,m+1):
    print("*", end=" ")
  print()