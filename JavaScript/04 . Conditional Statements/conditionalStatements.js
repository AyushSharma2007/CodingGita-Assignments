// A] if Statement

// 1. Write a program to check if a number is divisible by 5. If yes, print “Divisible by 5”.
let numA1 = 25;
if (numA1 % 5 === 0) {
console.log("Divisible by 5");
}

// 2. Check if a person’s age is greater than or equal to 60. If true, print “Senior Citizen”.
let ageA2 = 65;
if (ageA2 >= 60) {
console.log("Senior Citizen");
}

// 3. Write a program that checks if a given number is greater than 100. If yes, print “Big Number”.
let numA3 = 150;
if (numA3 > 100) {
console.log("Big Number");
}

// 4. Check if the temperature is less than 10. If true, print “Very Cold”.
let tempA4 = 5;
if (tempA4 < 10) {
console.log("Very Cold");
}

// 5. Write a program to check if a student scored full marks (100). If yes, print “Perfect Score”.
let marksA5 = 100;
if (marksA5 === 100) {
console.log("Perfect Score");
}

// 6. Check if a number is negative. If it is, print “Negative Number”.
let numA6 = -10;
if (numA6 < 0) {
console.log("Negative Number");
}

// 7. Write a program that checks if a user has entered an empty string. If the string is empty, print “No input provided”.
let strA7 = "";
if (strA7 === "") {
console.log("No input provided");
}

// 8. Check if a given year is divisible by 100. If yes, print “Century Year”.
let yearA8 = 2000;
if (yearA8 % 100 === 0) {
console.log("Century Year");
}

// 9. Write a program to check if a number is both positive and even using a single if condition. If true, print “Positive Even Number”.
let numA9 = 12;
if (numA9 > 0 && numA9 % 2 === 0) {
console.log("Positive Even Number");
}

// 10. Check if the value of a variable marks is greater than or equal to 35 and less than or equal to 100. If true, print “Valid Marks”.
let marksA10 = 75;
if (marksA10 >= 35 && marksA10 <= 100) {
console.log("Valid Marks");
}

// B] if...else Statement

// 1. Write a program to check whether a number is even or odd.
let numB1 = 15;
if (numB1 % 2 === 0) {
console.log("Even");
} else {
console.log("Odd");
}

// 2. Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.
let ageB2 = 20;
if (ageB2 >= 18) {
console.log("Eligible");
} else {
console.log("Not Eligible");
}

// 3. Write a program that checks whether a number is positive or negative.
let numB3 = -5;
if (numB3 >= 0) {
console.log("Positive");
} else {
console.log("Negative");
}

// 4. Check if a student has passed or failed based on marks (pass mark = 35).
let marksB4 = 30;
if (marksB4 >= 35) {
console.log("Passed");
} else {
console.log("Failed");
}

// 5. Write a program to check whether a given character is an uppercase letter or not.
let charB5 = 'G';
if (charB5 >= 'A' && charB5 <= 'Z') {
console.log("Uppercase Letter");
} else {
console.log("Not an Uppercase Letter");
}

// 6. Check if a number is divisible by 3 or not. Print appropriate messages.
let numB6 = 9;
if (numB6 % 3 === 0) {
console.log("Divisible by 3");
} else {
console.log("Not divisible by 3");
}

// 7. Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.
let passB7 = "admin123";
if (passB7 === "admin123") {
console.log("Login Successful");
} else {
console.log("Incorrect Password");
}

// 8. Check whether a given year is a leap year or not using the basic rule (divisible by 4).
let yearB8 = 2024;
if (yearB8 % 4 === 0) {
console.log("Leap Year");
} else {
console.log("Not a Leap Year");
}

// 9. Write a program to find the greater of two numbers using if...else.
let num1B9 = 40;
let num2B9 = 25;
if (num1B9 > num2B9) {
console.log(num1B9 + " is greater");
} else {
console.log(num2B9 + " is greater");
}

// 10. Check if a number is positive, negative, or zero using only if...else.
let numB10 = 0;
if (numB10 > 0) {
console.log("Positive");
} else if (numB10 < 0) {
console.log("Negative");
} else {
console.log("Zero");
}


// C] if...else if...else Statement

