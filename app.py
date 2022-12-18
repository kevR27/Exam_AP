from flask import Flask, render_template
from operations import *
from Registry import *

webapp = Flask('my_webapp')

#here we provide list of inactive operations
data = DataSet(path = 'Homo_sapiens.GRCh38.85.gff3.gz', inactive = ['get_unique_types','get_file'])
reg = Registry(data)


@webapp.route('/')
def homepage():
    # names = reg.registry()
    # link_names = reg.links()
    return render_template('homepage.html')


@webapp.route('/GBI')
def gbi():
    info = reg.link_basic_info()
    return render_template('GBI.html', info=info)


@webapp.route('/USI')
def usi():
    info = reg.link_unique_id()
    return render_template('/USI.html', info=info)


@webapp.route('/UT')
def ut():
    info = reg.link_unique_types()
    return render_template('/UT.html', info=info)


@webapp.route('/NFS')
def nfs():
    info = reg.link_number_feature()
    return render_template('/NFS.html', info=info)


@webapp.route('/NE')
def ne():
    info = reg.link_number_entries()
    return render_template('/NE.html', info=info)


@webapp.route('/NewData')
def new_data():
    info = reg.link_entire_chromosome_info()
    return render_template('/NewData.html', info=info)


@webapp.route('/CalcUS')
def calc_us():
    info = reg.link_unassembled_seq()
    return render_template('/CalcUS.html', info=info)


@webapp.route('/NewDataother')
def new_data_other():
    info = reg.link_selected_entries()
    return render_template('/NewDataother.html', info=info)


@webapp.route('/CountON')
def count_on():
    info = reg.link_number_specific_entries()
    return render_template('/CountON.html', info=info)


@webapp.route('/Gene')
def gene():
    info = reg.link_gene_names()
    return render_template('/Gene.html', info=info)


webapp.run(debug=True)
