// 1. Write a function to reverse a string.
function reverse_string(str) {
    return str.split('').reverse().join('');
}

let str = prompt("Reverse string");
alert(reverse_string(str));

// 2. Implement a function to check if a given string is a palindrome.
function reverse_str(str) {
    return str.split('').reverse().join('');
}

function isPalindrome(str) {
    reverse = reverse_str(str);
    if (reverse === str) {
        return true;
    }
    else {
        return false;
    }
}

let str = prompt("Reverse string");
alert(isPalindrome(str));

// 3. Write a function that counts the number of occurrences of each character in a string.
function countString(str, letter) {
    let count = 0;
    for (let i = 0; i <= str.length; i++) {
        if (str.charAt(i) == letter) {
            count += 1;
        }
    }
    return count;
}
let str = prompt("Enter a string");
let letterToCheck = prompt("Enter a letter to check");
let result = countString(str, letterToCheck);
alert(result);

// 4. Implement a function to find the maximum number in an array.
function maxNumber(arr) {
    let maxElement = arr[0];
    for (let i = 1; i <= arr.length; i++) {
        if (arr[i] > maxElement) {
            maxElement = arr[i];
            return maxElement;
        }
    }
}

let arr = [5, 9, 3, 7, 8, 6];
alert(arr);
alert(maxNumber(arr));

// 5. Write a function to remove duplicate elements from an array.
let arr = ["apple", "mango",
    "apple", "mango", "orange", "mango"];

function removeDuplicates(arr) {
    let unique = [];
    for (i = 0; i < arr.length; i++) {
        if (unique.indexOf(arr[i]) === -1) {
            unique.push(arr[i]);
        }
    }
    return unique;
}
alert(arr);
alert(removeDuplicates(arr));

// 6. Implement a function to check if two strings are anagrams.
function checkStringsAnagram(a, b) {
    let len1 = a.length;
    let len2 = b.length;
    if (len1 !== len2) {
        console.log('Invalid Input');
        return
    }
    let str1 = a.split('').sort().join('');
    let str2 = b.split('').sort().join('');
    if (str1 === str2) {
        return true;
    } else {
        return false;
    }
}
alert(checkStringsAnagram("anna", "naan"));
// 7. Write a function to find the factorial of a given number.
function factorial(n) {
    if (n == 0) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

let n = prompt("Find the factorial of a given number");
alert(factorial(n));

// 8. Implement a function to sort an array of numbers in ascending order.
let arr = [5, 3, 2, 4, 9, 7, 8, 14, 32, 1];
function sortArray(arr) {
    for (let i = 0; i <= arr.length; i++) {
        for (let j = 0; j <= (arr.length - i - 1); j++) {
            if (arr[j] > arr[j + 1]) {
                var temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

alert(arr);
alert(sortArray(arr));

// 9. Write a function to check if a given number is prime.
function isPrime(num) {
    if (num == 1) {
        return false;
    }
    else if (num == 2) {
        return true;
    }
    else {
        for (let i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
            return true;
        }
    }
}

let num = prompt("Check if a given number is prime");
alert(isPrime(num));

// 10.Implement a function to calculate the sum of all numbers in an array.
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

let arr = [40, 20, 60, 30, 80];
alert(arr);
alert(sumArray(arr));

// 11. Write a function to find the average of numbers in an array.
function avgArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    average = sum / arr.length;
    return average;
}

let arr = [40, 20, 60, 30, 80];
alert(arr);
alert(avgArray(arr));

// 12. Implement a function to find the median of a sorted array.
function median(arr) {
    const mid = Math.floor(arr.length / 2);
    const sortedArr = arr.sort((a, b) => a - b);

    if (arr.length % 2 === 0) {
        return (sortedArr[mid - 1] + sortedArr[mid]) / 2;
    } else {
        return sortedArr[mid];
    }
}
const arr = [1, 5, 8, 2, 6, 7, 3];
alert(median(arr));

// 13. Write a function to capitalize the first letter of each word in a sentence.
function toTitleCase(str) {
    const titleCase = str
        .toLowerCase()
        .split(' ')
        .map(word => {
            return word.charAt(0).toUpperCase() + word.slice(1);
        })
        .join(' ');

    return titleCase;
}

alert(toTitleCase('my name is harutyun.'));

// 14. Implement a function to check if a given year is a leap year.
function checkLeapYear(year) {
    if ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) {
        return true;
    } else {
        return false;
    }
}

const year = prompt('Enter a year:');
alert(checkLeapYear(year));

// 15. Write a function to remove falsy values from an array.
let arr = [23, 0, "gfg", false, true, NaN, 12, "hi", undefined, [], ""];

function removeFalsey(arr) {
    let newArr = [];
    arr.forEach((k) => {
        if (k) {
            newArr.push(k);
        }
    });
    return newArr;
}
alert(removeFalsey(arr));

// 16. Implement a function to check if a number is even or odd.
let num = prompt("Number is odd or even?")
function numOddOrEven(num) {
    if (num % 2 == 0) {
        return "Number is even";
    } else {
        return "Number is odd";
    }
}
alert(numOddOrEven(num));

// 17. Write a function to reverse the order of words in a sentence.
let str = "I love my country.";
function reverseString(str) {
    let reversed = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}

alert(reverseString(str));

// 18. Implement a function to calculate the power of a number.
let num = prompt("Enter a number.");
let pow = prompt("Enter a power");
function powOfNum(num, pow) {
    let result = 1
    for (let i = 0; i < pow; i++) {
        result = result * num;
    }
    return result;
}

alert(powOfNum(num, pow));

// 19. Write a function to remove whitespace from a string.
let string = "It's my life";
function removeSpace(string) {
    let newString = "";
    for (let i = 0; i < string.length; i++) {
        if (string[i] != " ") {
            newString += string[i];
        }
    }
    return newString;
}

alert(removeSpace(string));

// 20. Implement a function to find the largest sum of any two elements in an array.
function findLargestSumPair(arr, n) {
    if (arr[0] > arr[1]) {
        first = arr[0];
        second = arr[1];
    }
    else {
        first = arr[1];
        second = arr[0];
    }
    for (let i = 2; i < arr.length; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        }
        else if (arr[i] > second && arr[i] != first) {
            second = arr[i];
        }
    }
    return (first + second);
}
let arr = [20, 10, 2, 36, 15, 50];
let n = arr.length;
alert(findLargestSumPair(arr, n));

// 21. Write a function to convert a string to title case.
function toTitleCase(str) {
    str = str.toLowerCase().split(' ');
    for (var i = 0; i < str.length; i++) {
        str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
    }
    return str.join(' ');
}
alert(toTitleCase("my name is john"));

// 22. Implement a function to check if a string is a valid email address.
function checkIfEmail(email) {
    const regexExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/gi;

    return regexExp.test(email);
}

let email = prompt("Email");
alert(checkIfEmail(email));

// 23.Write a function to find the longest word in a sentence.
function getLongestWord(str) {
    let words = str.split(' ');
    let maxLength = 0;
    let longestWord = '';

    for (let i = 0; i < words.length; i++) {
        if (words[i].length > maxLength) {
            maxLength = words[i].length;
            longestWord = words[i];

        }
    }
    return longestWord;

}

alert(getLongestWord("This is a string, the longest word and its length will be printed on the console. Isn't it incredible ?"));

// 24. Implement a function to find the common elements between two arrays.
function getCommon(arr1, arr2) {
    var common = [];

    for (var i = 0; i < arr1.length; ++i) {
        for (var j = 0; j < arr2.length; ++j) {
            if (arr1[i] == arr2[j]) {
                common.push(arr1[i]);
            }
        }
    }
    return common;
}

var arr1 = [45, 99, 55, 223, 17, 93, 23];
var arr2 = [45, 18, 93, 7, 23, 1, 223, 5];
alert(getCommon(arr1, arr2));

// 25. Write a function to calculate the Fibonacci sequence up to a given number of terms.
function fibSequence(n) {
    if (n <= 1) {
        return n;
    }
    return fibSequence(n - 1) + fibSequence(n - 2);
}

let n = prompt("Enter number");
alert(fibSequence(n));

// 26. Implement a function to convert a decimal number to binary.
function decimalNum(decimal) {
    let binary = "";
    while (decimal > 0) {
        if (decimal & 1) {
            binary = "1" + binary;
        } else {
            binary = "0" + binary;
        }
        decimal = decimal >> 1;
    }
    return binary;
}

let decimal = prompt("Enter a number");
alert(decimalNum(decimal));

// 27. Write a function to calculate the area of a circle.
function areaCircle(r) {
    if (r < 0) {
        return -1;
    }
    else {
        area = Math.PI * r ** 2;
        return area;
    }
}
let r = prompt("Enter a radius");
alert(areaCircle(r));

// 28. Implement a function to find the second smallest element in an array.
function secondSmallestElem(arr) {
    let smallest = Infinity;
    let second_smallest = Infinity;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < smallest) {
            second_smallest = smallest;
            smallest = arr[i];
        } else if (arr[i] < second_smallest && arr[i] !== smallest) {
            second_smallest = arr[i];
        }
    }

    return second_smallest;
}

