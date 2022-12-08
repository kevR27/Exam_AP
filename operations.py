import pandas as pd
import gzip


class DataSetReader():
    def __init__(self, path):
        self.path = path

    def getFile(self):
        with gzip.open(self.path, 'rt', newline='\n') as f:
            content = f.readlines()
        # c = 0
        L = []
        for v in content:
            # c += 1
            # if c == 10000:
            #     break
            if v[0] != '#':
                L.append(v.split('	'))

        df = pd.DataFrame(L)
        df.rename(
            columns={0: 'seqid', 1: 'source', 2: 'type', 3: 'start', 4: 'end', 5: 'score', 6: 'strand', 7: 'phase',
                     8: 'attribute'}, inplace=True)

        return df


class DataSet(DataSetReader):

    def __init__(self, path, inactive):
        super().__init__(path)
        self.__file = DataSetReader.getFile(self)  # dataframe
        self._inactive = inactive

    # decorator
    def _inactive(f):
        def wrapper(self, *args, **kwargs):
            if f.__name__ in self._inactive:
                return ('Operation is inactive')
            return f(self, *args, **kwargs)

        return wrapper

    # return file
    @_inactive
    def get_file(self):
        return self.__file

    # getting the some basic information about the dataset.
    @_inactive
    def get_basic_info(self):
        # all([type(data.get_file().seqid[i]) for i in range(len(data.get_file()))]) check that all rows have the same type
        col = self.__file.columns
        # pick first row
        typ = [type(self.__file.iloc[0][i]) for i in range(len(col))]
        return {i: j for i in col for j in typ}

    # obtaining the list of unique sequence IDs available in the dataset;
    @_inactive
    def get_unique_ids(self):
        return list(set(self.__file.seqid))

    # obtaining the list of unique type of operations available in the dataset;
    @_inactive
    def get_unique_types(self):
        return list(set(self.__file.type))

    # counting the number of features provided by the same source;
    @_inactive
    def get_number_of_features(self):
        # Q: what is number of features?
        typ = self.__file.source
        full_dict = dict(typ.value_counts())
        full_dict.pop('.')
        return full_dict

    # counting the number of entries for each type of operation;
    @_inactive
    def get_number_of_entries(self):
        typ = self.__file.type
        full_dict = dict(typ.value_counts())
        return full_dict

    # deriving a new dataset containing only the information about entire chromosomes. Entries with entire
    # chromosomes comes from source GRCh38;
    @_inactive
    def get_entire_chromosome_info(self):
        return self.__file[self.__file['source'] == 'GRCh38']

    # calculating the fraction of unassembled sequences from source GRCh38
    @_inactive
    def calculate_fraction_of_unassembled_seq(self):
        subset_df = self.get_entire_chromosome_info()
        return sum(self.__file.type == 'supercontig') / len(subset_df)

    # obtaining a new dataset containing only entries from source ensembl , havana and ensembl_havana
    @_inactive
    def get_selected_entries(self):
        df = self.__file
        return df[(df.source == 'havana') | (df.source == 'ensembl') | (df.source == 'ensembl_havana')]

    #  counting the number of entries for each type of operation for the dataset containing containing only
    # entries from source ensembl , havana and ensembl_havana
    @_inactive
    def calcuate_number_of_specific_entries_for_each_operation(self):
        typ = self.get_selected_entries().type
        return dict(typ.value_counts())

    # returning the gene names from the dataset containing containing only entries from source ensembl ,
    # havana and ensembl_havana.
    # slow due to iteration over the rows
    # Q: maybe gene name is something else? is not Name?
    @_inactive
    def get_gene_names(self):
        selected = self.get_selected_entries().attribute
        names = []
        for i in range(len(selected)):
            entry = selected.iloc[i]
            if 'Name' in entry:
                unwrapped = dict(map(lambda x: x.split('='), entry.split(';')))
                names.append(unwrapped['Name'])
            if len(names)==10000:
                break
        return names
