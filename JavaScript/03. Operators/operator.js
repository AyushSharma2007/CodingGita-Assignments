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
console.log(5 + "5" + 5);===> output=555 
  // As js  perform concatenation instead of addition

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
let remainingBoxes=totalBoxes-boxesSend
console.log("Remaining Boxes=",remainingBoxes)

// Question-4
// 7

// Question -5
// 15

// Question-6
// 63

// question-7
let totalCapacity=500
let usedCapacity=175
let quantityLeft=totalCapacity-usedCapacity
console.log("Quantity left =",quantityLeft)

// Question-8
// both will give 30 as output as - converts string into number

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
let totalPages = 47;
let pagesPerSheet = 6;
let fullSheets = (totalPages - (totalPages % pagesPerSheet)) / pagesPerSheet; // 7
let leftoverPages = totalPages % pagesPerSheet;                               // 5

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
console.log("9b.", (2 ** 3) ** 2);    // Output: 64. Parentheses forces left-to-right: Evaluates as 8 ** 2.
console.log("9c.", 2 ** -3);          // Output: 0.125. Evaluates as 1 / (2 ** 3) = 1/8.
// console.log(-2 ** 2);              // SyntaxError: Unary operator (-) not allowed immediately before exponentiation base.
console.log("9d.", (-2)

// Question 10
// 1 as any non-zero number raised to the power of 0 is always 1.


            
// B] Assignment Operators

            
// 1. Simple Assignment =
// 1. Store a student’s name as "Priya" and marks as 92 using the assignment operator.
let studentName = "Priya";
let marks = 92;

// 2. Create a variable score and assign it the value 0.
let score = 0;

// 3. Assign the value 50 to three variables a, b and c using a single chained assignment.
let a, b, c;
a = b = c = 50;

// 4. Predict the output: let x; x = 100; console.log(x);
// Output: 100

// 5. Predict the output: let p = 15; let q = p; q = 30; console.log(p, q);
// Output: 15 30


// 2. Add and Assign +=
// 1. A player’s score is 80. He scores 25 more points. Update the score using +=.
let playerScore = 80;
playerScore += 25;

// 2. A wallet has ₹1500. Cashback of ₹120 is added. Update the balance using +=.
let wallet = 1500;
wallet += 120;

// 3. Predict the output: let count = 10; count += 5; console.log(count);
// Output: 15

// 4. Predict the output: let msg = "Good"; msg += " Morning"; console.log(msg);
// Output: Good Morning

// 5. What is the final value after let n = 20; n += "5";? Explain.
// Output: "205" (String concatenation happens because "5" is a string type)


// 3. Subtract and Assign -=
// 1. Health is 100. Player takes 35 damage. Update health using -=.
let health = 100;
health -= 35;

// 2. Stock of 300 items is reduced by 45 after a sale. Update using -=.
let stock = 300;
stock -= 45;

// 3. Predict the output: let lives = 5; lives -= 2; console.log(lives);
// Output: 3

// 4. Predict the output: let num = "40"; num -= 15; console.log(num);
// Output: 25

// 5. What is the result of let x = "abc"; x -= 5;? Explain.
// Output: NaN (Cannot subtract a number from a non-numeric string)


// 4. Multiply and Assign *=
// 1. Price of an item is ₹500. Apply 18% GST using *= 1.18.
let price = 500;
price *= 1.18;

// 2. A quantity of 8 is tripled. Update using *=.
let qty = 8;
qty *= 3;

// 3. Predict the output: let amount = 200; amount *= 1.1; console.log(amount);
// Output: 220.00000000000003

// 4. Predict the output: let val = "7"; val *= 3; console.log(val);
// Output: 21

// 5. What is the result of let y = "hello"; y *= 2;? Explain.
// Output: NaN (Cannot multiply a non-numeric string)


// 5. Divide and Assign /=
// 1. Total of 180 chocolates is shared among 6 children. Update using /=.
let chocolates = 180;
chocolates /= 6;

// 2. Distance of 300 km is covered in 5 hours. Find average speed using /=.
let distance = 300;
distance /= 5;

// 3. Predict the output: let total = 400; total /= 8; console.log(total);
// Output: 50

// 4. Predict the output: let num = "100"; num /= 4; console.log(num);
// Output: 25

// 5. What is the result of let z = 50; z /= 0;? Explain.
// Output: Infinity (Division by zero in JS yields Infinity)


// 6. Modulus and Assign %=
// 1. Number 47 is divided by 6. Store only the remainder using %=.
let num1 = 47;
num1 %= 6;

// 2. Counter is at 23. Keep only the remainder when divided by 12 using %=.
let counter = 23;
counter %= 12;

// 3. Predict the output: let num = 29; num %= 5; console.log(num);
// Output: 4

// 4. Predict the output: let x = "17"; x %= 3; console.log(x);
// Output: 2

// 5. What is the result of let m = 15; m %= 0;? Explain.
// Output: NaN (Modulus by zero yields NaN)


// 7. Exponentiation and Assign =
// 1. Side of a cube is 5. Update it to get the volume using = 3.
let side = 5;
side = 3;

// 2. Number 4 needs to be squared. Use = 2.
let num2 = 4;
num2 = 2;

// 3. Predict the output: let base = 2; base = 5; console.log(base);
// Output: 32

// 4. Predict the output: let n = 4; n = 0.5; console.log(n);
// Output: 2

// 5. What is the result of let p = 2; p = -1;? Explain.
// Output: 0.5 (2 to the power of -1 equals 1/2)



// C] Comparison Operators


// 1. Loose Equality ==
// 1. Check whether the string "25" is loosely equal to the number 25.
// "25" == 25 -> true

// 2. Check if 0 == false returns true or false.
// 0 == false -> true

// 3. Predict the output: console.log(10 == "10"); console.log(null == undefined);
// Output: true, true

// 4. Predict the output: console.log("" == 0); console.log([] == false);
// Output: true, true

// 5. Why does NaN == NaN return false?
// NaN is never equal to anything, not even itself, by IEEE 754 standards.


// 2. Loose Inequality !=
// 1. Check whether "18" != 18 returns true or false.
// "18" != 18 -> false

// 2. A password is stored as "1234". User enters 1234 (number). Will != return true?
// false (they are loosely equal, so inequality is false)

// 3. Predict the output: console.log(5 != "5"); console.log(0 != false);
// Output: false, false

// 4. Predict the output: console.log(null != undefined); console.log("" != 0);
// Output: false, false

// 5. What does NaN != NaN return? Explain.
// true (NaN is not equal to NaN)


// 3. Strict Equality ===
// 1. Check whether "25" === 25 returns true or false. Explain why.
// false (Strict equality checks data types. "25" is a string, 25 is a number).

// 2. Check if 0 === false and null === undefined.
// 0 === false -> false, null === undefined -> false

// 3. Predict the output: console.log(10 === "10"); console.log(true === 1);
// Output: false, false

// 4. Predict the output: console.log("" === 0); console.log([] === false);
// Output: false, false

// 5. Why is === preferred over == in most real-world code?
// It prevents unexpected, silent type coercion bugs.


// 4. Strict Inequality !==
// 1. Check whether "18" !== 18 returns true or false.
// true (Since their types are different, they are strictly not equal).

// 2. Check if 0 !== false and null !== undefined.
// 0 !== false -> true, null !== undefined -> true

// 3. Predict the output: console.log(5 !== "5"); console.log(true !== 1);
// Output: true, true

// 4. Predict the output: console.log("" !== 0); console.log(NaN !== NaN);
// Output: true, true

// 5. Write a condition that checks if a variable input is strictly not equal to the string "0".
// input !== "0"


// ### Part C] Relational Operator

// 5. Greater Than >

// 1. A student’s marks are 78. The passing marks are 40. Check whether the student has scored more than the passing marks.
let studentMarks = 78;
let passingMarks = 40;
console.log("student passed? ",studentMarks > passingMarks)

// 2. Temperature today is 35°C and yesterday it was 28°C. Check if today is hotter.
let todayTemp = 35;
let yesterTemp = 28;
console.log("Hotter than yesterday?", todayTemp > yesterTemp)

// 3. Predict the output.
console.log(15 > 10);      // true
console.log(10 > 15);      // false
console.log(10 > 10);      // false

// 4. Preedict the output.
console.log("20" > 15);        // true
console.log("5" > "10");       // true
console.log("abc" > 10);       // false

// 5. What is the result of null > 0 and undefined > 0? Explain.
console.log(null > 0)        // false
console.log(undefined > 0)   // false

// 6. A shop has 120 items in stock. A customer wants to buy 85 items. Write a condition using > to check if stock is sufficient.
let stock = 120 ;
let need = 85 ;
console.log("Stock sufficient?", stock > need)

// 07. Predict the output.
console.log(true > false);      // true
console.log("10" > "2");        // false
console.log(NaN > 5);           // false


// 6. Less Than <

// 1. A box can hold maximum 50 kg. Current weight is 42 kg. Check if more items can still be added.
let max = 50;
let weight = 42;
console.log("can more items be added? ", max < weight)

// 2. Age of a person is 16. Minimum age required is 18. Check if the person is underage.
let age = 16;
let minAge = 18;
console.log("is Underage? ",age < minAge)

// 3. Predict the output: 8 < 12, 20 < 10, 7 < 7
// true, false, false

// 4. Predict the output: "8" < 10, "20" < "3", "hello" < 5
// true, true, false

// 5. What is the result of null < 0 and undefined < 0? Explain.
// false, false. null converts to 0, undefined converts to NaN.

// 6. A tank capacity is 500 litres. Current water level is 375 litres. Write a condition using < to check if it is not full.
// 375 < 500

// 7. Predict and explain: false < true, "5" < "15", NaN < 10
// true (0 < 1)
// false (string 5 comes after 1)
// false (NaN comparisons are always false)


// 7. Greater Than or Equal To >=

// 1. Minimum marks required for distinction is 75. A student scored 75. Check if the student gets distinction.
let studentMarks = 75;
let minMarks = 75;
console.log("student gets distinction? ",studentMarks >= passingMarks)

// 2. Ticket price is ₹300. A person has ₹300. Check if they can buy the ticket.
let price = 300;
let balance = 300;
console.log("Ticket affordable? ",price >= balance).

// 3. Predict the output: 25 >= 25, 30 >= 25, 20 >= 25
// true, true, false

// 4. Predict the output: "25" >= 25, "10" >= "2", null >= 0
// true, false, true

// 5. What is the result of undefined >= 0? Explain.
// false. undefined converts to NaN.

// 6. A lift can carry maximum 8 people. Currently 8 people are inside. Write a condition using >= to check if the lift is full or overloaded.
// 8 >= 8

// 7. Predict and explain: true >= 1, "" >= 0, NaN >= NaN
// true (1 >= 1)
// true (empty string becomes 0, so 0 >= 0)
// false (NaN cannot be compared to NaN)

  
// 8. Less Than or Equal To <=

// 1. Maximum speed limit is 60 km/h. A vehicle is travelling at 60 km/h. Check if it is within the limit.
let Max = 60;
let current = 60;
console.log("Within limit? ",max <= current)

// 2. A student needs at least 40 marks to pass. He scored 39. Check if he has failed.
let studentMarks = 39;
let passingMarks = 40;
console.log("student failed? ",studentMarks <= passingMarks)

// 3. Predict the output: 15 <= 20, 20 <= 15, 15 <= 15
// true, false, true

// 4. Predict the output: "15" <= 20, "30" <= "5", null <= 0
// true, true, true

// 5. What is the result of undefined <= 0? Explain.
// false. undefined converts to NaN.

// 6. A bag can hold maximum 10 books. Currently it has 10 books. Write a condition using <= to check if more books can be added.
let Max = 60;
let current = 60;
console.log("More books can be added? ",max <= current)

// 7. Predict and explain: false <= 0, "" <= 0, NaN <= 5
// true (false converts to 0)
// true (empty string converts to 0)
// false (NaN comparisons are always false)


// Mixed Practice (>, <, >=, <=)

// 1. Write expressions to check: Whether age 18 is greater than or equal to voting age 18. Whether temperature 32 is less than 35. Whether score 90 is greater than 85.
// Check if age is greater than or equal to voting age
let age = 18;
let votingAge = 18;
console.log(age >= votingAge); 

// Check if temperature is less than 35
let temperature = 32;
console.log(temperature < 35); 

// Check if score is greater than 85
let score = 90;
console.log(score > 85);

// 2. Predict the outputs: 10 > 5 && 5 < 10, "10" >= 10, null <= undefined, "5" < "10" && 5 > 2
// true, true, false, false

// 3. A product costs ₹499. A customer has ₹500. Write conditions using >= and < to decide if the customer can buy it and if any change will be left.
let productCost = 499;
let customerMoney = 500;

// Condition to decide if the customer can buy it (>=)
let canBuy = customerMoney >= productCost;
console.log("Can buy the product:", canBuy);

// Condition to check if any change will be left over (<)
let changeLeft = productCost < customerMoney;
console.log("Will have change left:", changeLeft);

// 4. Explain why "10" > "2" is false but 10 > 2 is true.
// "10" > "2" compares strings character by character. Since the first character "1" is smaller than "2", the result is false. 10 > 2 compares numeric values, and 10 is mathematically greater than 2, making it true.
