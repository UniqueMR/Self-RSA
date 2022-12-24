# Self-RSA

This project is my implementation of the RSA asymmetric encrypting algorithm and its decrypting method. To get knowledge of the basic information of RSA, you can check https://en.wikipedia.org/wiki/RSA_(cryptosystem)

## Usage 

To test both the encrypting and decrypting methods together in a compact manner, you can run `python main.py -p <your p value> -q <your q value>`. The p and the q are both large primes. If you don't want to customize the prime value, you can just use the default value by running `python main.py`. Before you run the code, please be sure to put your message in the txt file. You may also use this project to encrypt and decrypt an image. Please put your original image inside the img directory and modify the path in the code. 

If you want to try encryption and decryption in an interactive way, you can run both server.py and client.py (even in different devices)  and then follow the instruction in the terminal. I'm sure you will explore further about the essence of RSA. 
