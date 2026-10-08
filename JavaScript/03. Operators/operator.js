// # Assignment : JavaScript Operators

---

// ## A] Arithmetic Operators

// ### 1. Addition `+`

// 1. A school collected ₹15,000 from one class and ₹12,500 from another class. Find the total collection.  
// 2. A person reads 18 pages in the morning and 25 pages in the evening. Find the total pages read.  
// 3. A shop sold 125 items on Monday and 178 items on Tuesday. Find the total items sold.  
// 4. Predict the output:
//    let a = "10";
//    let b = 5;
//    let result = a + b;
//    console.log(result);
  
// 5. Predict the output:
//    let x = 5;
//    let y = "3";
//    let result = x + y;
//    console.log(result);
  
// 6. What is the output of 15 + 27?  
// 7. Calculate the total price if a book costs ₹350 and a pen costs ₹45.  
// 8. What is the result of "25" + 10 and why?  
// 9. A person has ₹2000 in their wallet. They buy items worth ₹750 and ₹320. Write an expression using + to find the total spent, then calculate the remaining balance.  
// 10. Predict the outputs and explain: 
  
//     console.log(5 + "5" + 5);
//     console.log(5 + 5 + "5");
//     console.log("5" + 5 + 5);


// question -1

let collectionFromFirstClass=15000
let collectionFromSecondClass=12500
let totalCollection=collectionFromFirstClass+collectionFromSecondClass
console.log("Total Collection=",totalCollection)

// Question -2

let pagesReadInMorning = 18
let pagesReadInEvening = 25
let totalPages = pagesReadInMorning+pagesReadInEvening
console.log("Total Pages=",totalPages)

// Question -3

let itemsSoldOnMonday = 125
let itemsSoldOnTuesday = 178
let toldSold=itemsSoldOnMonday+itemsSoldOnTuesday
console.log("Total Sold=",toldSold)

// Question -4
// 105

// Question -5
// 53

// Question -6
// 42

// Question -7
Let costOfBook=350
Let costOfPen=45
let totalCost=costOfBook+costofPen
console.log("Total Cost=",totalCost)

// Question -8

Result:2510
// reason when js sees string it perform concatenation instead of addition

// Question -9

let amountInWallet=2000
Let amountSpendOnFirstItem=750
Let amountSpendOnsecondItem=320
let remaingAmount=amountInWallet-(amountSpendOnFirstItem+amountSpendOnSItem)
console.log("REmaining Amount=",remainingAmount)

// Question -10
console.log(5 + "5" + 5);===> output=555 , As js  perform concatenation instead of addition

console.log(5 + 5 + "5");===>>output =105
console.log("5" + 5 + 5); ===>>output = 555

// ### 2. Subtraction `-`

// 1. A bus has 80 seats, and 53 seats are occupied. Find the number of empty seats.  
// 2. A student has 500 marks and loses 35 marks due to incorrect answers. Find the final marks.  
// 3. A warehouse has 2,500 boxes and sends 875 boxes to a store. Find the remaining boxes.  
// 4. Predict the output:

//    let a = "10";
//    let b = 3;
//    let result = a - b;
//    console.log(result);

// 5. Predict the output:

//    let x = "20";
//    let y = "5";
//    let result = x - y;
//    console.log(result);

// 6. What is the output of 100 - 37?  
// 7. A tank has 500 litres of water. After using 175 litres, how much water is left?  
// 8. What is the result of "50" - 20 and "50" - "20"? Explain any difference.  
// 9. A shopkeeper had 240 apples. He sold 95 in the morning and 67 in the evening. Write expressions to find how many apples are left.  
// 10. Predict and explain the outputs:  

//     console.log("100" - 50);
//     console.log("abc" - 10);
//     console.log(10 - "5" - "2");
//     console.log("10" - "5" - "2");



// Question -1

let totalSeats=80
let occupiedSeats=53
let emptySeats=80-53
console.log("Empty seats=",emptySeats)

// Question-2

let totalMarks=500
let marksLoses=35
let finalMarks=totalMarks-marksLoses
console.log("final marks=",finalMarks)

// Question-3

let totalBoxes=2500
let boxesSend=875
let remainingBoxes=totalBoxes-BoxesSend
console.log("Remaining Boxes=",remainingBoxes)

// Question-4
// 7

// Question -5
// 15

// Question-6
// 67

// question-7
let totalCapacity=500
let usedCapacity=175
let quantityLeft=totalCapacity-usedCapacity
console.log("Quantity left =",quantityLeft)

// Question-8
// both will give 30mas output as - converts string into number

