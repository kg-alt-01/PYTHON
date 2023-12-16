#Design a Python program using NumPy library functions.
import numpy as np

arr= np.array( [[[1,2,13],[3,4,14],[5,6,15]],
                [[7,8,16],[9,10,17],[11,12,18]]])

print("Array:\n", arr)
print("Array is of type : ", type(arr))
print("No. of dimensions : ", arr.ndim)
print("Shape of the array : ", arr.shape)
print("Size of array : ",arr.size)
print("Array store elements of type : ", arr.dtype)
print("Maximum value : ", np.max(arr))
print("Minimum value : ", np.min(arr))
print("Mean : ", np.mean(arr))
print("Median : ", np.median(arr))
print("Sum : ", np.sum(arr))
reshaped_arr = arr.reshape(6, 3)
print("Reshaped array :")
print(reshaped_arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("\n")
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