let arr = [5, 3, 2, 6, 8, 7, 34];
alert(secondSmallestElem(arr));

// 29. Write a function to check if a given string is a valid URL.
function isValidUrl(string) {
    try {
        const url = new URL(string);
        return url.protocol === 'http:' || url.protocol === 'https:';
    } catch (err) {
        return false;
    }
}

alert(isValidUrl('https://codingbeautydev.com'));
alert(isValidUrl('app://codingbeautydev.com'));
alert(isValidUrl('Coding Beauty'));

// 30. Implement a function to find the number of vowels in a string.
function countVowel(str) {
    const count = str.match(/[aeiou]/gi).length;
    return count;
}

string = prompt('Enter a string: ');
alert(countVowel(string));

// 31. Write a function to check if a given array is sorted in ascending order.
function sorted(arr) {
    let second_index;
    for (let first_index = 0; first_index < arr.length; first_index++) {
        second_index = first_index + 1;
        if (arr[second_index] - arr[first_index] < 0) return false;
    }
    return true;
}

let arr = [1, 5, 3, 4];
alert('is array sorted ? ' + sorted(arr));

// 32. Implement a function to calculate the sum of digits in a number.
function sumDigits(value) {
    let sum = 0;
    while (value) {
        sum += value % 10;
        value = Math.floor(value / 10);
    }
    return sum;
}
let value = prompt("Enter a number");
alert(sumDigits(value));

// 33. Write a function to remove the specified character from a string.
function removeCharacter(inputString, charToRemove) {
    return inputString.split(charToRemove).join('');
}

let inputString = "Hello World!"
let charToRemove = prompt("Enter specified character");
alert(removeCharacter(inputString, charToRemove));
// 34. Implement a function to find the index of the first occurrence of a given element in an array.
function findFirstOccurrence(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
}
let arr = [1, 3, 5, 7, 9, 3, 2, 8, 4];
let target = prompt("Enter target element");
target = parseInt(target);
alert("Element find the index: " + findFirstOccurrence(arr, target));
// 35. Write a function to convert a binary number to decimal.
function binaryNum(binary) {
    let decimal = 0;
    let l = binary.length;
    for (let i = l - 1; i >= 0; i--) {
        if (binary[i] == '1')
            decimal += Math.pow(2, l - i - 1);// add power of 2 in the decimal if character of binary string is 1.
    }
    return decimal;
}

let binary = prompt("Enter binary number");
alert(binaryNum(binary));

// 36. Implement a function to check if a given string is a palindrome ignoring spaces and punctuation.
function isPalindromeIgnoringSpacesAndPunctuation(str) {
    const cleanStr = str.replace(/[^\w]/g, "").toLowerCase();
    return cleanStr === cleanStr.split("").reverse().join("");
}

alert(isPalindromeIgnoringSpacesAndPunctuation("A man, a plan, a canal, Panama"));
alert(isPalindromeIgnoringSpacesAndPunctuation("race a car"));
alert(isPalindromeIgnoringSpacesAndPunctuation("Was it a car or a cat I saw?"));

