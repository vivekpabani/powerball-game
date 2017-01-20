# Rules of the game

1. Capture the name of the player entering the number.
2. The first 5 favorite numbers will need to be in the 
   range of 1 to 69 and unique. remember that this is a 
   drawing so there cannot be duplicates in this range of 5
   numbers)
3. 6th favorite number will need to be in the range of 1 to 26 
   and flagged as the 6th Powerball number.
4. Keep count of each individual favorite number provided to determine which
   numbers to use in our final winning number. (i.e. count the duplicates).
5. Retrieve the max count of each unique duplicate number and use them as the
   Powerball numbers.
6. if there is a tie based on the max counts randomly select the tied number.
7. Display all employees with their corresponding number entries.
8. Display the final Powerball number based on the requirements above.

# Sample output:

Enter your first name: Wade<br/>
Enter your last name: Wilson<br/>
select 1st # (1 thru 69): 12<br/>
select 2nd # (1 thru 69 excluding 12): 20<br/>
select 3rd # (1 thru 69 excluding 12 and 20): 23<br/>
select 4th # (1 thru 69 excluding 12, 20, and 23: 56<br/>
select 5th # (1 thru 69 excluding 12, 20, 23, and 56: 30<br/>
select Power Ball # (1 thru 26): 25<br/>


Wade Wilson 15 26 33 60 34 Powerball: 16<br/>
Frank Castle 15 26 34 56 61 Powerball: 16<br/>


Powerball winning number:<br/>
15 26 34 55 63 Powerball: 16<br/>