// Question-9
let totalApples=240
let applesSoldInMorning=95
let applesSoldInEvening=67
let applesLeft=totalApples-(applesSoldInMorning+applesSoldInEvening)

// // Question-10
// "100" - 50 → "100" converts to 100 → 100 - 50 = 50
// "abc" - 10 → "abc" cannot convert to a number → NaN (Not a Number)
// 10 - "5" - "2" → strings convert to numbers → 10 - 5 - 2 = 3
// "10" - "5" - "2" → all strings convert to numbers → 10 - 5 - 2 = 3



// ### 3. Multiplication `*`

// 1. One notebook costs ₹45. Calculate the cost of buying 8 notebooks.  
// 2. A machine produces 120 bottles per hour. Calculate its production in 6 hours.  
// 3. A garden has 7 rows with 15 plants in each row. Find the total number of plants.  
// 4. Predict the output:

//    let a = "5";
//    let b = 4;
//    let result = a * b;
//    console.log(result);

// 5. Predict the output:

//    let x = "10";
//    let y = "2";
//    let result = x * y;
//    console.log(result);

// 6. What is the output of 12 * 8?  
// 7. One pizza costs ₹299. What is the total cost of 4 pizzas?  
// 8. What is the result of "7" * 6 and "7" * "6"?  
// 9. A factory produces 45 units per hour. How many units does it produce in 8 hours? Write the expression and calculate.  
// 10. Predict and explain the outputs:  

//     console.log("5" * 3 * "2");
//     console.log("abc" * 4);
//     console.log(10 * "2.5");
//     console.log("10" * "2.5" * "0");


// ---

// 1
console.log(45 * 8); // 360

// 2
console.log(120 * 6); // 720

// 3
console.log(7 * 15); // 105

// 4
let a = "5";
let b = 4;
let result = a * b;
console.log(result); // 20

// 5
let x = "10";
let y = "2";
let result2 = x * y;
console.log(result2); // 20

// 6
console.log(12 * 8); // 96

// 7
console.log(299 * 4); // 1196

// 8
console.log("7" * 6);     // 42
console.log("7" * "6");   // 42

// 9
console.log(45 * 8); // 360

// 10
console.log("5" * 3 * "2");       // 30
console.log("abc" * 4);           // NaN
console.log(10 * "2.5");           // 25
console.log("10" * "2.5" * "0");  // 0



// ### 4. Division `/`

// 1. A teacher distributes 144 pencils equally among 12 students. Find the number of pencils each student receives.  
// 2. A train travels 360 kilometres in 6 hours. Find its average distance travelled per hour.  
// 3. A company distributes ₹72,000 equally among 9 departments. Find the amount received by each department.  
// 4. Predict the output:

//    let a = "20";
//    let b = 4;
//    let result = a / b;
//    console.log(result);

// 5. Predict the output:

//    let x = "100";
//    let y = "5";
//    let result = x / y;
//    console.log(result);

// 6. What is the output of 144 / 12?  
// 7. 360 students are to be divided equally into 9 classrooms. How many students per classroom?  
// 8. What is the result of "100" / 4 and "100" / "4"?  
// 9. A total bill of ₹2400 is to be shared equally among 6 friends. Write the expression and find each person’s share.  
// 10. Predict and explain the outputs:  

//     console.log(10 / 0);
//     console.log(-10 / 0);
//     console.log(0 / 0);
//     console.log("20" / "4" / 2);
//     console.log("abc" / 5);


---


// Question 1
console.log(144 / 12); // 12 pencils

// Question 2
console.log(360 / 6); // 60 km per hour

// Question 3
console.log(72000 / 9); // ₹8000

// Question 4
let a = "20";
let b = 4;
let result = a / b;
console.log(result); // 5

// Question 5
let x = "100";
let y = "5";
let result2 = x / y;
console.log(result2); // 20

// Question 6
console.log(144 / 12); // 12

// Question 7
console.log(360 / 9); // 40 students

// Question 8
console.log("100" / 4);   // 25
console.log("100" / "4"); // 25

// Question 9
console.log(2400 / 6); // ₹400

// Question 10
console.log(10 / 0);          // Infinity
console.log(-10 / 0);         // -Infinity
console.log(0 / 0);           // NaN
console.log("20" / "4" / 2);  // 2.5
console.log("abc" / 5);       // NaN



// ### 5. Modulus `%`

// 1. A teacher has 53 students and forms groups of 5. Find the number of students left over.  
// 2. A shop has 128 candies and packs 10 candies in each box. Find the number of candies left unpacked.  
// 3. A factory produces 237 toys and packs them in boxes of 6. Find how many toys are left after packing full boxes.  
// 4. A bus can carry 40 passengers. If 185 people are waiting, find how many people will be left after filling as many full buses as possible.  
// 5. Predict the output:

//    let a = 10;
//    let b = 0;
//    let result = a % b;
//    console.log(result);

// 6. What is the output of 29 % 5?  
// 7. There are 23 chocolates to be packed in boxes of 4. How many chocolates will be left over?  
// 8. What is the result of 0 % 7 and 15 % 0? Explain.  
// 9. A number of pages (47) needs to be printed on sheets that hold 6 pages each. How many full sheets are needed and how many pages will be left over? Write expressions using % and /.  
// 10. Predict and explain the outputs (especially the signs):  

//     console.log(17 % 5);
//     console.log(-17 % 5);
//     console.log(17 % -5);
//     console.log(-17 % -5);
//     console.log(10 % 0);


// ---

// Question 1
console.log(53 % 5); // 3 students left

// Question 2
console.log(128 % 10); // 8 candies left

// Question 3
console.log(237 % 6); // 3 toys left

// Question 4
console.log(185 % 40); // 25 people left

// Question 5
let a = 10;
let b = 0;
let result = a % b;
console.log(result); // NaN

// Question 6
console.log(29 % 5); // 4

// Question 7
console.log(23 % 4); // 3 chocolates left

// Question 8
console.log(0 % 7);  // 0
console.log(15 % 0); // NaN

// Question 9
console.log(Math.floor(47 / 6)); // 7 full sheets
console.log(47 % 6);             // 5 pages left

// Question 10
console.log(17 % 5);    // 2
console.log(-17 % 5);   // -2
console.log(17 % -5);   // 2
console.log(-17 % -5);  // -2
console.log(10 % 0);    // NaN

// ### 6. Exponentiation `**`

// 1. Find the volume of a cube with a side length of 6 cm using side ** 3.  
// 2. Calculate the total number of cells in a square arrangement with 9 cells on each side using side ** 2.  
// 3. Find the value of \( 5^4 \) (5 raised to the power 4) using the exponentiation operator.  
// 4. A digital image has 1,024 pixels on each side (square image). Find the total number of pixels using pixels ** 2.  
// 5. Predict the output:

//    let base = 2;
//    let power = -1;
//    let result = base ** power;
//    console.log(result);

// 6. What is the output of 3 ** 4?  
// 7. Calculate the area of a square whose side is 9 units using the exponentiation operator.  
// 8. What is the result of 2 ** 5 and 5 ** 2? Are they the same?  
// 9. Predict and explain the outputs (and any errors):  

//    console.log(2 ** 3 ** 2);          // right-associative
//    console.log((2 ** 3) ** 2);
//    console.log(2 ** -3);
//    // console.log(-2 ** 2);           // Remember: Syntax error
//    console.log((-2) ** 2);
//    console.log(4 ** 0.5);

// 10. Predict the output:

//     let a = 10;
//     let b = 0;
//     let result = a ** b;
//     console.log(result);


----


// Question 1
let sideCube = 6;
console.log("1. Volume of cube:", sideCube ** 3); // Output: 216

// Question 2
let sideCells = 9;
console.log("2. Total cells:", sideCells ** 2); // Output: 81

// Question 3
console.log("3. 5 to the power 4:", 5 ** 4); // Output: 625

// Question 4
let pixels = 1024;
console.log("4. Total pixels:", pixels ** 2); // Output: 1048576

// Question 5
let base = 2;
let power = -1;
let result5 = base ** power;
console.log("5. Predicted output:", result5); // Output: 0.5 (Explanation: 2^-1 = 1/2 = 0.5)

// Question 6
console.log("6. 3 ** 4:", 3 ** 4); // Output: 81

// Question 7
let sideSquare = 9;
console.log("7. Area of square:", sideSquare ** 2); // Output: 81

// Question 8
console.log("8. 2 ** 5:", 2 ** 5); // Output: 32
console.log("8. 5 ** 2:", 5 ** 2); // Output: 25
// Explanation: No, they are not the same. Exponentiation is not commutative.

// Question 9
console.log("9a.", 2 ** 3 ** 2);      // Output: 512. Right-associative: Evaluates as 2 ** (3 ** 2) = 2 ** 9.
console.log("9b.", (2 ** 3) ** 2);    // Output: 64. Parentheses force left-to-right: Evaluates as 8 ** 2.
console.log("9c.", 2 ** -3);          // Output: 0.125. Evaluates as 1 / (2 ** 3) = 1/8.
// console.log(-2 ** 2);              // SyntaxError: Unary operator (-) not allowed immediately before exponentiation base.
console.log("9d.", (-2)

// Question 10
// 1 as any non-zero number raised to the power of 0 is always 1.

