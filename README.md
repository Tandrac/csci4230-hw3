# csci4230-hw3
Once I figured how the Blum Goldwasser Probabilistic Algorithm actually worked, it wasn't too hard to implement. This was made especially easy due to the fact that both the encryption and decryption shared much of the same code. One thing that I didn't consider until the middle of the homework was that often times some of the modular calculations I was doing grew too large before they were moded, so I had to switch to using the math pow function. I originally also tried to use some proper binary math (like bitwise), but I ended up using python casting and string manipulation like always.


My cypher text was: 00100000110011100100
