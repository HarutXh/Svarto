<<<<<<< HEAD
# Searching and sort algorithms
Searching algorithms are used to look for and retrieve the elements used in any data structure from that data structure itself. Sorting algorithms help arrange a list of data or an array of data into a particular order.

# Searching Algorithms
##### Linear Search
- Search items in sequence.
- Complexity of the sequential search, is O(n).  
- Sequential search can be improved by ordering the list in the case when the searched item is absent.
    - linear_search.py

##### Sentinel Linear Search

- In sentinel search, we first insert the target at the end of the list, and then we compare each item of the list until we find the required item. Either the required item is in the list, in which case it will be found before we reach the end of the list. Or the list didn’t have the target, so the algorithm will reach the end of the list and find the target item that we have inserted.
Here, we only need to check if the item matches the target, and we don’t need to check if the list is empty. This is because we are going to find the target one way or the other and break out of the loop.
Finally, we can check if the item we found was already there or was added by us. This check will happen only once and the entire runtime of the algorithm will be cut down significantly because we have one less comparison to do in every iteration of the loop.
- Complexity of the sentinal linear search, is O(n)
- sentinel_linear_search.py


##### Binary Search
- Take greater advantage of the ordered list.
- Complexity of binary search, is O(logn)
- A great example of a divide and conquer strategy
    - binary_search.py

##### Ternary Search
- Ternary search is a decrease(by constant) and conquer algorithm that can be used to find an element in an array. It is similar to binary search where we divide the array into two parts but in this algorithm, we divide the given array into three parts and determine which has the key (searched element). We can divide the array into three parts by taking mid1 and mid2 which can be calculated as shown below. Initially, l and r will be equal to 0 and n-1 respectively, where n is the length of the array. 
- Complexity of the sequential search, is O(logn)
- Decrease(by constant) and conquer algorithm
    - ternary_search.py

##### Jump Search
- Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
- Complexity of jump search, is O(√n)
    - jump_search.py

##### Interpolation Search
- Interpolation search is an algorithm for searching for a key in an array that has been ordered by numerical values assigned to the keys (key values). The Interpolation Search is a next step over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. But, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start searching toward the end side.
- To find the position to be searched, it uses the following formula. 
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo]) ]

pos == position of key to be searched 
arr[] == Array where elements need to be searched
x     == Element to be searched
lo    == Starting index in arr[]
hi    == Ending index in arr[]

- Complexity of interpolation search, is O(log2(log2 n)) for the average case, and O(n) for the worst case
    - interpolation_search.py


##### Exponential Search
-Exponential search is also known as doubling or galloping search. This mechanism is used to find the range where the search key may present. If L and U are the upper and lower bound of the list, then L and U both are the power of 2. For the last section, the U is the last position of the list. For that reason, it is known as exponential.
After finding the specific range, it uses the binary search technique to find the exact location of the search key.
- Complexity of exponential search, is O(logn)
    - exponential_search.py


### Sorting Algorithms

##### Bubble Sort
- Compares adjacent items and exchanges those that are out of order
- Complexity is O(n^2)
	- bubble_sort.py
	
##### Selection Sort
- Makes only one exchange for every pass through the list.
- Complexity is O(n^2)
	- selection_sort.py

##### Insertion Sort
- Builds the final sorted list one item at a time
- Always maintains a sorted sublist in the lower positions of the list
- Complexity is O(n^2)
	- insertion_sort.py
	
##### Merge Sort
- Divide and conquer strategy
- Requires extra space to hold the two halves
- Complexity is O(nlogn)
 	- merge_sort.py

##### Quick Sort
- Divide and conquer strategy
- Not using additional storage.
- Complexity is O(n^2)
	- quick_sort.py

# Installation

- git clone https://github.com/HarutXh/Svarto.git
- git checkout sort_and_searching_algorithms
- git branch
- git status

# Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b sort_and_searching_algorithms`)
3. Commit your Changes (`git commit -m 'Added sort_and_searching_algortihms'`)
4. Push to the Branch (`git push origin sort_and_searching_algorithms`)
5. Open a Pull Request








=======
# Svarto
Creating projects in Python programming language.

# Installation
git clone https://github.com/HarutXh/Svarto.git
>>>>>>> 54da45516e74e7c79c9d229f6d18724456e485c7
