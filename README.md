# Two Factor Authentication Through Morse Code Using Eye Blinks

A succint definition of this project is - a security tool that could potentially avoid/stop keylogger attacks by harnessing Morse Code technology to override the singular keyboard communication for password systems.

You can find the journal paper for this project [here](https://www.ijaresm.com/two-factor-authentication-through-morse-code-using-eye-blinks).


## **Steps to execute the code:**

**Step 1**: Run the file Morse_Login.py.

**Step 2**: A terminal opens which in turns opens the register/login panel to the user. The user is given the option of registering or login.

**Step 3**: Upon clicking the register button, the user must enter the username, password, and a security question. Once registration is complete, the system trains the dataset of the user over the haar cascade algorithm, and the user must go back to the previous step and click on login option.

**Step 4**: Once the username and password are entered correctly in the login option, the system trains a dataset of how the face of the user is using the haar cascade algorithm.

**Step 5**: The user is presented with a virtual keyboard containing the morse characters. When the morse code is entered correctly. The terminal signifies that the password entered in the keyboard is the same as the password entered over the morse code and the authentication is successful.