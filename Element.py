<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
    // Basic Level
    // Task 1: Convert to Uppercase
    let upper="hello world"
    console.log(upper.toUpperCase() )
    
    // Task 2: Convert to Lowercase
    let lower="i am from hyderabad"
    console.log(lower.toLowerCase())

   // Task 3: Reverse a String

  function reverseString(str) {   
     return str.split("").reverse().join("");
  }
  console.log(reverseString("Meghana")); 

// Task 4: Count the number of vowels in a string
function countVowels(str) {
    let matches = str.match(/[aeiouAEIOU]/g);
    return matches ? matches.length : 0;
}
console.log(countVowels("hello world")); 

// Advanced Level

// Task 1: Username Validation
function validateUsername(username) {
    if (username.length >= 5 && username.length <= 15) {
        return "Valid username";
    } else {
        return "Invalid username";
    }
}
console.log( validateUsername("user123")); 
console.log( validateUsername("us")); 

// Task 2: Email Formatter
function formatEmail(firstName, lastName) {
    return firstName.toLowerCase() + "." + lastName.toLowerCase() + "@gmail.com";
}
console.log(formatEmail("Meghana")); 

// Task 3: Word Counter
function wordCounter(sentence) {
    return sentence.split(" ").length;
}
console.log(wordCounter("Hello world this is JavaScript")); 

// Task 4: Palindrome Checker
function isPalindrome(str) {
    let reversed = str.split("").reverse().join("");
    return str === reversed ? "It is a palindrome" : "Not a palindrome";
}
console.log(isPalindrome("dad")); 
console.log(isPalindrome("john")); 

    </script>
</body>
</html>