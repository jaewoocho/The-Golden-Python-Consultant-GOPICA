Failures and Ending Comments

For the final code submission, I had to go through several adjustments for my code. 
I had problems with the real time gold price API from xignite, the first API I used from xignite that used to work perfectly as shown in Figure 1 and in phase 2. 
I tried to contact with the xignite API director, however I couldn't extend my access to the API. 
As the real time gold price API from xignite didn't work, I had to find new real time gold price APIs and change my algorithm in my code as seen from above. 
Finding another plan B real time gold API was hard as most of the companies that had the gold APIs required a confidential profile or a high "exchange" rate price to access the gold price API. 
Luckily, I have managed to find a real time gold price API that had a 50 requests per month limit.
This wasn't as great as the xignite API from Figure 1, but at least I was able to use this API to bring gold prices. 
For the current dates, I easily found the python date function to call the date from the jupyter notebook server timer in Syracuse. 

I also had problems with the financial Bloomberg API as it constantly changed their API format. 
This lead to the change of my code and breaking functions in to separate code functions to handle errors. 
Handling errors was one of the biggest problems in my code as the API format changed, the user defined functions for modularity kept on creating new errors. 
Before the bloomberg financial news API changed, it worked perfectly like in FIgure 2, 3. 
Eventually, I had to break the existing functions and had to hard code each line to create a flexible program for the constant change in the APIs. 
This also lead to problems with creating try: except error handlers as everytime the API format changed, there was always a new error or problem that bugged the whole program.
For formatting my project, I used multiple print statements in my code to create a scalable format for the dialogues from GOPICA. 
As GOPICA is a gold python consultant, the information and data represented for the user must be easily readable. 
So I used multiple print statements with \n spaces so that the size of the window of the program output wouldn't effect the readability for the user. 
For example, for users on a large screen, reading the text and data would be easy. 
However, for users on different smaller screen sizes, the layout of the text would be hard to read as it would be compacted like an essay. 

![figure 1](https://user-images.githubusercontent.com/25238652/120664191-b2a9b580-c4c5-11eb-91e7-10b935d0c51a.PNG)
![figure2](https://user-images.githubusercontent.com/25238652/120664205-b50c0f80-c4c5-11eb-9a56-47f46c57bf47.PNG)
![figure 3](https://user-images.githubusercontent.com/25238652/120664216-b6d5d300-c4c5-11eb-962e-205abe00a60e.PNG)



