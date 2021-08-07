# Lab 18 - Cryprography

## Problem Domain

Create an encrypt function that takes in a plain text phrase and a numeric shift.

    the phrase will then be shifted that many letters.
        E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

    shifts that exceed 26 should wrap around
        E.g. encrypt(‘abc’,27) would return ‘bcd’

shifts that push a letter out or range should wrap around
    E.g. encrypt(‘zzz’,1) would return ‘aaa’

Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

Devise a method for the computer to determine if code was broken with minimal human guidance.

## Approach and efficiency

ord changes letters to number
chr changes number to letter

A - 65
Z - 90
a - 97
z - 122
' '-32

- encrypt(‘abc’,1) would return ‘bcd’ 
- encrypt(‘abc’, 10) would return ‘klm’
- shifts that exceed 26 should wrap around
  - encrypt(‘abc’,27) would return ‘bcd’

function
- check if key is greater than 25
  - if it is convert key to

  delcare result string
- iterate through each letter


    - declare converted = ord(letter)
    - check for lower or uppercase
    - if LOWERCASE
      (this means converted between 97-122)
      - changed = converted + key
      - if changed is greater than 122
          - find out the difference beween converted and 122
          - modulo that difference 25 or 26
          - add that difference to 97
          - then we have the encrypted letter


    - if uppercase
      (this means converted between 65-90)
      - changed = converted + key
      - if changed is greater than 90
          - find out the differenc between converted and 90
          - modulo that difference
          - add the difference to 65
          - then the the encrypted letter. 

    - if it neither
      just add the character

## Collaboration
 For this lab I collaborated with Davee Sok, Daniel Dills, Prabin Singh, and Micheal Ryan