// 37. Write a function to remove all even numbers from an array.
let arr = [5, 31, 2, 6, 97, 85, 20, 48];
function removeAllEvenNum(arr) {
    let newArr = []
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            newArr.push(arr[i]);
        }
    }
    return newArr;
}

alert(removeAllEvenNum(arr));

// 38. Implement a function to generate a random number between a given range.
function generateRandom(min = 0, max = 100) {
    let difference = max - min;
    let rand = Math.random();
    rand = Math.floor(rand * difference);
    rand = rand + min;
    return rand;
}

alert(generateRandom());

// 39. Write a function to reverse the order of elements in an array.
let arr = [5, 3, 47, 9, 54, 21];
function reverseArr(arr) {
    let reversedArr = []
    for (let i = arr.length - 1; i >= 0; i--) {
        reversedArr.push(arr[i]);
    }
    return reversedArr;
}

alert(reverseArr(arr));

// 40. Implement a function to check if a number is a perfect square.
let number = prompt("Enter a number");
function isPerfectSquare(number) {
    if (Number.isInteger(Math.sqrt(number))) {
        return "Number is a perfect square";
    }
    else {
        return "Number is not perfect square";
    }
}

alert(isPerfectSquare(number));

// 41. Write a function to count the number of words in a sentence.
function countWords(str) {
    const arr = str.split(' ');

    return arr.filter(word => word !== '').length;
}
let str = prompt("Write sentence");
alert(countWords(str));

// 42. Implement a function to find the smallest common multiple of two numbers.
function findSmallestCommonMultiple(number1, number2) {
    for (let i = 1; i <= number1 && i <= number2; i++) {
        if (number1 % i == 0 && number2 % i == 0) {
            hcf = i;
        }
    }
    return hcf;
}
let hcf;
let number1 = prompt('Enter a first positive integer: ');
let number2 = prompt('Enter a second positive integer: ');
let lcm = (number1 * number2) / hcf;
alert(findSmallestCommonMultiple(number1, number2));

// 43. Write a function to convert a number to Roman numerals.
function romanize(num) {
    let lookup = { M: 1000, CM: 900, D: 500, CD: 400, C: 100, XC: 90, L: 50, XL: 40, X: 10, IX: 9, V: 5, IV: 4, I: 1 }, roman = '', i;
    for (i in lookup) {
        while (num >= lookup[i]) {
            roman += i;
            num -= lookup[i];
        }
    }
    return roman;
}

let num = prompt("Enter a number");
alert(romanize(num));

// 44. Implement a function to check if a given string is a valid palindrome.
function checkPalindrome(string) {
    for (let i = 0; i < string.length / 2; i++) {
        if (string[i] !== string[string.length - 1 - i]) {
            return 'It is not a palindrome';
        }
    }
    return 'It is a palindrome';
}
let string = prompt('Enter a string: ');
alert(checkPalindrome(string));

// 45. Write a function to sort an array of strings in alphabetical order.
function sortStringsAlphabetically(array) {
    array.sort();
    return array;
}

// Example usage:
let unsortedArray = ["banana", "apple", "cherry", "date"];
alert(sortStringsAlphabetically(unsortedArray));

// 46. Implement a function to remove all duplicates from an array of numbers.
let arr = [5, 3, 6, 4, 1, 5, 4, 1];

function removeAllDuplicates(arr) {
    let unique = [];
    for (i = 0; i < arr.length; i++) {
        if (unique.indexOf(arr[i]) === -1) {
            unique.push(arr[i]);
        }
    }
    return unique;
}
alert(arr);
alert(removeAllDuplicates(arr));

// 47. Write a function to find the longest common prefix among an array of strings.
function longestCommonPrefix(strs) {
    if (!strs || strs.length === 0) {
        return '';
    }
    let firstStr = strs[0];
    let prefix = '';
    for (let i = 0; i < firstStr.length; i++) {
        let char = firstStr[i];
        for (let j = 1; j < strs.length; j++) {
            let currentStr = strs[j];
            if (i >= currentStr.length || currentStr[i] !== char) {
                return prefix;
            }
        }
        prefix += char;
    }
    return prefix;
}

let inputArray = ['apple', 'app', 'april', 'apartment'];
alert("The longest common prefix is " + longestCommonPrefix(inputArray));

// 48. Implement a function to calculate the factorial of a large number.
function factorial(N) {
    let f = BigInt(1);
    for (var i = 2; i <= N; i++)
        f *= BigInt(i);
    return f;
}

let N = prompt("Enter n");
alert(factorial(N));

// 49. Write a function to find the missing number in an array of consecutive numbers.
function findMissingNumber(arr) {
    const n = arr.length + 1;
    const expectedSum = (n * (arr[0] + arr[arr.length - 1])) / 2;
    const actualSum = arr.reduce((acc, num) => acc + num, 0);

    return expectedSum - actualSum;
}

const arr = [1, 2, 3, 5, 6, 7];
alert(findMissingNumber(arr));

// 50. Implement a function to convert a string to camel case.
camelize = function camelize(str) {
    return str.replace(/\W+(.)/g, function (match, chr) {
        return chr.toUpperCase();
    });
}

let str = prompt("Enter string");
alert(camelize(str));

// 51. Write a function to check if a given number is Armstrong number.
function isArmstrongNumber(num) {
    let numString = num.toString();
    let numDigits = numString.length;
    let sum = 0;

    for (let i = 0; i < numDigits; i++) {
        let digit = parseInt(numString[i]);
        sum += Math.pow(digit, numDigits);
    }

    return sum === num;
}

let num = prompt("Enter a number");
num = parseInt(num);
alert(isArmstrongNumber(num));

