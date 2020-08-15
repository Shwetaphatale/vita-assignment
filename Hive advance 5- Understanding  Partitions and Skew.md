**Hive Advance Lab 5-  Understanding Partitions and Skew**

1. *Go to demos folder and then go on grunt shell.*

2. *Run select query which shows the names.*

3. *Run select query which shows partitions names.*

4. *Check the recurssive folders present in hdfs using -ls -R command.*

5. *Run a select which shows names where state belongs to CA.* 

6. *When we specify a where clause that includes a partition, Hive is smart enough to only scan the files in that partition. Here no need to run a MapReduce job.*

7. *The following query spans multiple It shows names where state is CA or SD.*

8. *Make directory named salarydata and put salarydata file in hdfs.  Using more command view skew_demo file using the salaries.txt data.*

9. *Run the skewdemo file and see output.*

10. *View the contents of the underlying Hive warehouse folder. Select a few records to check the table has data behind it.*