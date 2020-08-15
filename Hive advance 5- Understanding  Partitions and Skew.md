**Hive Advance Lab 5-  Understanding Partitions and Skew**

1. *Go to demos folder and then go on grunt shell.*

![image](https://user-images.githubusercontent.com/63608018/90313354-7f436d80-df29-11ea-8a00-dfa493fee706.png)

2. *Run select query which shows the names.*

![image](https://user-images.githubusercontent.com/63608018/90313362-8c605c80-df29-11ea-9427-a3acfa81ddd5.png)

3. *Run select query which shows partitions names.*

![image](https://user-images.githubusercontent.com/63608018/90313368-a437e080-df29-11ea-82bf-3f0ce44321dd.png)

4. *Check the recurssive folders present in hdfs using -ls -R command.*

![image](https://user-images.githubusercontent.com/63608018/90313369-ad28b200-df29-11ea-896e-81a4bbb2f4f7.png)

5. *Run a select which shows names where state belongs to CA.* 

![image](https://user-images.githubusercontent.com/63608018/90313386-cb8ead80-df29-11ea-88ec-77f13b9d11b6.png)

6. *When we specify a where clause that includes a partition, Hive is smart enough to only scan the files in that partition. Here no need to run a MapReduce job.*

![image](https://user-images.githubusercontent.com/63608018/90313394-d34e5200-df29-11ea-8afd-28bbfd24219e.png)

7. *The following query spans multiple It shows names where state is CA or SD.*

![image](https://user-images.githubusercontent.com/63608018/90313410-fd077900-df29-11ea-8bf2-d9d8d37d776c.png)

8. *Make directory named salarydata and put salarydata file in hdfs.  Using more command view skew_demo file using the salaries.txt data.*

![image](https://user-images.githubusercontent.com/63608018/90313414-0abcfe80-df2a-11ea-9ba7-8e861bb9f2b7.png)

9. *Run the skewdemo file and see output.*

![image](https://user-images.githubusercontent.com/63608018/90313488-96cf2600-df2a-11ea-9cd7-b0e34c4a785e.png)

10. *View the contents of the underlying Hive warehouse folder. Select a few records to check the table has data behind it.*

![image](https://user-images.githubusercontent.com/63608018/90313503-bf572000-df2a-11ea-8a5f-e8617d294fc0.png)