// 52․ Implement a function to check if a given string is a valid password.
function isValidPassword(password) {
    if (!(password.length >= 8 && password.length <= 15)) {
        return false;
    }
    if (password.indexOf(" ") !== -1) {
        return false;
    }
    let count = 0;
    for (let i = 0; i <= 9; i++) {
        if (password.indexOf(i) !== -1) {
            count = 1;
        }
    }
    if (count === 0) {
        return false;
    }
    if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
        return false;
    }
    count = 0;
    for (let i = 65; i <= 90; i++) {
        if (password.indexOf(String.fromCharCode(i)) !== -1) {
            count = 1;
        }
    }
    if (count === 0) {
        return false;
    }
    count = 0;
    for (let i = 97; i <= 122; i++) {
        if (password.indexOf(String.fromCharCode(i)) !== -1) {
            count = 1;
        }
    }
    if (count === 0) {
        return false;
    }
    return true;
}

let password = prompt("Write password");
alert(isValidPassword(password));

// 53. Write a function to find the largest prime factor of a given number.
function maxPrimeFactor(n) {
    let maxPrime = -1;
    while (n % 2 == 0) {
        n = n / 2;
        maxPrime = 2;
    }

    while (n % 3 == 0) {
        n = n / 3;
        maxPrime = 3;
    }

    for (let i = 5; i <= Math.sqrt(n); i += 6) {
        while (n % i == 0) {
            maxPrime = i;
            n = n / i;
        }
        while (n % (i + 2) == 0) {
            maxPrime = i + 2;
            n = n / (i + 2);
        }
    }

    return n > 4 ? n : maxPrime;
}

let n = prompt("Enter a number");
alert(maxPrimeFactor(n));

// 54. Implement a function to calculate the sum of all even Fibonacci numbers up to a given limit.
const sumOfEven = (limit) => {
    let temp, sum = 0, a = 0, b = 1;
    while (b < limit) {
        if (b % 2 === 0) {
            sum += b;
        };
        temp = a;
        a = b;
        b += temp;
    };
    return sum;
};

let limit = prompt("Enter a number");
alert(sumOfEven(limit));

// 55. Write a function to remove the duplicates from a sorted array in-place.
let arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5];

function removeAllDuplicates(arr) {
    let unique = [];
    for (i = 0; i < arr.length; i++) {
        if (unique.indexOf(arr[i]) === -1) {
            unique.push(arr[i]);
        }
    }
    return unique;
}
alert(arr);
alert(removeAllDuplicates(arr));

// 56. Implement a function to find the number of trailing zeros in the factorial of a given number.
function findTrailingZeros(n) {
    if (n < 0)
        return -1;
    let count = 0;
    for (let i = 5; Math.floor(n / i) >= 1; i *= 5)
        count += Math.floor(n / i);
    return count;
}

// Driver Code
let n = 100;
alert("Count of trailing 0s in " + 100
    + "! is " + findTrailingZeros(n));

// 57. Write a function to convert an integer to its English word representation.
function convertIntToWord(n) {
    if (n < 0)
        return false;
    single_digit = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    double_digit = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    below_hundred = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if (n === 0) return 'Zero'
    function translate(n) {
        word = ""
        if (n < 10) {
            word = single_digit[n] + ' '
        }
        else if (n < 20) {
            word = double_digit[n - 10] + ' '
        }
        else if (n < 100) {
            rem = translate(n % 10)
            word = below_hundred[(n - n % 10) / 10 - 2] + ' ' + rem
        }
        else if (n < 1000) {
            word = single_digit[Math.trunc(n / 100)] + ' Hundred ' + translate(n % 100)
        }
        else if (n < 1000000) {
            word = translate(parseInt(n / 1000)).trim() + ' Thousand ' + translate(n % 1000)
        }
        else if (n < 1000000000) {
            word = translate(parseInt(n / 1000000)).trim() + ' Million ' + translate(n % 1000000)
        }
        else {
            word = translate(parseInt(n / 1000000000)).trim() + ' Billion ' + translate(n % 1000000000)
        }
        return word
    }
    result = translate(n)
    return result.trim() + '.'
}

let n = prompt("Enter a number");
alert(convertIntToWord(n));

// 58. Implement a function to check if a given string is a valid IPv4 address.
function inRange(n) {
    // check if every split is in range 0-255
    if (n >= 0 && n <= 255) {
        return true;
    }
    return false;
}

function hasLeadingZero(n) {
    // check if every split has leading zero or not.
    if (n.length > 1) {
        if (n.charAt(0) === '0') {
            return true;
        }
    }
    return false;
}

function isValid(s) {
    let parts = s.split('.');
    if (parts.length !== 4) { // if number of splitting element is not 4 it is not a valid IP address
        return false;
    }
    for (let i = 0; i < parts.length; i++) {
        let part = parts[i];
        if (hasLeadingZero(part)) {
            return false;
        }
        if (part.length === 0) {
            return false;
        }
        try {
            let num = parseInt(part, 10);
            if (!inRange(num)) {
                return false;
            }
        } catch (e) {
            return false;
        }
    }
    return true;
}

let ip1 = "222.111.111.111";
let ip2 = "5555..555";
let ip3 = "0000.0000.0000.0000";
let ip4 = "1.1.1.1";
alert(ip1);
alert(isValid(ip1));
alert(ip2);
alert(isValid(ip2));
alert(ip3);
alert(isValid(ip3));
alert(ip4);
alert(isValid(ip4));

// 59. Write a function to find the intersection of two arrays.
function performIntersection(arr1, arr2) {
    let setA = new Set(arr1);
    let setB = new Set(arr2);
    let intersectionResult = [];
    for (let i of setB) {
        if (setA.has(i)) {
            intersectionResult.push(i);
        }

    }
    return intersectionResult;
}

let array1 = [1, 2, 3, 5, 9];
let array2 = [1, 3, 5, 8];
alert("First array " + array1);
alert("Second array " + array2);
alert("Intersection of two arrays " + performIntersection(array1, array2));

// 60. Implement a function to check if a given number is a perfect number.
function isPerfectNumber(num) {
    let sum = 0;
    for (let i = 1; i < num; i++) {
        if (num % i == 0) {
            sum += i;
        }
    }
    return sum == num;
}

let num = prompt("Enter a number");
alert(isPerfectNumber(num));

