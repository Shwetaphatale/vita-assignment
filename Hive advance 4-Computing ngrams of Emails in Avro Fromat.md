**Hive Advance Lab 4-Computing ngrams of Emails in Avro Format**

1. *Download the avro jar file.*

![image](https://user-images.githubusercontent.com/63608018/90313012-8e74ec00-df26-11ea-823c-81812e7a7eab.png)

2. *Using getschema command check the contents.*

![image](https://user-images.githubusercontent.com/63608018/90313014-959bfa00-df26-11ea-9aae-d016ff070e5f.png)

3. *Using put command put the file on hdfs.*

![image](https://user-images.githubusercontent.com/63608018/90313032-c0864e00-df26-11ea-8521-00b3787f1637.png)

4. *Create sample.avsc table and add query which shows the avro.schema.url property. Save and run the file.*

![image](https://user-images.githubusercontent.com/63608018/90313035-c8de8900-df26-11ea-90a9-33e6dc665ac0.png)

![image](https://user-images.githubusercontent.com/63608018/90313049-e6135780-df26-11ea-89a8-c93889a69f36.png)

5. *Start the hive shell and run the show table command to verify our table is successfully made. Using describe command check the contents of file. run the select query to         view the sample_table.*

![image](https://user-images.githubusercontent.com/63608018/90313055-f88d9100-df26-11ea-8bb8-38cbea9fd679.png)

6. *Using getschema mbox7.avro command check the file has mailing list for the month of July.Then put this file in hdfs.*

![image](https://user-images.githubusercontent.com/63608018/90313076-2ecb1080-df27-11ea-82d6-17dd5b6a796a.png)

7. *Use more command view the contents of the create_email_table.hive.*

![image](https://user-images.githubusercontent.com/63608018/90313113-879aa900-df27-11ea-8744-a7b68fc6d516.png)

8. *Run the script to create the hive_user_email table.*

![image](https://user-images.githubusercontent.com/63608018/90313090-515d2980-df27-11ea-8639-2539cb520081.png)

9. *Using select query check the contents of hive_user_email table.*

![image](https://user-images.githubusercontent.com/63608018/90313120-a5680e00-df27-11ea-8bc0-c96503fff076.png)

10. *Use the Hive ngrams function to create a bigram of the words in mbox7.avro.*

![image](https://user-images.githubusercontent.com/63608018/90313141-c0d31900-df27-11ea-9e6f-0489834d2e9a.png)

11. *Using the Hive explode function display the output in a more readable format.*

![image](https://user-images.githubusercontent.com/63608018/90313161-e102d800-df27-11ea-82bd-83da836b9114.png)

12. *This time add the Hive lower function and run the query again.*

![image](https://user-images.githubusercontent.com/63608018/90313171-f7a92f00-df27-11ea-9726-4be60fff710d.png)

13. *Run the following query, use context_ngrams function to find the top 20 terms that follow the word “error”.*

![image](https://user-images.githubusercontent.com/63608018/90313192-17405780-df28-11ea-95ad-e6a174a9f480.png)

14. *Run a Hive query that finds the top 20 results and follow the phrase “error in.”*

![image](https://user-images.githubusercontent.com/63608018/90313211-5373b800-df28-11ea-94cb-2ab0d14e0205.png)
