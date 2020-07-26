**Basic Lab 3.1**

1. *Go to Lab5.1 and unzip whitehouse_visits.zip file.*

2. *Using  tail command view all the records of whitehhouse file.*

3. *Using pig command we reach on grunt shell and make new directory named whitehouse.*

4. *Use the copyFromLocal command in the Grunt shell to copy the whitehouse_visits.txt file to the whitehouse folder in HDFS, renaming the file    visits.txt.*

5. *Using ls command verify that the file was uploaded successfully or not.*

6. *TextLoader simply creates a tuple for each line of text, and it uses a single chararray field that contains the entire line.*

7. *Using DESCRIBE command notice that A does not have a schema.*

8. *Using the LIMIT operator define a new relation named A_limit that is limited to 10 records of A.*

9. *Using the DUMP operator view the A_limit relation.*

10. *Loading the White House data again, but this time using the PigStorage loader and also define a partial schema.*

11. *Using the DESCRIBE command view the schema.*

12. *Using STORE command,stores the B relation into a folder named whouse_tab and separates the fields of each record with tabs.* 

13. *Using ls command Verify whouse_tab folder is created or not.*

14. *View one of the output files to verify they contain the B relation in a tab delimited  format.* 

15. *In the previous step, we stored a relation using PigStorage with a tab delimiter. Using following command,store same relation but in a JSON     format.*

16. *Verifying that the whouse_json folder is created.*

17. *View one of the output file.*