// 61. Write a function to remove the specified element from an array in-place.
function removeElementFromArray(arr, elementToRemove) {
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] === elementToRemove) {
            arr.splice(i, 1);
        }
    }
}
const myArray = [1, 2, 3, 4, 5];
alert(myArray);
const elementToRemove = parseInt(prompt("Enter the element to remove:"));
if (!isNaN(elementToRemove)) {
    removeElementFromArray(myArray, elementToRemove);
    alert(myArray);
} else {
    alert("Invalid input. Please enter a valid number.");
}

// 62. Implement a function to check if a given string is a valid credit card number.
function getDigit(number) {
    if (number < 9)
        return number;
    return Math.floor(number / 10) + number % 10;
}
function getSize(d) {
    let num = d.toString();
    return num.length;
}

function getPrefix(number, k) {
    if (getSize(number) > k) {
        let num = number.toString();
        return parseInt(num.substring(0, k));
    }
    return number;
}

function prefixMatched(number, d) {
    return getPrefix(number, getSize(d)) == d;
}

function sumOfDoubleEvenPlace(number) {
    let sum = 0;
    let num = number.toString();
    for (let i = getSize(number) - 2; i >= 0; i -= 2)
        sum += getDigit((num.charCodeAt(i) - '0'.charCodeAt(0)) * 2);

    return sum;
}

function sumOfOddPlace(number) {
    let sum = 0;
    let num = number.toString();
    for (let i = getSize(number) - 1; i >= 0; i -= 2)
        sum += num.charCodeAt(i) - '0'.charCodeAt(0);
    return sum;
}

function isValid(number) {
    return (getSize(number) >= 13 &&
        getSize(number) <= 16) &&
        (prefixMatched(number, 4) ||
            prefixMatched(number, 5) ||
            prefixMatched(number, 37) ||
            prefixMatched(number, 6)) &&
        ((sumOfDoubleEvenPlace(number) +
            sumOfOddPlace(number)) % 10 == 0);
}

let number = 5196081888500645
document.write(number + " is " + (isValid(number) ? "valid" : "invalid"));
// 63. Write a function to find the maximum sum of a subarray in a given array.
function maxSubArraySum(a, size) {
    var maxint = Math.pow(2, 53)
    var max_so_far = -maxint - 1
    var max_ending_here = 0

    for (var i = 0; i < size; i++) {
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here

        if (max_ending_here < 0)
            max_ending_here = 0
    }
    return max_so_far
}

// Driver code
var a = [-2, -3, 4, -1, -2, 1, 5, -3]
document.write("Maximum contiguous sum is ",
    maxSubArraySum(a, a.length))

// 64. Implement a function to reverse the order of words in a sentence without using built-in methods.
function reverseWords(sentence) {
    sentence = sentence.trim();
    let reversedSentence = '';
    let currentWord = '';
    for (let i = 0; i < sentence.length; i++) {
        const char = sentence[i];
        if (char === ' ' || i === sentence.length - 1) {
            if (i === sentence.length - 1) {
                currentWord += char;
            }
            if (currentWord.length > 0) {
                reversedSentence = currentWord + ' ' + reversedSentence;
                currentWord = '';
            }
        } else {
            currentWord += char;
        }
    }

    return reversedSentence.trim();
}

const sentence = "Hello, how are you?";
alert(reverseWords(sentence));

// 65. Write a function to check if a given string is a valid parentheses sequence.
function isValidParentheses(str) {
    const stack = [];
    const parenthesesMap = {
        '(': ')',
        '[': ']',
        '{': '}',
    };

    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (char in parenthesesMap) {
            stack.push(char);
        } else {
            const top = stack.pop();
            if (!top || parenthesesMap[top] !== char) {
                return false;
            }
        }
    }
    return stack.length === 0;
}

alert(isValidParentheses("()"));
alert(isValidParentheses("()[]{}"));
alert(isValidParentheses("([)]"));
alert(isValidParentheses("{{[[(())]]}}"));

// 66. Implement a function to calculate the square root of a given number using binary search.
function sqrtBinarySearch(x, epsilon = 1e-6) {
    if (x < 0) {
        throw new Error("Cannot calculate the square root of a negative number.");
    }

    if (x === 0) {
        return 0;
    }

    // Define the search range
    let low = 0;
    let high = Math.max(1, x);

    // Perform binary search
    while (high - low > epsilon) {
        const mid = (low + high) / 2;
        const square = mid * mid;

        if (square < x) {
            low = mid;
        } else {
            high = mid;
        }
    }

    return (low + high) / 2;
}

// Example usage:
const number = 25;
const result = sqrtBinarySearch(number);
alert(`The square root of ${number} is approximately: ${result}`);

// 67. Write a function to convert a string to snake case.
const toSnakeCase = str =>
    str &&
    str
        .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
        .map(x => x.toLowerCase())
        .join('_');

let str = prompt("Enter a string");
alert(toSnakeCase(str));

// 68. Implement a function to find the longest increasing subarray in a given array.
function lenOfLongIncSubArr(arr, n) {
    var max = 1, len = 1;
    for (var i = 1; i < n; i++) {
        if (arr[i] > arr[i - 1])
            len++;
        else {
            if (max < len) {
                max = len;
            }
            len = 1;
        }
    }
    if (max < len) {
        max = len;
    }
    return max;
}

var arr = [5, 6, 3, 5, 7, 8, 9, 1, 2];
var n = arr.length;
document.write("Length = " + lenOfLongIncSubArr(arr, n));

// 69. Write a function to check if a given number is a strong number.
function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function isStrongNumber(number) {
    const digits = number.toString().split('').map(Number);
    const sumOfFactorials = digits.reduce((sum, digit) => sum + factorial(digit), 0);
    return sumOfFactorials === number;
}

// Example usage:
const number = 145;
alert(`Is ${number} a strong number? ${isStrongNumber(number)}`);

// 70. Implement a function to check if a given string is a valid palindrome considering alphanumeric characters only.
function isPalindrome(str) {
    // Remove non-alphanumeric characters and convert to lowercase
    const cleanStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

    // Compare the original and reversed string
    return cleanStr === cleanStr.split('').reverse().join('');
}

