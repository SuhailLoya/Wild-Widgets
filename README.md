## Video Demo
https://youtu.be/URk19elfuyU

## Inspiration
We live in a world of distractions and being bored is a thing of the past. Our hack Wild Widgets brings in a playful twist to a seemingly boring task like changing system controls. To fill up your "bored" time with annoying time, we introduce you to Wild Widgets which is a fun game that disrupts system settings to create an entertaining experience for users. 

## What it does
We’ve developed an application called Wild Widgets for a hackathon, and its unique concept adds a playful twist to the traditional tech troubleshooting experience. This application, always running in the background, periodically launches an "attack" every hour, disrupting system settings to create an entertaining challenge for users.

The attack includes:
1. Random Brightness: The brightness fluctuates unpredictably, adding an element of surprise to the user's visual experience.
2. Keystroke Changes: The keystrokes for each character become unpredictable. To type a character, users may need to press the same key multiple times, with the number of presses determined randomly.
3. Cursor Chaos: The cursor starts moving randomly around the screen, adding an extra layer of complexity to user interactions.
4. Volume Decrease: The volume continuously decreases, requiring users to constantly play the Volume Game to counteract the decline.

To overcome these challenges, users engage in four distinct games within the application:
1. Volume Game: A continuous pump-style game where pulling a lever in the GUI increases the volume. Traditional volume adjustments through laptop settings are ineffective.
2. Brightness Game: Random brightness drops every 1 hour prompt users to play a Jump Scare game, clicking a button to increase brightness in a random manner. After the desired brightness level is set, players can close the game and relax for the next three hours.
3. Keyboard Game: Once every 1 hour, Keystrokes are set to random numbers, requiring users to press the same character multiple times to type it. To bypass this attack, players must play the Keyboard game which involves completing a timed paragraph where each character has a random number of keystrokes set. When a wrong character is entered at any point or the time runs out, the user is forced to start typing the paragraph from the start. Once the paragraph is done, the keystrokes are set back to the default, which is 1 and the user can type normally for the next 1 hour.
4. Cursor Game: Once every 1 hour, the cursor starts behaving in a random manner, moving around the screen randomly. To counteract the random cursor movements, users must play the Cursor game which involves clicking an object moving in random directions with the given constraint, which is the cursor moving around the screen randomly.

It's important to note that these games are played after the initial attack. Playing them successfully resolves the disruption for the next 1 hour, with the exception of the Volume Game, which needs constant attention due to the ongoing volume decrease. Wild Widgets not only challenges users but also turns the inconvenience of tech disruptions into an engaging and entertaining experience.


## How we built it
Our application is built on Python, leveraging the Tkinter library. Since our application involved the manipulation of system controls, we also used several OS related libraries in Python.

## Challenges we ran into
Each game module was made with relative simplicity, however integrating the various games together on a common interface proved to be an extremely difficult task. Another tough challenge we ran into was managing system settings and orchestrating game functionalities. Since our application has to run the games in the background of the main application, we implemented threading, this too turned out to be a difficult task.

To address the need for parallel processing and enhance performance, we implemented threading—a crucial addition that allowed various processes to run concurrently. Navigating through the subtleties of Python, particularly in managing system settings and orchestrating game functionalities, brought about a deep appreciation for the language's versatility. The decision to exclusively leverage Python allowed us to harness its capabilities, resulting in a well-rounded application that seamlessly balances annoyance and enjoyment. Wild Widgets stands as a testament to the artful fusion of precision, creativity, and technical prowess in the world of application development.


## Accomplishments that we're proud of
We're proud of the fact that we were able to pull of such a hack in a short span of 24 hours. Having little to no experience in the various libraries used, we learnt various concepts and technologies on the go to implement one of the most annoying games ever.


## What we learned
We learnt how to use various libraries like Tkinter, Pygame, and OS related libraries. Crafting games that are simultaneously challenging and enjoyable demanded a nuanced approach, and we found ourselves immersed in the complexities of logic flow within the program. 

The development of Wild Widgets provided us with insights into the nuances of controlling system settings. We delved into the complexities of managing and manipulating various system parameters, gaining a deeper understanding of how to seamlessly integrate these controls into the user experience. 

Some of us were also introduced to concepts of parallel programming through the implementation of multithreading. Learning how to efficiently manage and coordinate these threads became a crucial aspect of the development journey. 

Through these challenges, we were also able to gain a deeper understanding of the importance of user experience, especially in unconventional applications like Wild Widgets. The experience reinforced the idea that successful design extends beyond mere functionality, emphasizing the need to create a seamless and enjoyable user journey.


## What's next for Wild Widgets
As part of our roadmap, we are exploring measures to disable force quitting from the Task Manager, force shutting down the device, etc. adding an element of persistence to the delightful annoyance the app brings.
