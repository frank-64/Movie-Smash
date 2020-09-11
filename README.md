#Commits from after the git issue
(1) Sorry this should be multiple commits
(2) Parsed all the movies from movies.csv into the sqlite3 database after getting continuous errors which were due to the parse code being in the wrong area. Even though this does not seem correct, after the code was executed from the view, instead of it's own parse.py, the fault was fixed.
(2)Attempted to show all the movies in the sqlite3 database on index.html
 - This required me to store all the Model objects from the Movies model and store them in query_results.
 - Create a HTML table which use embedded python along with the context from query_results to get each attribute from the table and loop through each row.
 - Then use render to combine the index.html template with the table and the embedded Python tags to return a HTML response.