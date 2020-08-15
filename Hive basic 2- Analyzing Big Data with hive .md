**Hive Basic Lab2- Analyzing Big Data with  Hive**

1.  *Selecting all columns where the time_of_arrival is not empty. We will use the unix_timestamp for converting the time_of_arrival string into a timestamp.  Using limit function we check 10 records.*
   
2. *Add desc to the order by clause to check records in reverse order in previous query.*

3. *Create a new text file named comments.hive and add info_comment field in  query to determine the most common comment. Group the results of the query. Order the results by  comment_countin desc          order.  Using limit check 10 records.*

4. *Modify the query so that it ignores empty comments using where clause.*

5. *Removing DESC from order statement and add comment_count in the query. *

6. *Change the query Instead of searching for empty comments, search for comments that contain variations of the string “GEN RECEP.” and change limit to 30.* 

7. *Let’s add up the total number of them and run the query again.* 
 
8. *Change the where clause to match WHO and EOP. Add the DESC command back to the end of the order statement.*

9. *Modify the query to counts the number of records with WHO and EOP in the comments.*
  
10. *Use a grouping by both fname and lname check most visited people's with desc order by clause  and limit changes to 20.* 