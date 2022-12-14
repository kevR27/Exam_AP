# Advanced Programming Project 2022-2023

###

## Specification
The project contains three ***.py*** file to which each contains certain functions, necessary for the project to work:

1. ***operations.py*** is a program in which contains libraries like **pandas** (responsible for interpreting our dataset and trensforming it into a generic tabular data) and **gzip** (responsible for unzipping the zipped GFF3 file) which are responsible on reading the GFF3 File and transforming it into a readable dataset for the user. This program also contains a class named ***DataSetReader*** which contains the function *getFile* which is used to open and interpret our dataset (GFF3 File)consists a class **DataSet** and its asscociated method which are the operations. operations can only be executed whenever they are active; these attributes are used for:
     * returns our datsaet about the Human genome data
     * returns basic information of the human genome like name, source, sequence id, type; so information about the human genome which can be obtained by the user
     * returns all unique sequence ids found in the dataset; these sequence ID is different in every sequences and regions of the Human Genome
     * returns a value of the total value of features we can find in the dataset, Hence, every features we can see in different sources that provided the DNA sequences and Annotation of the Human Genome
     * returns a value of all the entries for each type of operation which can be found in every sources (databases)
     * returns a new dataset of the chromosome information from the GRCh38 source from ur old dataset
     * calculates the unassembled sequences which is present  on the dataset (it is done through getting the ratio between the supercontigs which are said to have gaps on the genome sequences and the whole human genome)
     * gets separate new dataset for the other sources we have (ensembl, havana, ensembl_havana)
     * gets the gene name which is seen on the said remaining sources and they are usually seen on the attribute column
     
2. ***Registry.py*** is a program which is able to print given function which is asked by the user; the file is linked with the *app.py*; this file is necessary for the implement web-based user interface

3. ***app.py*** consists in a program whichis able to open our dataset and it implements the Web-based user interface (UI). in order for it to function it needs the python modules and libraries like Flask, operations, and Registry


## CRC Cards
We provided a folder which contain the Class Responsibility Collaboration Cards (CRC Cards) which are used by the authors to brainstorm and devise the design of our Object Oriented Software, which can be seen in each class of the ***.py*** File; The said cards are created using an application called **Visual Paradigm**

## UML Diagrams
We have provided a folder with an UML diagram explaining the connections between the classes built which is important for the design of our program:
- "classdiagram.png" is an image representing the UML diagram created with **Visual Paradigm**.
- "Class Diagram.vpp" is the equivalent of .png of the UML diagram of all the classes but in _.vpp_ format.

## Templates
It is a folder which contains templates that are used to implement the file ***app.py*** to create an HTML web page. (User Interface)

## Static
It is a folder that contains accessory used on the implementation of the HTML web page (User Interface)

## Data
You can see it uploaded in the repository; otherwise it can be downloaded through this link ***https://www.dropbox.com/s/11yzbl0dpyanvyi/Homo_sapiens.GRCh38.85.gff3.gz?dl=0***

This data is the human genome sequence and annotation which is in a General Feature Format (GFF3) File Format, this format is the common format used for analyzing Genomic data

***https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md*** 

this link gives a thorough explanation of the contents of the GFF3 File

## Libraries
Several libraries have been used:
```python
import pandas as pd
import gzip 
from flask import Flask, render_template, request
```
## How can you run the Program?
To run the program, make sure to have them installed the following Libraries. 
- Installing *[Flask](https://phoenixnap.com/kb/install-flask)*
- Installing *[pandas](https://pandas.pydata.org/docs/getting_started/install.html)*
- Installing *[gzip](https://docs.python.org/3/library/gzip.html)*

Installation usually is done using the **pip install** command

To run the program, using terminal or powershell, you first need to run first ***operation.py***, then run ***Registry.py***, then finally we run the ***app.py*** which will then give you a link in which contains all the functions of our program

## HTML page
Once we executed all of the ***.py*** files especially when we run the *app.py*, a link will be provided in the terminal which can be used to access the Homepage of the web interface.
***http://127.0.0.1:5000***

## Authors
*Coviello Lilliana*, *Knyazhitskiy Dmitriy*, *Mohebbi Pegah*, *Ramos Kevin Karl* 