// 1. Write a program that takes a month number (1–12) and prints the corresponding season:
//  Winter (12, 1, 2), Summer (3, 4, 5), Monsoon (6, 7, 8), Autumn (9, 10, 11).

let monthNumber = 7;

if (monthNumber === 12 || monthNumber === 1 || monthNumber === 2) {
    console.log("Winter");
} else if (monthNumber === 3 || monthNumber === 4 || monthNumber === 5) {
    console.log("Summer");
} else if (monthNumber === 6 || monthNumber === 7 || monthNumber === 8) {
    console.log("Monsoon");
} else if (monthNumber === 9 || monthNumber === 10 || monthNumber === 11) {
    console.log("Autumn");
} else {
    console.log("Invalid month number");
}

// 2. Create a simple tax calculator based on income:
// Income < 3,00,000 → No tax
// 3,00,000 – 7,00,000 → 5% tax
// 7,00,000 – 10,00,000 → 10% tax
// Above 10,00,000 → 15% tax
// Print the tax amount.
  
let incomeAmount = 500000;
let taxToPay = 0;

if (incomeAmount < 300000) {
    taxToPay = 0;
} else if (incomeAmount >= 300000 && incomeAmount <= 700000) {
    taxToPay = incomeAmount * 0.05;
} else if (incomeAmount > 700000 && incomeAmount <= 1000000) {
    taxToPay = incomeAmount * 0.10;
} else if (incomeAmount > 1000000) {
    taxToPay = incomeAmount * 0.15;
}
console.log("Tax amount: " + taxToPay + " Rs");


// 3. Write a program that checks a student’s score and prints:
// “Outstanding” (90 and above), “Good” (70–89), “Average” (40–69), “Needs Improvement” (below 40).

let studentScore = 85;

if (studentScore >= 90) {
    console.log("Outstanding");
} else if (studentScore >= 70 && studentScore <= 89) {
    console.log("Good");
} else if (studentScore >= 40 && studentScore <= 69) {
    console.log("Average");
} else if (studentScore < 40) {
    console.log("Needs Improvement");
}

// 4. Check the speed of a vehicle and print:
// “Slow” (below 40), “Normal” (40–80), “Fast” (above 80).

let vehicleSpeed = 65;

if (vehicleSpeed < 40) {
    console.log("Slow");
} else if (vehicleSpeed >= 40 && vehicleSpeed <= 80) {
    console.log("Normal");
} else if (vehicleSpeed > 80) {
    console.log("Fast");
}

// 5. Write a program that checks a person’s height (in cm) and prints:
// “Short” (< 150), “Average” (150–170), “Tall” (> 170).

let personHeight = 160;

if (personHeight < 150) {
    console.log("Short");
} else if (personHeight >= 150 && personHeight <= 170) {
    console.log("Average");
} else if (personHeight > 170) {
    console.log("Tall");
}

// 6. Check the day number (1–7) and print whether it is a Weekday or Weekend
// (1 to 5 = Weekday, 6 and 7 = Weekend).

let dayOfWeek = 6;

if (dayOfWeek >= 1 && dayOfWeek <= 5) {
    console.log("Weekday");
} else if (dayOfWeek === 6 || dayOfWeek === 7) {
    console.log("Weekend");
} else {
    console.log("Invalid day");
}

// 7. Write a program that calculates electricity bill based on units:
// 0–50 units → ₹2 per unit
// 51–150 units → ₹4 per unit
// Above 150 units → ₹6 per unit
// Print the total bill.

let electricityUnits = 120;
let totalBill = 0;

if (electricityUnits <= 50) {
    totalBill = electricityUnits * 2;
} else if (electricityUnits >= 51 && electricityUnits <= 150) {
    let first50UnitsCost = 50 * 2;
    let remainingUnits = electricityUnits - 50;
    totalBill = first50UnitsCost + (remainingUnits * 4);
} else if (electricityUnits > 150) {
    let first50UnitsCost = 50 * 2;
    let next100UnitsCost = 100 * 4;
    let remainingUnits = electricityUnits - 150;
    totalBill = first50UnitsCost + next100UnitsCost + (remainingUnits * 6);
}
console.log("Total electricity bill: ₹" + totalBill);

// 8. Create a program that checks a student’s attendance percentage and prints:
// “Excellent” (≥ 90), “Good” (75–89), “Satisfactory” (50–74), “Poor” (< 50).
  
