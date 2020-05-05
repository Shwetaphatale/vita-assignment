**Day 4**
*Direct communication between two services is possible using either* 

* *Inside AWS*, or 
* *Outside AWS*

**Inside AWS**
*Using Inside AWS we can communicate two services. In this we use IAM Roles.*
*IAM stands for identity access management. Here we set some policies to access services.*


**How to attach IAM Roles to EC2**:
**Steps:**
1.  -*On AWS console select services and find Role*
2.  -*In creat role select service as EC2 and click on next permission*
3.  -*Search S3 in permission policies and select* **AmazonS3FullAccess**	
4.  -*Click on dropdown and select JSON*
5.  -*Click on next tag*
6.  -*Click on next review and give role name whichever we want*
7.  -*And finally click on creat*


**How to attach EC2 with IAM**
1.  -*In services select EC2*
2.  -*Select the instance*
3.  -*Select actions and go to instance settings*
5.  -*Select Attach/ Replace IAM*
6.  -*From drop down select the IAM which we created*
7.  -*Click on apply and then close*  