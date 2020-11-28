# Django web application

## The Website
This Django web app now includes my website contains my project portfolio. The website is hosted using DigitalOcean with a Ubuntu virtual machine.
I used Nginx and Gunicorn together, Nginx is the web server, it decides where requests go and sends HTTP requests through reverse proxy for Gunicorn to handle and serves static files itself.

## What is Movie Smash?
Movie smash is a movie comparison web app which analyses the overall choices of the users to find the collective movie rankings.
The concept is based on Mark Zuckerberg's Face Smash which was designed to choose between two women based on their attractiveness.
However, in our Movie Smash users pick which movie they prefer which influences each movie's ranking (or elo) which allows the movies to be ranked.

## What I set out to do
* What I wanted to get out of this project:
    - Develop my skills using Django which is a framework I have never used before.
    - Further my web design experience.
    - Using Apache as well as port forwarding to allow access of my website across the internet
    - Refresh my database knowledge.

## What I used
* Django is a web application framework I used for this project. Django is a Python web framework which means ease of use due to the high-level nature of the language. This means you can focus on developing the web app whilst not having to worry about syntax and variable declaration.
* Web scraping for the movie images
    - This is the process of scraping basically any information from a website.
    - The web page is downloaded and parsed then queried for a certain HTML class/element type to find the data.
    - Some websites however do not allow the access of web scrapers as they disable them in the robots.txt file on their site.
* Hosted the website on an Apache server which I set up on a Ubuntu Virtual Machine.
* Mathematical algorithm for the elo ranking system which works as follows:
   - A choice is made between two movies by the user.
   - Example: Movie A: 1400 elo and Movie B: 1000 elo.
   - The way this algorithm works is by updating the elo based on the difference between the elo's.
   - So if Movie B was chosen over Movie A the percentage increase would be higher than vice versa.
   - Elo if A wins: A:1409.1 B:990.9
   - Elo if B wins: A:1309.1 B:1090.9 
   - As you can see when B was selected there was an 81.8 elo difference.
   - I would not say this is the best Algorithm I could have used for ranking but I liked the idea and understood it.
* SQLite3 database to store each movie's information and ranking.
    - SQLite3 is a small localised database stored on the device accessing it.
* CSV to parse the data from a CSV file into the SQLite3 database.
* HTML and JS to present the website.
* AJAX on the index.html page to post the user's results to the edit_rankings view which could then be used to access the database after performing the elo calculations.

## What I have learned
* Use small data sets while developing and testing a project.
    - Parsing and working with large datasets becomes increasingly difficult especially for hardware strenuous tasks.
    - large datasets can also cause havoc with git as there is a minimum file size git will allow. I learned this the hard way as I almost lost all my commits due to a .gz file preventing me from pushing anything to GitHub. To get around this I had to use git reset HEAD --hard to remove the commit containing the large file.
* There is often someone who experienced the exact same issue as you, I just need to get better at Googling. Now, I understand this is not always the best solution especially as an intermediate programmer, doing it yourself forces you to understand the process. However, after being stuck on something as simple as trying to order rows by a descending column I needed another solution. After trying to use a Datatables JS library and manually sorting the rows in Javascript I luckily found that Django has an order_by method which would have saved me three hours had I know where to look.
* My commits need to be more consistent.
    - Each commit should be more isolated with each containing one main fix/addition.
    - The commit messages should follow a more concise format each time.

# Things I could have done better
* As this is one of my first projects many things could be improved but I wanted to do this project for fun and experience more than correctness. Here are some things that could have been better:
    - Reading the AJAX post in the edit_rankings view was very clunky as it sends the movieID's as a string split by a comma but I was struggling with get the post parameters so I settled for the current implementation.
    - I had a lot of trouble with the scraping of the Movie images to use on the webpage. This is because I had to parse Google to find the images but only some had URLs that could be saved in the database and the URLs I did successfully parse were only thumbnails and I could not figure out how to get the full image.
    - Throughout my HTML I used style instead of having a separate CSS file, this would have been so much easier for implementing multiple classes using the same style but I had some issues with the CSS file being read as Django store static files differently and I couldn't get it to work.

