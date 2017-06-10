# Al-Jazeera Content Abuse Project

## Introduction:
We consume an enormous amount of digital content every day, perhaps more than any previous generation.  Whether it is YouTube, Facebook, Twitter, Hulu, a newspaper we are constantly consuming and contributing gbytes of content without much thought.  With this democratization of data, i.e. its availability and your ability to contribute to it, there is quite a spectrum of users.  One one end of the spectrum, users post content that is relevant and appropriate for others to view and read, but the opposite is also true.  Others have used such forums to post irrelvant or inappropriate comments, sometimes at scale.  For those who abuse the system, there is quite of spectrum of damage they can do ranging from that which trivial to non-trivial.  For example, a troll posting business listings repeatedly on a news website is annoying, but a radicialized citizen posting hate speech could be a national security threat.  Understanding the behaviors of such content abusers from both ends of the spectrum will become increasingly important for companies and governments in the future.  It is in this vein, the following projects hopes to explore creative ways of identifying such content abusers more commonly known as "trolls."

## Problem
Al-Jazeera is a Doha-based state-funded broadcaster owned by the Al Jazeera Media Network, which is partly funded by the House of Thani, the ruling family of Qatar.  It is one of the largest, if not the largest most widely viewed media station in the Middle East claiming some 40 million viewers in the Middle East alone.

Al-Jazeera's website currently allows for readers to post their comments on virtually all articles posted on the media giants homepage. This freedom of publically expressing political opinions on highly charged and controversial topics on the Middle Eastern topics which governments often surpress or censor is unique.  

In regrards to content abusers, their impact can have minimal or long-term impacts. Content abusers tend to create unhealthy social ecosystem (reduces users desire to participate in discussion), they can create a legal liabilities, can impact company ROI, churn rate, ability to attract talent or investors, ability to attract users, retain employees, to name a few.

Al-Jazeera currently has a number of users who post irrelevant or inappropriate comments on their webpage. The media giant currently relies on other users to report inappropriate comments or spam; however, there is little incentive for other readers to "police" the website especially at scale.  As a result, many "troll" comments remain on the page creating an unhealthy social environment for people who may legtimately want to discuss an issue, ask a question, or have a meaningful discussion. 

## Current Solutions:
Media companies and other major social media companies have approached the issue of trolls from different angles and with little consensus.  Some companies have decided:

1. Ban comments altogether such as U.S. media giant CNN:http://www.cnn.com/2014/11/21/tech/web/online-comment-sections/), 
2. Others tolerate negative comments under the umbrella of “free speech, like Breitbart:http://www.breitbart.com/tech/2015/10/27/the-lefts-war-on-comment-sections/), 
3. Others are hiring labor force to flag negative comments, like Facebook:http://www.npr.org/sections/thetwo-way/2017/05/03/526727711/facebook-plans-to-add-3-000-workers-to-monitor-remove-violent-content),  
4. Others leverage technology to curb the volume of negative comments, like Twitter: https://www.nytimes.com/2016/11/16/technology/twitter-adds-new-ways-to-curb-abuse-and-hate-speech.html?_r=0). 

Company policies regarding what to remove, censor, or flag are in constant flux, especially with the advent of new technologies that make it easier and more efficient to identify abusers.  However, many challenge still remain, and al-Jazeera is facing many of the same challenges its competitors are grappling with 


## Purpose:

The purpose of this project identify content abusers currently using al-Jazeera's plaform.  To find such users on Al-Jazeera's entire platform with its own employees would take a vast labor force, a lot of money, and it would still not likely be acheived.  However, cleverly using machine learning to cut through vast amounts of data can signal when users post negative comments, how often they post, and what they post. Al-Jazeera could then decide if they wanted to use the tool internally as an exploratory way to monitor content abusers, or have it automatically classify or suspend certain users based on a certain threshold.  In either case, reducing the number of trolls would reduce the risk of retaining users, employees, users, investors, among other things. 

## Data:
The data used in the following project stems directly from al-Jazeera's homepage (www.aljazeera.com).  Data was webscraped daily at 5 p.m for a period of two weeks during the Spring of 2017. 

## Analysis:
See DAG and code.

## Results:
Trolls on al-Jazeera can be classified in one of three categories: Business Trolls, Hate Speech Trolls, Sarcastic Trolls.

### Business Trolls:
1. Try to sell a product or service when their product or service is irrelevant to the article, website, or conversation. 
2. Typically post a lot of comments over a wide variety of articles in hopes of "getting a bite," i.e. having someone respond to their business proposals.  Essentially they are about volumne, preferencing visibility about content qualitity or some other factor. 

### Hate Speech Trolls:
1. Typically threaten other users (or people in general) with racist, lewd, foul language inappropriate for a comment forum.  
2. Typically really short or really long comments – in caps

### Sarcastic Trolls:
1. Clever trolls who may or may not use offensive, racist, or threatening remarks, but whose underlying intention for the comment is  dubious even hurtful 
2. Basically a Hate troll,  just not as explicit about it

## Next Steps:
There are many ways to build on the current work in understanding the behaviors of users to post "troll" comments on Al-Jazeera's homepage.

1. Conducting a longitudinal study of how behaviors changed over time using time series.
2. If al-Jazeera decided to suspend or ban a certain profile, monitoring the accounts closed and accounts opened within a given a time  frame would help repeat abusers.  
3. Is there a relationship between an article title and contents and the trolls who posted their comments on the page? What do topics tell us about the personalities of certain trolls?
4. Can trolls be clustered into a certain political group? If so, how does this contrast with the objective of al-Jazeera?


