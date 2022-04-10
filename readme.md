
# JPath: A compiler for XPath to JSON





## 1. Introduction

JSON and XML are two commonly used data formats for NoSQL databases and have different advantages. 

To solve the data exchanging problem between JSON and XML, our group have developed a tool called Jpathwhich 
![image](https://user-images.githubusercontent.com/50799916/162623892-1f5b6e99-8d21-4605-ab55-f976baf5b034.png)

It takes XPath query as the input, then converts it into syntax that MongoDB can understand, and finally outputs equivalent JSON query results.


## 2. How to use it 

### Step 1

To start Jpath, open main.py and run the module.
![image](https://user-images.githubusercontent.com/50799916/162624412-b3361c44-5a50-4c35-a21e-c51d2d5e9a75.png)


### Step 2
In the python shell, enter the host and port of your MongoDB server. 
The default config is localhost/27017.
![image](https://user-images.githubusercontent.com/50799916/162624430-b9bbc5ba-c96a-4a56-b0b9-96211d69190d.png)

### Step 3

After connecting to MongoDB, you need to specify the database and collection you want to query.
If the data is invalid, the program will show the alert information.
![image](https://user-images.githubusercontent.com/50799916/162624461-a4bb265f-e8ab-472a-974a-97ee6528e8fb.png)

### Step 4

Now you can enter your Xpath Query.
![image](https://user-images.githubusercontent.com/50799916/162624185-829ae1f4-7a76-4d19-8e7b-5091b5789aa0.png)

## 3. Sample Data Format 

To understand which kind of json data is valid, you may have a look at our sample datasets: library.json and library.xml.  

The data needs to have only one root element. 
![image](https://user-images.githubusercontent.com/50799916/162624793-a6e402eb-d2fa-4d1b-9f64-97b10d1e00f5.png)

---
![image](https://user-images.githubusercontent.com/50799916/162624854-fb805589-0ccb-475e-a98c-8c83e057db11.png)


If there are sibling nodes which share the same tag name, they should be stored in a JSON array.




