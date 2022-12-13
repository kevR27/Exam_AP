## Description of the Project

#Software Analysis
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