// Example usage:
const inputString = "A man, a plan, a canal, Panama!";
console.log(`Is "${inputString}" a valid palindrome? ${isPalindrome(inputString)}`);

// 71. Write a function to find the sum of all multiples of 3 or 5 below a given number.
function sumMultiplesOf3And5(number) {
    let sum = 0;

    for (let i = 1; i < number; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            sum += i;
        }
    }

    return sum;
}

// Example usage:
const givenNumber = 100;
const result = sumMultiplesOf3And5(givenNumber);
alert(`The sum of all multiples of 3 or 5 below ${givenNumber} is: ${result}`);

// 72. Implement a function to find the number of ways to reach the nth step in a staircase, given that you can only climb 1 or 2 steps at a time.
function fib(n) {
    if (n <= 1)
        return n;
    return fib(n - 1) +
        fib(n - 2);
}
function countWays(s) {
    return fib(s + 1);
}
let s = 5;
document.write("Number of ways = " + countWays(s));

// 73. Write a function to convert a number to its binary representation without using built-in methods.
function decToBin(n) {
    if (n == 0)
        return "0";
    var bin = "";
    while (n > 0) {
        bin = ((n & 1) == 0 ? '0' : '1') + bin;
        n >>= 1;
    }
    return bin;
}
var n = prompt("Enter a number");
document.write(decToBin(n));

// 74.Implement a function to calculate the Hamming distance between two strings.
function hammingDist(str1, str2) {
    let i = 0, count = 0;
    while (i < str1.length) {
        if (str1[i] != str2[i])
            count++;
        i++;
    }
    return count;
}
let str1 = "geekspractice";
let str2 = "nerdspractise";

// function call
document.write(hammingDist(str1, str2));

// 75. Write a function to check if a given number is a power of two.
function isPowerOfTwo(n) {
    if (n == 0)
        return false;

    return parseInt((Math.ceil((Math.log(n) / Math.log(2))))) == parseInt((Math.floor(((Math.log(n) / Math.log(2))))));
}

// Driver Code

if (isPowerOfTwo(31))
    document.write("Yes<br/>");
else
    document.write("No<br/>");

if (isPowerOfTwo(64))
    document.write("Yes<br/>");
else
    document.write("No<br/>");

// 76. Implement a function to find the longest non-repeating substring in a given string.
function longest_substring_without_repeating_characters(input) {
    var chars = input.split('');
    var curr_char;
    var str = "";
    var longest_string = "";
    var hash = {};
    for (var i = 0; i < chars.length; i++) {
        curr_char = chars[i];
        if (!hash[chars[i]]) {
            str += curr_char;
            hash[chars[i]] = { index: i };
        }
        else {
            if (longest_string.length <= str.length) {
                longest_string = str;
            }
            var prev_dupeIndex = hash[curr_char].index;
            var str_FromPrevDupe = input.substring(prev_dupeIndex + 1, i);
            str = str_FromPrevDupe + curr_char;
            hash = {};
            for (var j = prev_dupeIndex + 1; j <= i; j++) {
                hash[input.charAt(j)] = { index: j };
            }
        }
    }
    return longest_string.length > str.length ? longest_string : str;
}
alert(longest_substring_without_repeating_characters("google.com"));

alert(longest_substring_without_repeating_characters("example.com"));

// 77. Write a function to calculate the sum of all prime numbers up to a given number.
function sumOfPrimes(n) {
    let prime = new Array(n + 1);
    for (let i = 0; i < n + 1; i++)
        prime[i] = true;
    for (let p = 2; p * p <= n; p++) {
        if (prime[p] == true) {
            for (let i = p * 2; i <= n; i += p)
                prime[i] = false;
        }
    }
    let sum = 0;
    for (let i = 2; i <= n; i++)
        if (prime[i])
            sum += i;
    return sum;
}

let n = 20;
document.write(sumOfPrimes(n));

// 78. Implement a function to find the maximum product of any three elements in an array.
function maxProduct(arr, n) {
    if (n < 3)
        return -1;
    let max_product = Number.MIN_VALUE;
    for (let i = 0; i < n - 2; i++)
        for (let j = i + 1; j < n - 1; j++)
            for (let k = j + 1; k < n; k++)
                max_product = Math.max(max_product,
                    arr[i] * arr[j] * arr[k]);

    return max_product;
}

let arr = [10, 3, 5, 6, 20];
let n = arr.length;

let max = maxProduct(arr, n);

if (max == -1)
    document.write("No Triplet Exists");
else
    document.write("Maximum product is " + max);

// 79. Write a function to check if a given string is a valid JSON.
function isValidJSON(str) {
    try {
        JSON.parse(str);
        return true;
    } catch (error) {
        return false;
    }
}

// Example usage:
const jsonString1 = '{"name": "John", "age": 30, "city": "New York"}';
document.write(isValidJSON(jsonString1));

const jsonString2 = '{"name": "John", "age": 30, "city": "New York",}';
document.write(isValidJSON(jsonString2));

const invalidString = 'This is not a JSON string.';
document.write(isValidJSON(invalidString));

// 80. Implement a function to calculate the GCD (Greatest Common Divisor) of two numbers.
function gcd(a, b) {
    var divisor;
    for (let i = 1; i <= a && i <= b; i++) {
        if (a % i == 0 && b % i == 0) {
            divisor = i;
        }
    }
    return divisor;
}

var result = gcd(20, 30);
alert(result);

// 81. Write a function to sort an array of objects based on a given property.
function compareName(a, b) {
    const name1 = a.name.toUpperCase();
    const name2 = b.name.toUpperCase();
    let comparison = 0;
    if (name1 > name2) {
        comparison = 1;
    } else if (name1 < name2) {
        comparison = -1;
    }
    return comparison;
}
const students = [{ name: 'Sara', age: 24 }, { name: 'John', age: 24 }, { name: 'Jack', age: 25 }];
console.log(students.sort(compareName));

