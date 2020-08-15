**Hive Basic Lab2- Analyzing Big Data with Hive**

1.  *Selecting all columns where the time_of_arrival is not empty. We will use the unix_timestamp for converting the time_of_arrival string into a timestamp.  Using limit            function we check 10 records.*

![image](https://user-images.githubusercontent.com/63608018/90313885-94ba9680-df2d-11ea-8902-a98d732c8ea6.png)

![image](https://user-images.githubusercontent.com/63608018/90313890-98e6b400-df2d-11ea-9a09-717a5e6f5b6f.png)

2. *Add desc to the order by clause to check records in reverse order in previous query.*

![image](https://user-images.githubusercontent.com/63608018/90313923-c59acb80-df2d-11ea-93b3-6cf97600b6e6.png)

![image](https://user-images.githubusercontent.com/63608018/90313927-cb90ac80-df2d-11ea-8749-f8dc4731a84c.png)

3. *Create a new text file named comments.hive and add info_comment field in  query to determine the most common comment. Group the results of the query. Order the results by       comment_countin desc order. Using limit check 10 records.*

![image](https://user-images.githubusercontent.com/63608018/90313954-ecf19880-df2d-11ea-99c8-f0434f394f5e.png)

![image](https://user-images.githubusercontent.com/63608018/90313964-f24ee300-df2d-11ea-93a8-d4d37c3c9890.png)

4. *Modify the query so that it ignores empty comments using where clause.*

![image](https://user-images.githubusercontent.com/63608018/90314004-3510bb00-df2e-11ea-85e6-522bd116284e.png)

![image](https://user-images.githubusercontent.com/63608018/90314009-3e9a2300-df2e-11ea-8e64-4aff62cf45f1.png)

5. *Removing DESC from order statement and add comment_count in the query.*

![image](https://user-images.githubusercontent.com/63608018/90314030-64272c80-df2e-11ea-81f8-8b1aeb3ffb96.png)

![image](https://user-images.githubusercontent.com/63608018/90314040-6d17fe00-df2e-11ea-9d95-81347a0997e8.png)

6. *Change the query Instead of searching for empty comments, search for comments that contain variations of the string “GEN RECEP.” and change limit to 30.* 

![image](https://user-images.githubusercontent.com/63608018/90314072-989ae880-df2e-11ea-8ced-e57cf380fe0e.png)

![image](https://user-images.githubusercontent.com/63608018/90314078-a2bce700-df2e-11ea-973c-02c1dc24a40a.png)

7. *Let’s add up the total number of them and run the query again.* 

![image](https://user-images.githubusercontent.com/63608018/90314369-dd278380-df30-11ea-98a6-b5b62ccea866.png)

![image](https://user-images.githubusercontent.com/63608018/90314374-e7e21880-df30-11ea-95c4-1445aedc343f.png)

8. *Change the where clause to match WHO and EOP. Add the DESC command back to the end of the order statement.*

![image](https://user-images.githubusercontent.com/63608018/90314398-22e44c00-df31-11ea-910c-d38eb67d32cd.png)

![image](https://user-images.githubusercontent.com/63608018/90314405-2972c380-df31-11ea-810d-88fa6c7f218e.png)

9. *Modify the query to counts the number of records with WHO and EOP in the comments.*
  
  ![image](https://user-images.githubusercontent.com/63608018/90314427-545d1780-df31-11ea-9f3e-428830a9e2c8.png)
  
  ![image](https://user-images.githubusercontent.com/63608018/90314431-5d4de900-df31-11ea-8453-5ee4843ed46c.png)

10. *Use a grouping by both fname and lname check most visited people's with desc order by clause  and limit changes to 20.* 

![image](https://user-images.githubusercontent.com/63608018/90314468-9ab27680-df31-11ea-9244-552827954379.png)

![image](https://user-images.githubusercontent.com/63608018/90314471-a4d47500-df31-11ea-8da0-d1f115283d70.png)


