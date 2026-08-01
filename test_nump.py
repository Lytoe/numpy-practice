
import numpy as np
'''
a = np.array([1,2,3])
b = np.array([7,8,9])
c = np.array([4,5,6])
a_mag=np.linalg.norm(a)
b_mag=np.linalg.norm(b)
a_dim = len(a)
print(a_dim,"and the norm : ",a_mag)

normalized = a/a_mag
print(normalized)
print("-----------------------")
print("this is the norm of a: ", a_mag, "and this is the norm of b: ", b_mag)
print("mag a and b multipilied: ", a_mag * b_mag)
print("the coss thetha: " ,np.dot(a,b)/(a_mag * b_mag))
print(np.dot(a,b))
print(np.dot(a,c))

a = np.array([2,2])
a_norm  = np.linalg.norm(a)
print(a_norm)
unittt =  a / a_norm
print(unittt)
print("jame do elemen" ,unittt[0] + unittt[1])
unit_norm = np.linalg.norm(unittt)
print(unit_norm)   
 '''
a = np.array([3,5,1])
b = np.array([2,2,1])
dot_pro_a_a = np.dot(a,a)
dot_pro_a_b = np.dot(a,b)
print(dot_pro_a_a)
beta = dot_pro_a_b / dot_pro_a_a
print(beta)
proj_vector = beta * a
print(proj_vector)