// 82. Implement a function to perform a binary search in a sorted array.
function binarySearch(sortedArray, key) {
    let start = 0;
    let end = sortedArray.length - 1;
    while (start <= end) {
        let middle = Math.floor((start + end) / 2);
        if (sortedArray[middle] === key) {
            return middle;
        } else if (sortedArray[middle] < key) {
            start = middle + 1;
        } else {
            end = middle - 1;
        }
    }
    return -1;
}

const sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const key = 6;

const index = binarySearch(sortedArray, key);
if (index !== -1) {
    alert(`Key ${key} found at index ${index}`);
} else {
    alert(`Key ${key} not found in the array`);
}

// 83. Write a function to find the shortest distance between two points in a 2D plane.
function calculateDistance(x1, y1, x2, y2) {
    const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    return distance;
}

const point1 = { x: 1, y: 2 };
const point2 = { x: 4, y: 6 };

const distance = calculateDistance(point1.x, point1.y, point2.x, point2.y);
alert("Shortest distance between the two points: " + distance);

// 84. Implement a function to check if a given number is a palindrome in binary representation.
function isBinaryPalindrome(number) {
    const binaryString = number.toString(2);
    const reversedBinaryString = binaryString.split("").reverse().join("");
    return binaryString === reversedBinaryString;
}

let number = prompt("Enter a number");
alert(isBinaryPalindrome(number));

// 85. Write a function to calculate the sum of digits raised to the power of their respective position in a given number.
function sumOfDigitsRaisedToPosition(number) {
    const numStr = number.toString();
    let sum = 0;
    for (let i = 0; i < numStr.length; i++) {
        const digit = parseInt(numStr[i], 10);
        const position = i + 1;
        sum += Math.pow(digit, position);
    }
    return sum;
}
alert(sumOfDigitsRaisedToPosition(123));  // Output: 1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32
alert(sumOfDigitsRaisedToPosition(456));  // Output: 4^1 + 5^2 + 6^3 = 4 + 25 + 216 = 245
alert(sumOfDigitsRaisedToPosition(789));  // Output: 7^1 + 8^2 + 9^3 = 7 + 64 + 729 = 800

// 86. Implement a function to find the missing element in an array of consecutive numbers.
function findMissing(arr, n) {
    let l = 0, h = n - 1;
    let mid;
    while (h > l) {
        mid = l + Math.floor((h - l) / 2);
        if (arr[mid] - mid == arr[0]) {
            if (arr[mid + 1] - arr[mid] > 1)
                return arr[mid] + 1;
            else {
                l = mid + 1;
            }
        }
        else {
            if (arr[mid] - arr[mid - 1] > 1)
                return arr[mid] - 1;
            else {
                h = mid - 1;
            }
        }
    }
    return -1;
}
let arr = [-9, -8, -7, -5, -4, -3, -2, -1, 0];
let n = arr.length;

document.write(findMissing(arr, n));

// 87. Write a function to remove the specified number of characters from the beginning and end of a string.
function removeCharactersFromString(str, numCharsToRemove) {
    if (str.length <= numCharsToRemove * 2) {
        return '';
    }
    const result = str.substring(numCharsToRemove, str.length - numCharsToRemove);
    return result;
}

alert(removeCharactersFromString("Happy Birthday!", 3));

// 88. Implement a function to check if a given string is a valid time in the format "HH:MM".
function isValidTime(timeStr) {
    const timeRegex = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/;
    if (!timeRegex.test(timeStr)) {
        return false;
    }
    const [hours, minutes] = timeStr.split(':').map(Number);
    if (hours < 0 || hours > 23 || minutes < 0 || minutes > 59) {
        return false;
    }
    return true;
}

alert(isValidTime("12:34"));

// 89.Write a function to calculate the intersection area of two rectangles.
function calculateIntersectionArea(rect1, rect2) {
    const x1 = Math.max(rect1.x, rect2.x);
    const y1 = Math.max(rect1.y, rect2.y);
    const x2 = Math.min(rect1.x + rect1.width, rect2.x + rect2.width);
    const y2 = Math.min(rect1.y + rect1.height, rect2.y + rect2.height);
    if (x2 <= x1 || y2 <= y1) {
        return 0;
    }
    const width = x2 - x1;
    const height = y2 - y1;
    const area = width * height;

    return area;
}
const rect1 = { x: 0, y: 0, width: 5, height: 5 };
const rect2 = { x: 3, y: 2, width: 6, height: 4 };
console.log(calculateIntersectionArea(rect1, rect2));