let attendancePercent = 82;

if (attendancePercent >= 90) {
    console.log("Excellent");
} else if (attendancePercent >= 75 && attendancePercent <= 89) {
    console.log("Good");
} else if (attendancePercent >= 50 && attendancePercent <= 74) {
    console.log("Satisfactory");
} else if (attendancePercent < 50) {
    console.log("Poor");
}

// 9. Write a program that takes three subject marks and finds the highest mark among them using if...else if...else.

let mark1 = 80;
let mark2 = 95;
let mark3 = 85;

if (mark1 >= mark2 && mark1 >= mark3) {
    console.log("Highest mark is: " + mark1);
} else if (mark2 >= mark1 && mark2 >= mark3) {
    console.log("Highest mark is: " + mark2);
} else {
    console.log("Highest mark is: " + mark3);
}


// 10. Check a number and print one of the following:
// “Positive Even”, “Positive Odd”, “Negative Even”, “Negative Odd”, or “Zero”.

let myNumber = -4;

if (myNumber === 0) {
    console.log("Zero");
} else if (myNumber > 0 && myNumber % 2 === 0) {
    console.log("Positive Even");
} else if (myNumber > 0 && myNumber % 2 !== 0) {
    console.log("Positive Odd");
} else if (myNumber < 0 && myNumber % 2 === 0) {
    console.log("Negative Even");
} else if (myNumber < 0 && myNumber % 2 !== 0) {
    console.log("Negative Odd");
}


// D] Nested if Statement

// 1. Check if a number is greater than 10.
// If yes, then check whether it is divisible by 3 and print the appropriate message.
  
let testNumber = 15;

if (testNumber > 10) {
    if (testNumber % 3 === 0) {
        console.log("Number is greater than 10 and divisible by 3");
    }
}

// 2. Write a program that first checks if a person is 18 or older.
// If yes, then check if they have a voter ID. Print “Can Vote” only if both conditions are true.

let personAge = 20;
let hasVoterId = true;

if (personAge >= 18) {
    if (hasVoterId === true) {
        console.log("Can Vote");
    }
}

// 3. Check if a student has scored 40 or more marks.
// If yes, then check if the score is 80 or above and print “Passed with Distinction”.

let examMarks = 85;

if (examMarks >= 40) {
    if (examMarks >= 80) {
        console.log("Passed with Distinction");
    } else {
        console.log("Passed");
    }
} else {
    console.log("Failed");
}


// 4. Create a simple ATM system:
// First check if the PIN is correct.
// If PIN is correct, then check if the account balance is sufficient for withdrawal.

let isPinCorrect = true;
let accountBalance = 5000;
let withdrawalAmount = 2000;

if (isPinCorrect === true) {
    if (accountBalance >= withdrawalAmount) {
        console.log("Please collect your cash.");
    } else {
        console.log("Insufficient balance.");
    }
} else {
    console.log("Incorrect PIN.");
}

// 5. Write a program that checks if a year is divisible by 4.
// If yes, then further check if it is divisible by 100.
// If it is divisible by 100, then check if it is also divisible by 400 to confirm it is a leap year.

let checkYear = 2024;

if (checkYear % 4 === 0) {
    if (checkYear % 100 === 0) {
        if (checkYear % 400 === 0) {
            console.log("It is a Leap Year");
        } else {
            console.log("It is NOT a Leap Year");
        }
    } else {
        console.log("It is a Leap Year");
    }
} else {
    console.log("It is NOT a Leap Year");
}


// 6. Check if a user has entered a valid email (contains “@”).
// If yes, then check if the email ends with “.com”.
// If both are true, then check if the length of the email is greater than 10 characters and print “Valid Email”.

let email = "ayush@gmail.com";
let isEmailValid = false;
if (email.includes("@") == true) {
  let l = email.length;
  let lastChars = email[l - 4] + email[l - 3] + email[l - 2] + email[l - 1];
  if (lastChars == ".com") {
    if (l > 10) {
      isEmailValid = true;
    } else {
      console.log("Email is too short");
    }
  } else {
    console.log("Email doesnt include .com at the end");
  }
} else {
  console.log("Email doesnt include @");
}
if (isEmailValid) {
  console.log("Email valid!");
} else {
  console.log("Email is not valid!!");
}

