# Project: Logs Analysis
This project had us build a python script that connected to a PostgreSQL database and return SQL queries.

###Prerequisites

1. Vagrant VM
2. Python 3 with psycopg2 module installed
3. PostgreSQL

#### Code Design

1. It checks the database connection.
2. It then runs the 1st question query by running a `select` with a `count` function then joins the log and articles tables, concatenates the log.path with articles.slug, `group by` the title of the article, `order by` the count function descending so it shows the most views on top and `limit` to top 3 then prints the answer.

3. It then runs the 2nd question query by running a `select` with a `count` function then joins the log, articles, and authors tables, concatenates the log.path with articles.slug, `AND` uses the = operator to compare the articles.author table column with the authors.id column, then `group by` the authors name of the article, `order by` the count function descending so it shows the most views on top then prints the answer.

4. It then runs the 3rd question query using a `with` clause querying the log table. It first finds the number of requests per day using `num_requests`. Then it finds the number of errors per day by finding every other status except 200 OK statuses per day. Then it calculates the `error_rate` using the previous `num_requests` and `num_errors`. From there is does the `select` statement that finds the total amount of requests with a error rate greater than 1%.

##### How to run code

1. Create a new directory named news inside your vagrant folder
2. Copy newsserver.py file inside the newly created news directory
3. Open terminal and `cd` inside your vagrant directory you type `vagrant up`
4. Once VM is started you type `vagrant ssh` to log into the VM
5. You then `cd` into /vagrant directory
6. From inside the /vagrant directory inside your VM you type `python3 newsserver.py`
7. My python file will then run and output the answers inside the terminal.
8. Press Control-d to log out of the VM
9. Then type `vagrant halt` to shut down the VM

