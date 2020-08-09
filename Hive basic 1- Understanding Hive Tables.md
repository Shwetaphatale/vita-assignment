1. *First do some command from pig lab where unzip whitehouse_visits folder and go on the warehouse path.*

![image](https://user-images.githubusercontent.com/63608018/89736062-70ba0980-da84-11ea-9156-dfa5796b07c0.png)

![image](https://user-images.githubusercontent.com/63608018/89736531-b3311580-da87-11ea-888b-15bf55431d2b.png)

![image](https://user-images.githubusercontent.com/63608018/89736545-ca700300-da87-11ea-847f-0aa24880be1a.png)

![image](https://user-images.githubusercontent.com/63608018/89736554-deb40000-da87-11ea-921f-22f3f55260b9.png)

2. *Using hdfs dfs -ls command check the contents of wh_visits file.*

![image](https://user-images.githubusercontent.com/63608018/89736520-9b599180-da87-11ea-9205-e9415808442e.png)

3. *Using more command check the file contents.*

![image](https://user-images.githubusercontent.com/63608018/89736502-71a06a80-da87-11ea-98ac-8a6ba5864920.png)

4. *Then go on grunt shell and using show tables command check all the tables.*

![image](https://user-images.githubusercontent.com/63608018/89736485-5cc3d700-da87-11ea-9ecd-5cc0cc3c1a72.png)

5. *To load the records first take the all records in warehouse file path and then run select query and it shows 20 records from wh_visits file.*

![image](https://user-images.githubusercontent.com/63608018/89736468-3d2cae80-da87-11ea-9b69-0d07c360eac6.png)

6. *Using count command it shows how many rows are present in that file.*

![image](https://user-images.githubusercontent.com/63608018/89736458-2423fd80-da87-11ea-8aab-9e1918f2a69d.png)

7. *Using select query where lname LIKE '%y' we get records whose last name starts with y.*

![image](https://user-images.githubusercontent.com/63608018/89736424-e32be900-da86-11ea-9485-869f5e002fe1.png)

8. *Create  new table on hive.*

![image](https://user-images.githubusercontent.com/63608018/89736402-c98aa180-da86-11ea-942d-db1fbfb27c3c.png)

9. *Go to lab 7.1 folder in hdfs and put names.txt file in whitehouse folder.*

![image](https://user-images.githubusercontent.com/63608018/89736384-afe95a00-da86-11ea-943a-cc50de9d3ddb.png)

10. *After that go on grunt shell and using dfs -ls command check list of files stored in folder.*

![image](https://user-images.githubusercontent.com/63608018/89736375-96e0a900-da86-11ea-80bf-c5b799bccdd3.png)

11. *Again load the names.txt file and run query related with names.*

![image](https://user-images.githubusercontent.com/63608018/89736335-4701e200-da86-11ea-9b33-3617ab1cf9fb.png)

12. *Then drop the names table.*

![image](https://user-images.githubusercontent.com/63608018/89736358-7284cc80-da86-11ea-9630-988bd0d75eb8.png)

13. *Put names.txt file in lab7.1*

![image](https://user-images.githubusercontent.com/63608018/89736312-246fc900-da86-11ea-81fb-55f27e7a05d3.png)

14. *Create a folder for external table.*

![image](https://user-images.githubusercontent.com/63608018/89736282-e2468780-da85-11ea-80d8-b484810e39c5.png)

15. *Create external table using external keyword before table.*

![image](https://user-images.githubusercontent.com/63608018/89736294-fb4f3880-da85-11ea-8331-7f95b341854f.png)

16. *Load data into table.*

![image](https://user-images.githubusercontent.com/63608018/89736247-9bf12880-da85-11ea-8d41-b7a3ee055128.png)

17. *Verify load command is worked using select query.*  

![image](https://user-images.githubusercontent.com/63608018/89736232-7ebc5a00-da85-11ea-8b01-2ac9beb98dba.png)

18. *Notice the names.txt file has been moved to /user/root/hivedemo.*

![image](https://user-images.githubusercontent.com/63608018/89736209-57fe2380-da85-11ea-89d7-4a96ffdef543.png)

19. *Now drop names tables.*

![image](https://user-images.githubusercontent.com/63608018/89736179-313fed00-da85-11ea-911d-2c8cf6411734.png)

20. *View the contents of /user/root/hivedemo. Notice that names.txt is still there.*

![image](https://user-images.githubusercontent.com/63608018/89736147-ef16ab80-da84-11ea-993d-ce0bd083ad86.png)