// 7. Write a program for online shopping:
// First check if the cart total is ₹1000 or more.
// If yes, then check if the user is a premium member.
// If the user is premium, give 20% discount, otherwise give 10% discount.
// Finally print the final amount after discount.

let cartTotalAmount = 1500;
let isPremiumUser = true;
let finalAmount = cartTotalAmount;

if (cartTotalAmount >= 1000) {
    if (isPremiumUser === true) {
        let discount = cartTotalAmount * 0.20; // 20%
        finalAmount = cartTotalAmount - discount;
    } else {
        let discount = cartTotalAmount * 0.10; // 10%
        finalAmount = cartTotalAmount - discount;
    }
}
console.log("Final amount to pay: ₹" + finalAmount);


// 8. Check if a number is positive.
// If yes, then check whether it is even.
// If it is even, then further check if it is divisible by 4 and print “Positive Even and Divisible by 4”.

let valueToCheck = 16;

if (valueToCheck > 0) {
    if (valueToCheck % 2 === 0) {
        if (valueToCheck % 4 === 0) {
            console.log("Positive Even and Divisible by 4");
        }
    }
}


// 9. Create a job eligibility checker with multiple conditions:
// First check if age is between 21 and 30.
// If age is valid, then check if the candidate has a graduation degree.
// If the degree is present, then check if the candidate has at least 2 years of experience.
// Print “Eligible for Interview” only if all three conditions are true.

let candidateAge = 25;
let hasDegree = true;
let experienceYears = 3;

if (candidateAge >= 21 && candidateAge <= 30) {
    if (hasDegree === true) {
        if (experienceYears >= 2) {
            console.log("Eligible for Interview");
        }
    }
}


// 10. Write a nested program for exam eligibility:
// First check if the student is present.
// 3If present, then check if internal marks are ≥ 30.
// If internal marks are valid, then check if external marks are ≥ 35.
// Print “Eligible for Final Exam” only when all conditions are satisfied.

let studentPresent = true;
let internalMarks = 32;
let externalMarks = 40;

if (studentPresent === true) {
    if (internalMarks >= 30) {
        if (externalMarks >= 35) {
            console.log("Eligible for Final Exam");
        }
    }
}


// E] switch Statement

// 1. Write a program that takes a month number (1–12) and prints the number of days in that month using switch
// (Hint: Consider 28/29 for February as 28 for simplicity).

let monthForDaysCheck = 2;

switch (monthForDaysCheck) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 days");
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 days");
        break;
    case 2:
        console.log("28 days");
        break;
    default:
        console.log("Invalid month");
}


// 2. Write a program that checks a character and prints whether it is a vowel or consonant using switch.

let alphabetChar = 'e';

switch (alphabetChar) {
    case 'a' || 'A':
    case 'e' || 'E':
    case 'i' || 'I':
    case 'o' || 'O':
    case 'u' || 'U':
        console.log("It is a Vowel");
        break;
    default:
        console.log("It is a Consonant");
}


// 3. Create a program that takes a number from 1 to 4 and prints the season using multiple cases together:
// 1 or 2 → Winter
// 3 or 4 → Summer

let seasonNumber = 1;

switch (seasonNumber) {
    case 1:
    case 2:
        console.log("Winter");
        break;
    case 3:
    case 4:
        console.log("Summer");
        break;
    default:
        console.log("Unknown season");
}


// 4. Write a program using switch (true) to assign class based on marks:
// ≥ 75 → Distinction
// ≥ 60 → 1st class
// ≥ 50 → 2nd class
// ≥ 35 → 3rd class
// below 35 → Failed

let gradeMarks = 65;

switch (true) {
    case (gradeMarks >= 75):
        console.log("Distinction");
        break;
    case (gradeMarks >= 60):
        console.log("1st class");
        break;
    case (gradeMarks >= 50):
        console.log("2nd class");
        break;
    case (gradeMarks >= 35):
        console.log("3rd class");
        break;
    default:
        console.log("Failed");
}


// 5. Create a nested switch program:
// First take a role (“admin” or “user”).
// If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.
// If role is “user”, print “Limited Access”.

let userRole = "admin";
let actionCommand = "create";

