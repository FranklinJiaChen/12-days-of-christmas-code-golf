"""
analyzing property of numbers
"""
abundant=[12,
18,
20,
24,
30,
36,
40,
42,
48,
54,
56,
60,
66,
70,
72,
78,
80,
84,
88,
90,
96,
100,
102,
104,
108,
112,
114,
120,
126,
132,
138,
140,
144,
150,
156,
160,
162,
168,
174,
176,
180,
186,
192,
196,
198,
200]

for num in abundant:
    # no new line
    print(chr(num//2+26), end="")



# printable ascii range = 32 to 126