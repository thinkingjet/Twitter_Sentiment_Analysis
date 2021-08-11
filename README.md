# Twitter_Sentiment_Analysis
A Sentiment Analysis Program That Gets the Top 100 Tweets relating to a certain keyword, performs sentiment analysis on the tweets, and then graphs them

# New, As of 12th August 2021
Competition submissions attached as well


## Comp Details:

@everyone @Competitor 

Ok Second Competition:

This one is **a lot harder** than the previous one guys, so **don't stress** if you can't finish it. 
> "A little progress each day adds up" - unknown:pepeyoucantseeme: 


**__Important things to keep in mind:__**
1) You will get **__exactly one week__** from now to finish the competition. :one:  :roundtable_next_week: 
2) **The allowed modules for this competition are:**
    1. `tweepy`   ->  `pip install tweepy`
    2. `textblob`   -> `pip install textblob`
    3. `matplotlib.pyplot`   ->  `pip install matplotlib`
    4. `re`   ->  `pip install regex`
    5. `pandas`   -> `pip install pandas`
3) **To import these modules, add the following at the top of your python file:**
```python
import tweepy
import textblob
import pandas as pd
import matplotlib.pyplot as plt
import re
```
__4) You will be using the **Twitter api** for this challenge. I strongly recommend you get your own **__for free__** by going here:pepelike: : https://developer.twitter.com/en/apply-for-access
__
5) ***In case you guys can't get your own api keys for whatever reason, I am providing my own twitter api keys and access tokens along with their respective secrets below:cyanbook: :***
```python
api_key = "x2XjAlMEW7UzorVmKAviXLYZX"
api_key_secret = "CSVoUoCwB2W9R2RfhRX1zXZQa7xrW1zzM9naISGJN1v9IeHV7j"
access_token = "1007964620164759552-vF2IGdfuXB7Z0FBxGNidx1IKy6ww7K"
access_token_secret = "WIivnWduK1dLCWKohGoYrDv5nSqanwRLgGrxMjM6DPucj"
```

**__*DISCLAIMER:red_circle: : DO NOT TRY AND GO BEYOND THE SCOPE OF THE COMPETITION. DO NOT TRY AND MESS WITH MY ACCOUNT, DOING SO WILL RESULT IN AN IMMEDIATE AND PERMANENT BAN(AND I HAVE WAYS OF TRACKING THE USAGE OF MY API KEYS :wink:  )
**__*

6) The top 3 winners will get the @1st Place @2nd Place and @3rd place tags respectively. The winner will be determined based off the code efficiency, and time of submission.


**Now on to the actual competition:sweat_smile: :**
***The task is a bit lengthy this time, so I'm detailing the steps below:***
1) Set `topic, start_date, end_date and tweet_limit` **variables to **anything,(The `start_date` and `end_date` have to be `"2021-08-03"` and `"2021-08-08"` respectively :tridentblob: )

2) Your first task is to **scrape the top hundred tweets** relating to the `topic`, ranging between the `start_date` and the `end_date` using the `tweepy, regex and pandas modules`

3) After you can successfully get the top 100 tweets relating to any `topic`, and print them to the console using a simple ||for loop||, you now have to **perform sentiment analysis** on them using the `textblob` module, based on them being either positive or negative.

4) **This step will be hard!** It is probably going to be the most time consuming part of the whole challenge, so don't give up! (You might still have a chance of winning if no one submits their code, and you submit part of yours even if its not finished :stuck_out_tongue: ) 

5) That's done, now on to the second last part. You need to use the python ||map()||function along with ||lambda||to assign a `+` or `-` value to the tweets. When you used the `texblob` module on the ||pandas dataframe|| and assigned it to a new ||column||, you should've used ||`lambda tweet: textblob.TextBlob(tweet).sentiment.polarity`||

6) If you did step 5 correctly, you can easily assign `'+'` or `'-'` values to the column.

7) The final step! Now that you've done the above, the last part is easy. Simply use the `matplotlib.pyplot` module to plot a bar graph which plots the data based on positivity vs negativity. The final output is attached, and yours should look similar to it. This one which gets the **top 100 tweets about bitcoin** between the dates `2021-08-03 and 2021-08-08`.

8) Step 8?! NO, that's it the comp's done. To submit your code, follow the steps below:


## Submission
To submit your code, do the following:
In #bot-commands , type the following:
?ticket create <your_name> where <your_name> is to be replaced by your actual name. 

After you do that, you will see that a new channel pops up for you just above the COMMUNITY category, it appears in a new categor called Competition Submissions. It should look similar to the attached screenshot. 

Now go to that channel, and paste in your code. We will review it throughout the week, and after one week you'll be informed if you're a winner!

You have exactly 1 week from now, till 10 am UTC, Thursday 12th August
Good Luck!:Likee:

PS: Final Code Right Here: https://bit.ly/challenge_final_code
<img src=https://cdn.discordapp.com/attachments/862330721413890078/872780733624750090/unknown.png></img>

