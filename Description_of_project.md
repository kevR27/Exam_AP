## Description of the Project

### Software Analysis
In this Project, we made 

***Registry.py*** 

is a python file connected to *operation.py* because it contains all the attributes and methods which are used for the *app.py* for the implementation of the User Interface, 
indeed it 
If you look onto the file you can only see a class called ***Registry***; its task is to return all the data present on the human genome annotation file (GFF3); it 
contains all the functions calling analytical operations defined in the *operations.py*


***operations.py***
It is a python file which is dependent on the use of two libraries: 
- *gzip* which is able to unzip our GFF3 File 
- *pandas* which is able to transformed our GFF3 File into dataframe which makes the dataset easily manipulated through the *Registry.py* 

The python file contains two classes namely:

**DataSetReader**:
- the class contain a method called getFile which is defined by our group which its aim is to unzip the file and transform our file into a dataframe which is much flexible.

**DataSet**:

it is a class that contains ten method which is defined by a decorator which allows us to modify the behavior of the functions inside this class; it allow us
to wrap another function in order to extend the behavior of wrapped function,
without permanently modifying it. then functions are taken as the argument into another function and then called inside the wrapper function; the function of decorator in our case is that it defines the activity of every method inside this class (active or inactive operations). in fact we can see this in line 37 -43


Here are the function that this class contain, to which results are obtained though the use of some functions of the *pandas* library:


•	get_basic_info() - in this function we get all the basic information like name, type source and etc of specific gene or sequence we, in the user interface this function is at play; it returns the information into a dictionary, on the program file, it is executed as a list comprehension, but as we have said it returns a dictionary as an output.

•	get_unique_ids() - in this function it returns all the sequence IDs which is found on the dataset into a list

•	 get_unique_types() - it is a function that returns a list which contains all the unique types (like exons, introns and etc) found on the dataset.

•	get_number_of_features() - is a function that returns a value of the total number of features contained in every source found on the dataset

•	get_number_of_entries() - returns a value of entities for each type of operations 

•	get_entire_chromosome_info() - returns a new dataset which contains all the information of the chromosome (ex. we use the GRCh38 to extract information regarding the chromosome itself)

•	calculate_fraction_of_unassembled_seq() - calculates the unassembled seq inside the GRCh38 and  this is done through the ratio of supercontigs and the whole chromosome itself then returns the value of this ratio

•	get_selected_entries() - the function returns a new dataset from selected source like, ensemble, Havana, ensembl_havana; in fact we can see it as a list

•calculate_number_of_specific_entries_for_each_operation() - the function returns a dictionary to which contains all the number of specific entries that can be found in each operations (database)

•	get_gene_names() - it returns a list of gene names containing from ensemble, havana, and ensemble_havana 


***app.py***
The .py file use libraries like Flask and modules like operations and Registry to function, this is possible thought the command import.
The  file is able to open the GFF3 file using all the functions we have on the operations.py file; we also defined in this page which operation results inactive when executed.
Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. 

It will create eleven pages, each pages contain a 'back' button which brings the user on the homepage:

- /:
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
- Text-decoration shorthand CSS properties: set the appearance of decorative lines on text (head part)
- Title
- Body - contains short description of the operations found in every page, in the hompage.html it is quite different because we have a list of all the active and inactive function while for the rest of the html file the user can see the output with its corresponding description
- Button - except for the homepage.html, all the html files have the button which is linked with the homepage, thus whenever the user wants to go back and perform other operations they can just click it and returns the user to the original page

### Efficiency of the program

The time execution of all the functions in our classes are low due to its reliability to pandas thus time complexity of the program itself is low except for the function get_gene_names() because gene names are stored inside the 'attribute' column which returns a very long description, hence data manipulation becomes very slow as we iterate the function in every rows of the dataset thus having a higher time complexity compare to other functions; to avoid this problem we set a display for the first 10000 rows of our dataset otherwise it will take time to obtain the result.

### CRC cards and UML description
CRC cards and UML diagram is used in this project to know how our class and methods should be 


