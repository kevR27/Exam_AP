 # Description of the Project

To create our project, we conceptualized different ideas through the use of the CRC cards, which is important for software analysis given a problem which is how can we interpet Human Genome Annotation file (GFF3 File) into a simple dataframe that any user can easily understand. Afterwards we use UML Diagram to realize these concept of class, and transform them into solutions that is able to solve our problem

Here, we provided some additional information regarding every python file created using the classes we created during the conceptualization:

***Registry.py*** 
is a python file connected to *operation.py* because it contains all the attributes and methods used for the *app.py* for the implementation of the User Interface, indeed looking onto this file you can see a unique class called ***Registry***; its task is to return data present on the human genome annotation file (GFF3); it contains all the functions calling analytical operations defined in the *operations.py*, which allow to manipulate the dataframes obtained thanks to Pandas.

***operations.py***
It is a python file which is dependent on the use of two libraries: 
- *gzip* which is able to unzip our GFF3 File 
- *pandas* which is able to transform our GFF3 File into a dataframe which makes the dataset easily manipulable


The python file contains two classes, namely:
**DataSetReader**:
- this class contains a method called getFile, which has been defined by our group, whose aim is to unzip the file and convert it into another format 

**DataSet**:
it is a class that contains ten methods, whose behaviour is modifified by a decorator: this is also called wrapper function and it allows to change the output, without directly modifying the code. We can do this by passing a function inside another function as the argument and then making a function call inside a wrapper function. The function of decorator in our case is to define the activity of every method inside this class (active or inactive operations). That's what happens in line 37 -43


Here there's a list of the functions contained in the dataset class, which will provide the results based on the dataframe obtained using Pandas library

•	get_basic_info() - in this function we get all the basic information characterizing GFF3, that is enclosed in nine columns, each providing different data. It returns information into a dictionary, on the program file, but it is executed as a list comprehension.

•	get_unique_ids() - in this function it returns all the sequence IDs which is found on the dataset into a list, this alphanumeric string allows to distinguish anambigously each different feature.

•	 get_unique_types() - it is a function that returns a list which contains all the unique types, which correspond to the different segments found an DNA strand (like exons, introns and etc) present in GFF3.

•	get_number_of_features() - is a function that returns a value of the total number of features contained in every source found in the dataframe 

•	get_number_of_entries() - returns a value of each type of operation, which represents the number that a given segment appears in the dataframe 

•	get_entire_chromosome_info() - returns a new dataset which contains information on the entire chromosome; this is possible considering only a precise source, that is GRCh38

•	calculate_fraction_of_unassembled_seq() - calculates the unassembled seq inside the GRCh38 and  this is done through the ratio of supercontigs and the whole chromosome itself then returns the value of this ratio

•	get_selected_entries() - the function returns a new dataframe from selected source ensembl, Havana, ensembl_havana; we can see it as a list 

•calculate_number_of_specific_entries_for_each_operation() - the function returns a dictionary which contains the exact number that each type operator appears in the dataframe (example: 'exon:1180596')

•	get_gene_names() - it returns a list of gene names contained in selected sources, which are ensembl, havana, and ensembl_havana 


***app.py***
The .py file use libraries like Flask and modules like operations and Registry to function, this is possible thought the command import.
The  file is able to open the GFF3 file using all the functions we have on the operations.py file; we also defined in this page which operation results inactive when executed.
Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. 

It will create eleven pages, each pages contain a 'back' button which brings the user on the homepage:

-  /:
the page shows the homepage of our web interface to which it gives the user a short description of the project and also shows a list of the possible active and inactive operations that is implemented on the web page; through this the user can choose any operations that are listed on the page.

- /GBI:
the page shows us the execution of the first operation which is the get_basic_info(), that returns the column of the metadata

- /USI: 
the page shows us the execution of the second operation which is the get_unique_ids() that returns all the unique sequence id founf in human genome

