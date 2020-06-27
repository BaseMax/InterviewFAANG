# FAANG Interview

I took a Job offer from FB.com a few days ago to work as a **Technical Lead, Senior Software engineer**.

So I try to solve some Facebook interview and this was really cool for me.

## Solving Facebook interview questions

<details><summary>
## Pretty Json
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

---------

<details><summary>
## Integer To Roman
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

------

<details><summary>
## Roman To Integer
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

----

<details><summary>
## Add Two Numbers as Lists
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

----

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)

