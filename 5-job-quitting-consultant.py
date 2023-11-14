# Display a cool relevant ASCII art
print('''
         _,,,_
       .'     `'.
      /     ____ \
     |    .'_  _\/
     /    ) a  a|         .----.
    /    (    > |        /|     '--.
   (      ) ._  /        ||    ]|   `-.
   )    _/-.__.'`\       ||    ]|    ::|
  (  .-'`-.   \__ )      ||    ]|    ::|
   `/      `-./  `.      ||    ]|    ::|
  _ |    \      \  \     \|    ]|   .-'
 / \|     \   \  \  \     L.__  .--'(
|   |\     `. /  /   \  ,---|_      \---------,
|   `\'.     '. /`\   \/ .--._|=-    |_      /|
|     \ '.     '._ './`\/ .-'          '.   / |
|     |   `'.     `;-:-;`)|             |-./  |
|    /_      `'--./_  ` )/'-------------')/)  |
\   | `""""----"`\//`""`/,===..'`````````/ (  |
 |  |            / `---` `==='          /   ) |
 /  \           /                      /   (  |
|    '------.  |'--------------------'|     ) |
 \           `-|                      |    /  |
  `--...,______|                      |   (   |
         | |   |                      |    ) ,|
         | |   |                      |   ( /||
         | |   |                      |   )/ `"
        /   \  |                      |  (/
    . .' /I\ '.|                      |  /)
   .-'_.'/ \'. |                      | /
   ```  `"""` `| .-------------------.||
               `"`                   `"`
''')

# Welcome message
print("Welcome to the job quitter consultant!")

# Get user input for the first question and convert to lowercase for case-insensitive comparison
q1 = input("Are you generally satisfied with your current job role? (y/n)").lower()

if q1 == "y":
    # Subsequent questions for the positive pathway
    q2 = input("Do you feel that your work aligns with your long-term career goals? (y/n)").lower()
    
    if q2 == "y":
        q4 = input("Do you feel valued and compensated in your job? (y/n)").lower()
        
        if q4 == "y":
            print("You might want to continue in your job as it seems to fulfill most of your needs.")
        else:
            q7 = input("Do you believe you could find a job that better meets your needs and aspirations? (y/n)").lower()
            
            if q7 == "y":
                print("It might be worth exploring new opportunities.")
            else:
                print("Consider if there are ways to address the issues in your current job.")
    else:
        q5 = input("Are there opportunities for growth and learning in your current job? (y/n)").lower()
        
        if q5 == "y":
            q7 = input("Do you believe you could find a job that better meets your needs and aspirations? (y/n)").lower()
            
            if q7 == "y":
                print("It might be worth exploring new opportunities.")
            else:
                print("Consider if there are ways to address the issues in your current job.")
        else:
            q8 = input("Have you explored and exhausted all avenues for improving your current job situation? (y/n)").lower()
            
            if q8 == "y":
                print("It might be time to consider quitting.")
            else:
                print("Try addressing these issues before deciding to quit.")
else: 
    # Subsequent questions for the negative pathway
    q3 = input("Is your job negatively affecting your mental or physical health? (y/n)").lower()
    
    if q3 == "y":
        print("You should strongly consider quitting, as health is a priority.")
    else:
        q6 = input("Do you have significant financial or personal reasons that require you to stay in your job? (y/n)").lower()
        
        if q6 == "y":
            print("You may need to continue for now but look for ways to improve your situation or prepare for a change.")
        else:
            q8 = input("Have you explored and exhausted all avenues for improving your current job situation? (y/n)").lower()
            
            if q8 == "y":
                print("It might be time to consider quitting.")
            else:
                print("Try addressing these issues before deciding to quit.")

# Closing message
print("Thank you for using the job quitter consultant! Have a nice day!")
