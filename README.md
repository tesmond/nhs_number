# NHS Numbers

While old NHS Numbers are 9 digits the new NHS numbers have 10 digits with the 10th digit being a check digit. The code in this repo is just a simple function that validates a 10 digit NHS Number returning a true or false outcome based on the input number.

## NHS Number Validation
The NHS NUMBER is 10 numeric digits in length. The tenth digit is a check digit used to confirm its validity. The check digit is validated using the Modulus 11 algorithm and the use of this algorithm is mandatory. There are 5 steps in the validation of the check digit:

### Step 1
Multiply each of the first nine digits by a weighting factor as follows:

Digit Position (starting from the left) Factor:

| Position | Factor |
| :---: | :---: |
| 1 | 10 |
| 2 | 9 |
| 3 | 8 |
| 4 | 7 |
| 5 | 6 |
| 6 | 5 |
| 7 | 4 |
| 8 | 3 |
| 9 | 2 |

### Step 2
Add the results of each multiplication together.

### Step 3
Divide the total by 11 and establish the remainder.

### Step 4
Subtract the remainder from 11 to give the check digit.

If the result is 11 then a check digit of 0 is used. If the result is 10 then the NHS NUMBER is invalid and not used.

### Step 5
Check the last digit matches the check digit. If it does not, the NHS NUMBER is invalid.

# Performance

While this is a simple function, why not use it to explore pythons performance. My initial working version took 0.014 seconds to validate 10,000 calls. So optimizing this obviously seems like a waste of time, when would you ever need to validate 1 million NHS numbers per second? However, it is a useful exercise as you might need to perform similar translations on a much larger volume of data. The regex check was relatively slow compared to a simpler length and digit check. Using sum() was slower than incrementing a total in a for loop. Using ord rather than int for the string to digit conversion was also faster. All of these changes combined to a reduction in runtime of 50% to 0.007 seconds to validate 10,000 calls.