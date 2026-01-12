# workout-parser Python application
> Copy and paste plaintext workout logs generated from Strong Workout Tracker app on android to get sets broken down by muscle group.

## Input Text Formatting
It is important that the copy-pasted text have some where in it this format  
 "number of sets for muscle group" x "muscle-group"
 
### Example Input Data from Strong
 3 x Biceps
 Biceps Curl (Dumbbells)
 12 reps @ 30 lbs
 12 reps @ 30lb
 10 reps @ 30 lb
 
 3 x Chest
 Chest Fly (Machine)
 12 reps @ 100 lbs
 10 reps @ 120 lbs
 9 reps @ 120 lbs
 9 reps @ 120 lbs

### Example Output
Muscle Summary
Biceps x 3 
After you copy and paste this, it will give you a readout of the total sets per muscle groups. It is essentially a useful calculator that takes in text and spits out a summary of your weekly workout volume.

## Contribution
Much of this code was initially AI generated using ChatGPT as I am still learning regex. I modified and iterated the code to improve the way it handled diferrent input formats. It is still a work in progress.