- /UT:
the page shows us the execution of the third operation which is the get_unique_types(). however we have set this operation inactive, thus it returns into a message "operation is inactive" instead of all the unique types inside the dataframe

- /NFS:
the page shows us the execution of the fourth operation which is the get_number_of_features() that returns value of the features found in the GFF3 File

- /NE:
the page shows us the execution of the fifth operation which is the get_number_of_entries() that returns value of all entries of each type found in the GFF3 File

- /NewData:
the page shows us the execution of the sixth operation which is the get_entire_chromosome_info() that returns all the dataset of the source GRCh38

- /CalcUS:
the page shows us the result of the execution of the seventh operations which is the calculate_fraction_of_unassembled_seq(), that returns as a value of the unassembled region of the human genome

- /NewDataother:
the page shows us the execution of the eighth operation which is the get_selected_entries() that returns all the dataset of the sources ensembl, havana, ensembl_havana

- /CountON:
the page shows us the execution of the ninth operation which is the calculate_number_of_specific_entries_for_each_operation()that returns all the values of types found in each entries of the other sources

- /Gene:
the page shows us the execution of the tenth operation which is the get_gene_names(), that returns all the gene names found on the three sources

In order for the file to work properly we use a functions from Flask which are **render_template** which is able to generate the template we have provided thus HTML and this allows us on implementing our web application using python; and **request** which is a function that allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data, so in our case, our object is "info" which is able to return a response base form the operations we did (found on both the Registry.py and operations.py)
 

### Templates

The folder contains eleven HTML files that displays the output that was cretaed through the class and its operations;every HTML files contain:
- **Text-decoration shorthand CSS properties**: set the appearance of decorative lines on text (head part)
- **Title**
- **Body** - contains short description of the operations found in every page, in the hompage.html it is quite different because we have a list of all the active and inactive function while for the rest of the html file the user can see the output with its corresponding description
- **Button** - except for the homepage.html, all the html files have the button which is linked with the homepage, thus whenever the user wants to go back and perform other operations they can just click it and return to original page

### Efficiency of the program

The time execution of all the functions in our classes are low due to its reliability to pandas thus time complexity of the program itself is low except for the function get_gene_names() because gene names are stored inside the 'attribute' column which returns a long description, hence data manipulation becomes slow as we iterate the function in every row of the dataset in order to select a relevant part of the substring thus having a higher time complexity compare to other functions. Moreover, displaying around 1 million items is slow and useful. Hence, to avoid this problem we set a display for the first 10000 rows of our dataset.

### CRC cards and UML description
CRC cards are useful during software analysis because it let us conceptualize our ideas and organize our class in a detailed manner before starting the project. In such way we describe the role of each class (seen on the crc cards) and the corresponding attributes that the class contain; hence base from the project sepcifiaction we created the classes with their respected attributes; If you look at the CRC cards, each one of them contain some description and on how they work in our program given their attributes.

We use the UML diagram to design our software, and this diagram is made using the CRC cards that we created earlier. UML diagram is the realization of our problems, hence we can consider it as our solution. The UML Diagram describes how each class' relationship between them.
In our UML diagram we put the connection of each class and how these classes influence each other; if you check our diagram, 
class *DataSetReader* which has attributes like the path and data, it is dependent to the python libraries gzip and pandas because without these libraries the class (the program itself) cannot open the GFF3 itself because it is in zipped form and the human genome file cannot be manipulated and interpreted. After that, we have class *DataSet* which has data as an attribute, this class is able to manipulate the data into dataframes with the use of pandas; as we can see on the diagram we can say that *DataSet* class is a generalization of the class *DataSetReader* because we have used its method to obtain our dataframe which is important for the operations to return the dataframe properly. We can also say that the two classes are associated because class *DataSet* also relies from pandas to create the dataframe.
Finally we have class *Registry* which is able to link all the operations we have defined inside the class *DataSet*, in fact we can say that class *Registry* is associated to class *DataSet* because as we know the role of this class is to return all the obtined result of our defined functions inside the class *DataSet* in our web interface. 

