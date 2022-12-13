## Description of the Project

#Software Analysis
In this Project, we made 

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

•	get_entire_chromosome_info() - returns a new dataset which contains all the information of the chromosome (ex. we use the GRCh38 to extract information regarding the chromosome itself)

•	calculate_fraction_of_unassembled_seq() - calculates the unassembled seq inside the GRCh38 and  this is done through the ratio of supercontigs and the whole chromosome itself then returns the value of this ratio

•	get_selected_entries() - the function returns a new dataset from selected source like, ensemble, Havana, ensembl_havana; in fact we can see it as a list

•calculate_number_of_specific_entries_for_each_operation() - the function returns a dictionary to which contains all the number of specific entries that can be found in each operations (database)

•	get_gene_names() - it returns a list of gene names containing from ensemble, havana, and ensemble_havana 


***app.py***

