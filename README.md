# Coffee Breaks with ChatGPT Repository

This repository contains the code files from the series of "My Coffee Breaks with ChatGPT"
Medium articles by Jeff Braun. The articles focus on using ChatGPT to assist with development
of Python programs for completing various types of data science tasks.

Article 1: [My Coffee Breaks with ChatGPT - Insights and Tips for Using ChatGPT in Real World Data Science Work — Part 1: Visualizations](https://medium.com/@jbraun_44616/my-coffee-breaks-with-chatgpt-d62f181b2ef4)

Article 2: [My Coffee Breaks with ChatGPT - Insights and Tips for Using ChatGPT in Real World Data Science Work -  Part 2: Creating Time-Series Models](https://medium.com/@jbraun_44616/my-coffee-breaks-with-chatgpt-490f1511c982)

The tips identified in the articles are consolidated in this README file.


## Tips and Suggestions from the Articles

- The more specific you can be in your request, the better the code you will get from ChatGPT. Providing links to the data you are using, providing variable names, and describing the end goal will get you a program that is ready-to-run, or very close to it.
- When asking ChatGPT to fix an error in the code, tell it the offending code statement and give it the text of the error - 'I get the error "TypeError ..." at statement "df = ..."' 
- Know when it is time to use a different research tool. It is tempting to keep on asking ChatGPT to correct a certain error in its code. At some point, though, you will probably get to an answer faster using a regular web query.
- Text token limits and heavy usage of the ChatGPT research release web portal can cause slow or incomplete responses. Sometimes entering "go on" in the request box after getting an incomplete response may get you the complete answer. You can also click the edit icon on your request and press "Save and Resubmit". 
- As your code grows, consider asking ChatGPT to only show you the new and changed code in its response.
- Remember that it takes an enormous amount of time to train the language models behind ChatGPT. The current version (version 3) is based on data current through part of 2021. If you need more current information, use other web search resources.
- Break your code requests to ChatGPT into multiple smaller function units (for example, missing value imputation, model creation/fitting, model prediction and testing, etc.) Doing this improve the likelihood that ChatGPT will generate code (versus just giving advice) and that the code will be useable. 
- On several occasions, ChatGPT's code used an approach that was new to me or that I would not have considered if I coded the algorithm myself from scratch. That was both enlightening and refreshing. But don't get in the habit of accepting ChatGPT's code blindly. Use your own knowledge and experience to tweak the code as appropriate for accurate results, faster performance, preferred style, etc. Also, review the code for potential algorithmic bias.
