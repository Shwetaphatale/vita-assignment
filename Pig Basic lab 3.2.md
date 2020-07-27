**Basic Lab 3.2**

1. *On grunt shell use TextLoader to load the visits.txt file.*

![image](https://user-images.githubusercontent.com/63608018/88528132-d84f6e00-d01b-11ea-85bd-164c2078e50d.png)

2. *Using DESCRIBE command view schema B.*

![image](https://user-images.githubusercontent.com/63608018/88530658-53feea00-d01f-11ea-9f90-bd1095344421.png)

3. *Using the COUNT function determine how many lines of text are in visits.txt.*

![image](https://user-images.githubusercontent.com/63608018/88530737-77c23000-d01f-11ea-89cd-c6eb6390718d.png)

4. *Use DUMP A view the result.*

![image](https://user-images.githubusercontent.com/63608018/88530892-ab9d5580-d01f-11ea-856f-f398ee38ed17.png)

![image](https://user-images.githubusercontent.com/63608018/88530941-bd7ef880-d01f-11ea-8413-2d5d5ada2844.png)

5. *Load the data using PigStorage(‘,’) instead of TextLoader(). Using FOREACH...GENERATE command define relation that is a projection of the first 10 fields of the visits       relation.Use LIMIT to display only 50 records.* 

![image](https://user-images.githubusercontent.com/63608018/88531069-ea331000-d01f-11ea-8556-b19601d2b1cb.png)

6. *Then DUMP the result.*

![image](https://user-images.githubusercontent.com/63608018/88531135-020a9400-d020-11ea-8ad2-c3efac797851.png)

7. *Using last seven fields ($19 to $25) of visits. Use LIMIT to only output 500 records.*

![image](https://user-images.githubusercontent.com/63608018/88528906-df2ab080-d01c-11ea-883b-5a45a53f64b9.png)

8. *Here Using FILTER to define a relation that only contains records of visits where field $19 matches POTUS. Limit the output to 500 records.*

![image](https://user-images.githubusercontent.com/63608018/88529720-05048500-d01e-11ea-8623-1b2325e32a63.png)

![image](https://user-images.githubusercontent.com/63608018/88529848-2ebdac00-d01e-11ea-8028-93b72e6b508c.png)

9. *Now FILTER the relation by visitors who met with the President.*

![image](https://user-images.githubusercontent.com/63608018/88529511-bce56280-d01d-11ea-9ab4-10b3c9701cd2.png)

10. *Define the potus relationship that contains the name and time of arrival of the visitor.*

![image](https://user-images.githubusercontent.com/63608018/88529392-93c4d200-d01d-11ea-81ff-cc1b56e6fcdd.png)

11. *Order the potus_details by last name using desc command.*

![image](https://user-images.githubusercontent.com/63608018/88529294-6a0bab00-d01d-11ea-9187-823c63f1f4f0.png)

12. *Store the records of potus_details_ordered into potus folder using a comma delimiter.*

![image](https://user-images.githubusercontent.com/63608018/88529194-46e0fb80-d01d-11ea-9c46-e4ef3ccc4751.png)

13. *View the contents of the potus folder.*

![image](https://user-images.githubusercontent.com/63608018/88529108-2618a600-d01d-11ea-95fa-fd5caf9d9ea4.png)

14. *View the contents of the output file using cat.*

![image](https://user-images.githubusercontent.com/63608018/88529040-100ae580-d01d-11ea-8125-4de0ab5a809c.png)

