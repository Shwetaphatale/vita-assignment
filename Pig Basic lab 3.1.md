**Basic Lab 3.1**

1. *Go to Lab5.1 and unzip whitehouse_visits.zip file.*

![image](https://user-images.githubusercontent.com/63608018/88471865-70b9f580-cf2b-11ea-874e-b012dab1156b.png)

2. *Using  tail command view all the records of whitehhouse file.*

![image](https://user-images.githubusercontent.com/63608018/88471879-9646ff00-cf2b-11ea-8b67-fadb2dc18788.png)

3. *Using pig command we reach on grunt shell and make new directory named whitehouse.*

![image](https://user-images.githubusercontent.com/63608018/88471879-9646ff00-cf2b-11ea-8b67-fadb2dc18788.png)

4. *Use the copyFromLocal command in the Grunt shell to copy the whitehouse_visits.txt file to the whitehouse folder in HDFS, renaming the file  visits.txt.*

![image](https://user-images.githubusercontent.com/63608018/88471913-e7ef8980-cf2b-11ea-9fca-ba9febac0e7e.png)

5. *Using ls command verify that the file was uploaded successfully or not.*

![image](https://user-images.githubusercontent.com/63608018/88471916-efaf2e00-cf2b-11ea-9d2f-c836eb8c6e6d.png)

6. *TextLoader simply creates a tuple for each line of text, and it uses a single chararray field that contains the entire line.*

![image](https://user-images.githubusercontent.com/63608018/88471970-5af90000-cf2c-11ea-9832-36e5e44bf935.png)

7. *Using DESCRIBE command notice that A does not have a schema.*

![image](https://user-images.githubusercontent.com/63608018/88472095-3d786600-cf2d-11ea-8c1c-9b720fb9c64a.png)

8. *Using the LIMIT operator define a new relation named A_limit that is limited to 10 records of A.*

![image](https://user-images.githubusercontent.com/63608018/88472119-5aad3480-cf2d-11ea-8363-2418702be641.png)

9. *Using the DUMP operator view the A_limit relation.*

![image](https://user-images.githubusercontent.com/63608018/88472136-7284b880-cf2d-11ea-8edd-74b97ee4eefe.png)

10. *Loading the White House data again, but this time using the PigStorage loader and also define a partial schema.*

![image](https://user-images.githubusercontent.com/63608018/88472140-7d3f4d80-cf2d-11ea-92b9-d22367b9965c.png)

11. *Using the DESCRIBE command view the schema.*

![image](https://user-images.githubusercontent.com/63608018/88472166-abbd2880-cf2d-11ea-8d09-f5b089ad51a6.png)

12. *Using STORE command,stores the B relation into a folder named whouse_tab and separates the fields of each record with tabs.*

![image](https://user-images.githubusercontent.com/63608018/88472174-c0012580-cf2d-11ea-9435-0bc7628a73b6.png)

13. *Using ls command Verify whouse_tab folder is created or not.*

![image](https://user-images.githubusercontent.com/63608018/88472186-da3b0380-cf2d-11ea-832a-ab750943c998.png)

14. *View one of the output files to verify they contain the B relation in a tab delimited  format.* 

![image](https://user-images.githubusercontent.com/63608018/88472195-eb841000-cf2d-11ea-8baa-05ec7bd2f897.png)

15. *In the previous step, we stored a relation using PigStorage with a tab delimiter. Using following command,store same relation but in a JSON  format.*

![image](https://user-images.githubusercontent.com/63608018/88472206-0c4c6580-cf2e-11ea-9c8f-6ca078c9ed9a.png)

16. *Verifying that the whouse_json folder is created.*

![image](https://user-images.githubusercontent.com/63608018/88472216-1f5f3580-cf2e-11ea-9bda-0af27e03bfc5.png)

17. *View one of the output file.*

![image](https://user-images.githubusercontent.com/63608018/88472227-3e5dc780-cf2e-11ea-8f5d-aa25e38e0f3d.png)