// 90. Implement a function to find the maximum subarray sum using Kadane's algorithm.
function maxSubarraySum(arr) {
    if (arr.length === 0) {
        return 0;
    }
    let maxEndingHere = arr[0];
    let maxSoFar = arr[0];
    for (let i = 1; i < arr.length; i++) {
        maxEndingHere = Math.max(arr[i], arr[i] + maxEndingHere);
        maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }
    return maxSoFar;
}
console.log(maxSubarraySum([1, 2, 3, -2, 5]));
console.log(maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(maxSubarraySum([-2, -3, -1, -5]));
console.log(maxSubarraySum([]));

// 91.Write a function to check if a given number is a palindrome in both decimal and binary representation.
function isDecimalPalindrome(number) {
    const numStr = number.toString();
    return numStr === numStr.split("").reverse().join("");
}

function isBinaryPalindrome(number) {
    const binaryString = number.toString(2);
    return binaryString === binaryString.split("").reverse().join("");
}

function isPalindromeInDecimalAndBinary(number) {
    const isDecimalPal = isDecimalPalindrome(number);
    const isBinaryPal = isBinaryPalindrome(number);
    return isDecimalPal && isBinaryPal;
}

console.log(isPalindromeInDecimalAndBinary(585));
console.log(isPalindromeInDecimalAndBinary(121));
console.log(isPalindromeInDecimalAndBinary(10));
console.log(isPalindromeInDecimalAndBinary(0));
console.log(isPalindromeInDecimalAndBinary(8));

// 92. Implement a function to rotate an array by a given number of steps.
function rotateArray(arr, steps) {
    const effectiveSteps = steps % arr.length;

    if (effectiveSteps === 0) {
        return arr;
    }
    const rotatedPart = arr.slice(0, -effectiveSteps);
    const remainingPart = arr.slice(-effectiveSteps);
    const rotatedArray = remainingPart.concat(rotatedPart);

    return rotatedArray;
}

const array = [1, 2, 3, 4, 5, 6];
const rotatedArray = rotateArray(array, 2);
console.log(rotatedArray);

// 93. Write a function to check if a given string is a valid ISBN (International Standard Book Number).
function isValidISBN(isbn) {
    let n = isbn.length;
    if (n != 10)
        return false;
    let sum = 0;
    for (let i = 0; i < 9; i++) {
        let digit = isbn[i] - '0';

        if (0 > digit || 9 < digit)
            return false;

        sum += (digit * (10 - i));
    }
    let last = isbn[9];
    if (last != 'X' && (last < '0' || last > '9'))
        return false;
    sum += ((last == 'X') ? 10 : (last - '0'));
    return (sum % 11 == 0);
}

let isbn = "007462542X";

if (isValidISBN(isbn))
    document.write("Valid");
else
    document.write("Invalid");

// 94. Implement a function to find the smallest positive missing integer in an unsorted array.
function solution(A) {
    let n = A.length;
    let present = new Array(n + 1);
    for (let i = 0; i < n + 1; i++) {
        present[i] = false;
    }
    for (let i = 0; i < n; i++) {
        if (A[i] > 0 && A[i] <= n) {
            present[A[i]] = true;
        }
    }
    for (let i = 1; i <= n; i++) {
        if (!present[i]) {
            return i;
        }
    }
    return n + 1;
}

// Driver Code
let arr = [0, 10, 2, -10, -20]
document.write(solution(arr));

// 95. Write a function to calculate the sum of all numbers below a given number that are multiples of 3 or 5.
function sumMultiplesOf3And5BelowN(n) {
    let sum = 0;

    for (let i = 3; i < n; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            sum += i;
        }
    }

    return sum;
}
const number = 10;
const result = sumMultiplesOf3And5BelowN(number);
console.log(result);

// 96.Implement a function to check if a given string is a valid credit card number using the Luhn algorithm.
function getDigit(number) {
    if (number < 9)
        return number;
    return Math.floor(number / 10) + number % 10;
}
function getSize(d) {
    let num = d.toString();
    return num.length;
}
function getPrefix(number, k) {
    if (getSize(number) > k) {
        let num = number.toString();
        return parseInt(num.substring(0, k));
    }
    return number;
}
function prefixMatched(number, d) {
    return getPrefix(number, getSize(d)) == d;
}
function sumOfDoubleEvenPlace(number) {
    let sum = 0;
    let num = number.toString();
    for (let i = getSize(number) - 2; i >= 0; i -= 2)
        sum += getDigit((num.charCodeAt(i) - '0'.charCodeAt(0)) * 2);

    return sum;
}
function sumOfOddPlace(number) {
    let sum = 0;
    let num = number.toString();
    for (let i = getSize(number) - 1; i >= 0; i -= 2)
        sum += num.charCodeAt(i) - '0'.charCodeAt(0);
    return sum;
}
function isValid(number) {
    return (getSize(number) >= 13 &&
        getSize(number) <= 16) &&
        (prefixMatched(number, 4) ||
            prefixMatched(number, 5) ||
            prefixMatched(number, 37) ||
            prefixMatched(number, 6)) &&
        ((sumOfDoubleEvenPlace(number) +
            sumOfOddPlace(number)) % 10 == 0);
}
let number = 5196081888500645
document.write(number + " is " + (isValid(number) ? "valid" : "invalid"));

// 97. Write a function to find the longest substring without repeating characters.

function areDistinct(str, i, j) {
    var visited = new Array(26).fill(false);
    for (var k = i; k <= j; k++) {
        if (visited[str.charCodeAt(k) - 'a'.charCodeAt(0)])
            return false;
        visited[str.charCodeAt(k) - 'a'.charCodeAt(0)] = true;
    }
    return true;
}

function longestUniqueSubsttr(str) {
    var n = str.length;
    var res = 0;

    for (var i = 0; i < n; i++)
        for (var j = i; j < n; j++)
            if (areDistinct(str, i, j))
                res = Math.max(res, j - i + 1);

    return res;
}

// Driver code
var str = "geeksforgeeks";
alert("The input string is " + str);
var len = longestUniqueSubsttr(str);
alert("The length of the longest non-repeating character substring is " + len);

// 98. Implement a function to calculate the number of trailing zeros in the factorial of a given number without actually calculating the factorial.
function countTrailingZerosInFactorial(n) {
    let count = 0;

    while (n >= 5) {
        n = Math.floor(n / 5);
        count += n;
    }

    return count;
}

// Example usage:
const number = 20;
const trailingZeros = countTrailingZerosInFactorial(number);
console.log(`The number of trailing zeros in ${number}! is ${trailingZeros}.`);

// 99. Write a function to find the minimum number of coins needed to make change for a given amount.
function minCoins(coins, m, V) {
    if (V == 0)
        return 0;
    let res = Number.MAX_VALUE;
    for (let i = 0; i < m; i++) {
        if (coins[i] <= V) {
            let sub_res = minCoins(coins, m,
                V - coins[i]);
            if (sub_res != Number.MAX_VALUE &&
                sub_res + 1 < res)
                res = sub_res + 1;
        }
    }
    return res;
}

let coins = [9, 6, 5, 1];
let m = coins.length;
let V = 11;

document.write("Minimum coins required is " +
    minCoins(coins, m, V));

// 100. Implement a function to generate all possible permutations of a given string
function generatePermutations(str) {
    const result = [];

    function backtrack(current, remaining) {
        if (remaining.length === 0) {
            result.push(current);
        } else {
            for (let i = 0; i < remaining.length; i++) {
                const nextCurrent = current + remaining[i];
                const nextRemaining = remaining.slice(0, i) + remaining.slice(i + 1);
                backtrack(nextCurrent, nextRemaining);
            }
        }
    }

    backtrack('', str);
    return result;
}

console.log(generatePermutations('abc'));
console.log(generatePermutations('abcd'));