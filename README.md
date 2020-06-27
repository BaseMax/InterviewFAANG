# FAANG Interview

I took a Job offer from [Google](https://www.google.com/) 1 years ago, and took another Job offer from [FB](https://www.fb.com/) a few days ago to work as a **Technical Lead, Senior Software engineer**.

So I try to solve some Facebook interview and this was really cool for me.

I will add more tasks soon one by one, So it's a source for watching popular questions...

## Solving Facebook interview questions

<details><summary>
Pretty Json
</summary>
<p>

> Asked in: Facebook, Microsoft

Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

Rules for proper indentaion:

- Every inner brace should increase one indentation to the following lines.
- Every close brace should decrease one indentation to the same line and the following lines.
- The indents can be increased with an additional ‘\t’

Note:

- `[]` and `{}` are only acceptable braces in this case.
- Assume for this problem that space characters can be done away with.


##### Input Format

The only argument given is the integer array A.

##### Output Format

Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.

##### For Example

```
Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    { 
        A:"B",
        C: 
        { 
            D:"E",
            F: 
            { 
                G:"H",
                I:"J"
            } 
        } 
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo", 
        {
            "bar":
            [
                "baz", 
                null, 
                1.0, 
                2
            ]
        }
    ]
```

</p>
</details>

<details><summary>
Integer To Roman
</summary>
<p>

> Asked in: Amazon, Facebook, Microsoft, Twitter

##### Please Note:

Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

> Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output”

For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations. 

##### Input Format

The only argument given is integer A.

##### Output Format

Return a string denoting roman numeral version of A.

##### Constraints

1 <= A <= 3999

##### For Example

```
Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"
```

</p>
</details>


<details><summary>
Roman To Integer
</summary>
<p>

> Asked in: Amazon, Facebook, Microsoft, Twitter

Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

> NOTE: Read more details about roman numerals at Roman Numeric System

##### Input Format

The only argument given is string A.

##### Output Format

Return an integer which is the integer verison of roman numeral string.

##### For Example

```
Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20
```

</p>
</details>

<details><summary>
Add Two Numbers as Lists
</summary>
<p>

> Asked in: Amazon, Qualcomm, Microsoft, Facebook

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

- Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
- Output: 7 -> 0 -> 8

    342 + 465 = 807

Make sure there are no trailing zeros in the output list
So, `7 -> 0 -> 8 -> 0` is not a valid response even though the value is still 807.

</p>
</details>

<details><summary>
Count And Say
</summary>
<p>

> Asked in: Facebook, Amazon

The count-and-say sequence is the sequence of integers beginning as follows:

```
1, 11, 21, 1211, 111221, ...
```

- 1 is read off as one 1 or 11.
- 11 is read off as two 1s or 21.
- 21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

> Note: The sequence of integers will be represented as a string.
Each term of the sequence of integers will be represented as a string.

The count-and-say sequence is the sequence of integers with the first five terms as following:

```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

Given an integer n where `1 ≤ n ≤ 30`, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

##### Example:

if n = **2**,
the sequence is **11**.

```
Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
```

</p>
</details>


<details><summary>
Add Binary Strings
</summary>
<p>

> Asked in: Facebook, Microsoft

Given two binary strings, return their sum (also a binary string).

##### Example:

```
a = "100"
b = "11"
Return a + b = “111”.
```

</p>
</details>



<details><summary>
Reverse the String
    </summary>
<p>

> Asked in: Qualcomm, Amazon, Microsoft, Cisco, Facebook

Given a string A.

Return the string A after reversing the string word by word.

> NOTE: A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

##### Input Format

The only argument given is string A.

##### Output Format

Return the string A after reversing the string word by word.

##### For Example

```
Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
```

</p>
</details>




<details><summary>
Sort by Color
</summary>
<p>

> Asked in: Facebook, Microsoft

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

> Note: Using library sort function is not allowed.

##### Example :

```
Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
```

</p>
</details>


----

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)

