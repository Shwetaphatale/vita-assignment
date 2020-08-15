**Hive Advance Lab 4-  Computing ngrams of Emails in Avro Format**

1. *Download the avro jar file.*

2. *Using getschema command check the contents.*

3. *Using put command put the file on hdfs.*

4. * Create sample.avsc table and add query which shows the avro.schema.url property. Save and run the file.*

5. *Start the hive shell and run the show table command to verify our table is successfully made. Using describe command check the contents of file. run the select query to      view the sample_table.*

6. *Using getschema mbox7.avro command check the file has mailing list for the month of July. Then put this file in hdfs.*

7. *Use more command view the contents of the create_email_table.hive.*

8. *Run the script to create the hive_user_email table.*

9. *Using select query check the contents of hive_user_email table.*

10. *Use the Hive ngrams function to create a bigram of the words in mbox7.avro.*

11. *Using the Hive explode function display the output in a more readable format.*

12. *This time add the Hive lower function and run the query again.*

13. *Run the following query, use context_ngrams function to find the top 20 terms that follow the word “error”.*

14. *Run a Hive query that finds the top 20 results and follow the phrase “error in.”*