switch (userRole) {
    case "admin":
        switch (actionCommand) {
            case "create":
                console.log("Admin Create Action Done");
                break;
            case "edit":
                console.log("Admin Edit Action Done");
                break;
            case "delete":
                console.log("Admin Delete Action Done");
                break;
        }
        break;
    case "user":
        console.log("Limited Access");
        break;
}


// 6. Predict and explain the output of the following code. Then correct it so that only one message is printed:
// let fruit = "mango";switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//   case "mango":
//     console.log("Mango is yellow");
//   case "banana":
//     console.log("Banana is yellow");
//   default:
//     console.log("Unknown fruit");}

// Explanation: The original code does not have "break" statements.
// When a switch case matches, it runs ALL the code below it too.
// Corrected version:
let fruit = "mango";
switch (fruit) {
    case "apple":
        console.log("Apple is red");
        break;
    case "mango":
        console.log("Mango is yellow");
        break;
    case "banana":
        console.log("Banana is yellow");
        break;
    default:
        console.log("Unknown fruit");
}


// 7. Write a program that takes a value which can be either a number or a string (0, "0", false, null, undefined) and uses switch to correctly identify each one. Explain why some values may not match as expected.

// Explanation: switch uses strict equality (===). So the number 0 is NOT equal to the string "0" or the boolean false.
let unknownValue = 0;

switch (unknownValue) {
    case 0:
        console.log("It is the number 0");
        break;
    case "0":
        console.log("It is the string '0'");
        break;
    case false:
        console.log("It is the boolean false");
        break;
    case null:
        console.log("It is a null object");
        break;
    case undefined:
        console.log("It is undefined");
        break;
}

// 3. Create a tricky calculator using switch that supports these operations:
// +, -, *, /, %, and also ** (exponentiation).
// Handle division by zero properly inside the corresponding case.

let mathOperator = "/";
let number1 = 10;
let number2 = 0;

switch (mathOperator) {
    case "+":
        console.log(number1 + number2);
        break;
    case "-":
        console.log(number1 - number2);
        break;
    case "*":
        console.log(number1 * number2);
        break;
    case "/":
        if (number2 === 0) {
            console.log("Error: Cannot divide by zero!");
        } else {
            console.log(number1 / number2);
        }
        break;
    case "%":
        console.log(number1 % number2);
        break;
    case "**":
        console.log(number1 ** number2);
        break;
}

// 9. Write a program using switch that takes a date (day number of the month) and prints:
// “Beginning of the month” (1–10)
// “Middle of the month” (11–20)
// “End of the month” (21–31)
// Use switch (true) technique for range checking.

let dateNumber = 15;

switch (true) {
    case (dateNumber >= 1 && dateNumber <= 10):
        console.log("Beginning of the month");
        break;
    case (dateNumber >= 11 && dateNumber <= 20):
        console.log("Middle of the month");
        break;
    case (dateNumber >= 21 && dateNumber <= 31):
        console.log("End of the month");
        break;
    default:
        console.log("Invalid date");
}


// 10. Create a multi-level nested switch program for an online food ordering system:
// First select Category: "veg" or "nonveg".
// Then select Item based on category.
// Finally select Size: "half" or "full" and print the final order summary with price.

let category = "veg";
let foodItem = "paneer";
let portionSize = "full";

switch (category) {
    case "veg":
        switch (foodItem) {
            case "paneer":
                switch (portionSize) {
                    case "half":
                        console.log("Order: Half Paneer, Price: 150");
                        break;
                    case "full":
                        console.log("Order: Full Paneer, Price: 250");
                        break;
                }
                break;
        }
        break;
    case "nonveg":
        switch (foodItem) {
            case "chicken":
                switch (portionSize) {
                    case "half":
                        console.log("Order: Half Chicken, Price: 200");
                        break;
                    case "full":
                        console.log("Order: Full Chicken, Price: 350");
                        break;
                }
                break;
        }
        break;
}


// F] Ternary Operator Questions

// 1. Write a ternary operator to check whether a given number is divisible by 7. If yes, return "Divisible by 7", otherwise "Not Divisible by 7".
    
let divCheckNum = 14;

let divisibleResult = (divCheckNum % 7 === 0) ? "Divisible by 7" : "Not Divisible by 7";
console.log(divisibleResult);

// 2. Using ternary operator, check if the temperature is greater than or equal to 30. Return "Hot Day" or "Pleasant Day".

let weatherTemp = 35;

