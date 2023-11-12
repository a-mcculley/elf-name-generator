# elf-name-generator
Used to generate proper LOTR elf names, was created for use in a RPG campaign
The underlying logic (like how to conjugate the prefixes properly) was curtesy of https://www.fantasynamegenerators.com/lotr-elf-names.php
That website generates 5 random names, this code generates all of them.
See comments for some details on how it functions
Recommended usage:
1. Remove any unwanted genders
2. Remove any unwanted suffixes (I dont recommend doing this, since even the bad looking ones can look good with a good prefix + conjugation)
3. Remove unwanted prefixes
4. Generate rejected lists semifrequently, if you wanna double check/make sure you didn't accidentally remove something good
5. Do multiple passes minimizing the prefix count
6. Once the total number of names gets down to a managable level, go through the list produced and manually trim down the names until you find the one you want

This version is after I had used it for many iterations. Female/Gender Neutral only, removed a ton of prefixes. Many many iterations, as can be seen by the rejected names. Also broke down the names I wanted into a few different categories. 
