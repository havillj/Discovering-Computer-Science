"""
Exercise 2.2.8

Discovering Computer Science, Second Edition
Jessen Havill
"""

sites = [(1.45, 7.31), (2.99, 7.55), (7.58, 6.29), (2.17, 4.71), 
         (1.07, 5.56), (1.52, 3.89), (1.42, 4.55), (1.83, 7.36), 
         (2.38, 4.55), (2.77, 5.25), (1.85, 3.4), (1.13, 4.4), 
         (1.51, 5.25), (2.0, 7.09), (4.05, 5.15), (2.99, 3.94), 
         (2.29, 7.16), (2.55, 7.91), (1.27, 4.85), (4.83, 2.85), 
         (2.64, 2.05), (1.04, 4.91), (2.6, 4.43), (4.06, 4.05), 
         (2.49, 4.38), (1.63, 3.17), (2.33, 5.47), (2.23, 5.92), 
         (1.3, 6.09), (2.27, 6.09), (1.84, 6.05), (1.54, 7.46), 
         (1.22, 7.65), (1.27, 3.77), (1.58, 2.44), (1.7, 6.76), 
         (2.39, 6.97), (2.82, 4.7), (1.75, 4.52), (2.08, 3.45), 
         (6.71, 5.8), (1.02, 4.39), (1.26, 6.71), (1.87, 5.63), 
         (2.06, 3.8), (1.69, 4.91), (1.98, 2.5), (2.04, 3.69), 
         (3.85, 7.62), (2.24, 2.85), (1.86, 7.68), (1.72, 5.1), 
         (4.23, 2.35), (2.44, 2.95), (0.59, 4.23), (1.34, 6.43), 
         (1.38, 6.37), (2.68, 2.89), (2.66, 7.85), (5.94, 4.84), 
         (1.11, 7.11), (2.77, 5.07), (2.58, 5.53), (1.61, 7.22), 
         (2.16, 3.19), (1.47, 6.81), (1.25, 2.03), (2.65, 5.18), 
         (1.97, 2.44), (2.8, 3.4), (1.69, 3.83), (7.63, 4.4), 
         (1.67, 3.96), (1.62, 3.78), (1.94, 3.0), (2.53, 2.18), 
         (8.77, 6.77), (2.46, 7.02), (1.31, 3.77), (2.23, 6.27), 
         (1.84, 6.87), (4.91, 2.79), (2.56, 3.29), (2.82, 5.97), 
         (1.45, 5.65), (1.77, 6.13), (1.21, 2.34), (2.23, 5.47), 
         (2.11, 5.0), (2.24, 3.71), (1.38, 6.3), (1.32, 3.98), 
         (1.8, 3.62), (1.41, 2.53), (1.68, 2.66), (1.28, 7.31), 
         (2.55, 7.52), (2.67, 0.65), (1.42, 4.49), (2.39, 6.01), 
         (1.49, 7.93), (2.87, 5.08), (2.8, 2.16), (1.33, 2.38), 
         (0.91, 8.56), (2.88, 5.65), (1.18, 3.5), (1.67, 2.23), 
         (1.69, 2.4), (2.32, 6.68), (2.22, 7.55), (2.86, 3.6), 
         (2.06, 4.29), (1.67, 4.01), (1.2, 3.72), (1.85, 6.08), 
         (1.57, 0.06), (2.73, 2.23), (5.94, 7.72), (1.46, 5.67), 
         (2.34, 4.44), (2.63, 6.27), (1.98, 3.48), (2.3, 2.49), 
         (2.58, 7.55), (1.1, 5.47), (1.72, 7.31), (2.25, 6.84), 
         (2.14, 4.55), (2.88, 2.13), (1.42, 5.29), (1.27, 7.35), 
         (7.08, 4.92), (1.12, 6.21), (1.25, 3.86), (2.35, 6.55), 
         (2.38, 6.0), (2.26, 6.72), (2.03, 6.14), (1.76, 2.0), 
         (2.13, 2.72), (1.22, 5.01), (5.26, 8.64), (1.74, 4.15), 
         (2.84, 2.34), (1.42, 3.29), (1.19, 1.88), (2.6, 8.61), 
         (1.62, 2.08), (1.75, 2.15), (4.97, 6.63), (4.99, 0.58)]
