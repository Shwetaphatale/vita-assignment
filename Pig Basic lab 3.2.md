**Basic Lab 3.2**

1. *On grunt shell use TextLoader to load the visits.txt file.*

2. *Define a new relation B that is a group of all the records in A.*

3. *Using DESCRIBE command view schema B.*

4. *Using the COUNT function determine how many lines of text are in visits.txt.*

5. *Use DUMP A view the result.*

6. *Load the data using PigStorage(‘,’) instead of TextLoader(). Using FOREACH...GENERATE command define relation that is a projection of the first    10 fields of the visits relation.Use LIMIT to display only 50 records.* 

7. *Then DUMP the result.*

8. *Using last seven fields ($19 to $25) of visits. Use LIMIT to only output 500 records.*

9. *Here Using FILTER to define a relation that only contains records of visits where field $19 matches POTUS. Limit the output to 500 records.*

10. *Now FILTER the relation by visitors who met with the President.*

11. *Define the potus relationship that contains the name and time of arrival of the visitor.*

12. *Order the potus_details by last name using desc command.*

13. *Store the records of potus_details_ordered into potus folder using a comma delimiter.*

14. *View the contents of the potus folder.*

15. *View the contents of the output file using cat.*

