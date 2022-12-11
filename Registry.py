class Registry:  # take a Dataset object, kind of a wrapper around it, can go without this class
    # because why not
    __operations = [
        "Get Basic information of each column",
        "Obtain a list of unique sequence IDs",
        "Obtain a list of unique type",
        "Count the number of features of the same source",
        "Count the number of entries for each type of operations",
        "Obtain new dataset containing information of entire Chromosome",
        "Calculating unassembled sequences from the GRCh38",
        "New dataset from other source",
        "counting the number of entries for each type of operation for the dataset containing from source",
        "returning the gene names from the dataset "]

    __links = ["GBI", "USI", "UT", "NFS", "NE", "NewData", "CalcUS", "NewDataother", "CountON", "Gene"]

    def __init__(self, data):
        self.__data = data  # object of Dataset type

    def registry(self):
        return self.__operations

    def links(self):
        return self.__links

    def link_DataSet(self):
        return self.__data.get_file()

    def link_basic_info(self):
        return self.__data.get_basic_info()

    def link_unique_id(self):
        return self.__data.get_unique_ids()

    def link_unique_types(self):
        return self.__data.get_unique_types()

    def link_number_feature(self):
        return self.__data.get_number_of_features()

    def link_number_entries(self):
        return self.__data.get_number_of_entries()

    def link_entire_chromosome_info(self):
        return self.__data.get_entire_chromosome_info()

    def link_unassembled_seq(self):
        return self.__data.calculate_fraction_of_unassembled_seq()

    def link_selected_entries(self):
        return self.__data.get_selected_entries()

    def link_number_specific_entries(self):
        return self.__data.calcuate_number_of_specific_entries_for_each_operation()

    def link_gene_names(self):
        return self.__data.get_gene_names()