let weatherResult = (weatherTemp >= 30) ? "Hot Day" : "Pleasant Day";
console.log(weatherResult);

// 3. Write a ternary expression that checks if a string is empty. Return "Empty String" if it is empty, otherwise "String has content".

let testString = "";

let stringResult = (testString === "") ? "Empty String" : "String has content";
console.log(stringResult);

// 4. Using nested ternary, check a person’s age and return:
//   - "Child" (age < 13)
//   - "Teenager" (13–19)
//   - "Adult" (20 and above)

let ageToGroup = 15;

let lifeStage = (ageToGroup < 13) ? "Child" : (ageToGroup >= 13 && ageToGroup <= 19) ? "Teenager" : "Adult"; 
console.log(lifeStage);

// 5. Write a nested ternary to find the greater of three numbers (a, b, c) without using Math.max.

let numA = 10;
let numB = 25;
let numC = 15;

let largestNum = (numA > numB) ? ((numA > numC) ? numA : numC) : ((numB > numC) ? numB : numC);                 
console.log("Largest number is: " + largestNum);

// 6. Create a nested ternary that classifies a student’s marks as:
//   - "Distinction" (≥ 75)
//   - "First Class" (60–74)
//   - "Second Class" (50–59)
//   - "Pass" (35–49)
//   - "Fail" (< 35)

let resultMarks = 65;

let finalGrade = (resultMarks >= 75) ? "Distinction" : (resultMarks >= 60) ? "First Class" : (resultMarks >= 50) ? "Second Class" : (resultMarks >= 35) ? "Pass" : "Fail";
console.log(finalGrade);

// 7. Write a single nested ternary expression that returns one of the following based on a number:
// "Positive Even", "Positive Odd", "Negative Even", "Negative Odd", or "Zero".

let targetNumber = -4;

let numberProperty = (targetNumber === 0) ? "Zero" : (targetNumber > 0) ? ((targetNumber % 2 === 0) ? "Positive Even" : "Positive Odd") : ((targetNumber % 2 === 0) ? "Negative Even" : "Negative Odd");
console.log(numberProperty);

// 8. Using only nested ternary operators, implement the full leap year logic
// (divisible by 4 and (not divisible by 100 or divisible by 400)) and return "Leap Year" or "Not a Leap Year".

let leapYearTest = 2024;

let leapYearResult = (leapYearTest % 4 === 0) ? ((leapYearTest % 100 !== 0) ? "Leap Year" : ((leapYearTest % 400 === 0) ? "Leap Year" : "Not a Leap Year")) : "Not a Leap Year";
console.log(leapYearResult);

// 9. Convert the following decision tree into one single nested ternary expression:
// if (role === "admin") {
//   if (action === "delete") → "Admin Delete"
//   else if (action === "edit") → "Admin Edit"
//   else → "Admin Other"
// } else if (role === "user") {
//   if (action === "view") → "User View"
//   else → "User Restricted"
// } else {
//   → "Invalid Role"
// }

let appRole = "admin";
let appAction = "edit";

let roleOutput = (appRole === "admin") ? 
                    ((appAction === "delete") ? "Admin Delete" : 
                     (appAction === "edit") ? "Admin Edit" : "Admin Other") : 
                 (appRole === "user") ? 
                    ((appAction === "view") ? "User View" : "User Restricted") : 
                 "Invalid Role";

console.log(roleOutput);

// 10. Write a complex nested ternary that calculates discount and final amount based on these rules:
//   - Cart total ≥ 5000 → 20% discount
//   - Cart total ≥ 2000 → 10% discount
//   - Cart total ≥ 1000 → 5% discount
//   - Otherwise → 0% discount
//   - Return both the discount percentage and the final payable amount in a single expression (you may return an object or a formatted string).

let cartTotal = 5000;
let discount = 0;
final =
  cartTotal >= 5000
    ? ("discount % : 20 , final payable amount :", cartTotal -= cartTotal * 0.2)
    : cartTotal >= 2000
      ? ("discount % : 10 , final payable amount :", cartTotal -= cartTotal * 0.1)
      : cartTotal >= 1000
        ? ("discount % : 5 , final payable amount :", cartTotal -= cartTotal * 0.05)
        : ("discount % : 0 , final payable amount :", cartTotal);
console.log(final);
