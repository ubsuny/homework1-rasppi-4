from numpy import genfromtxt

def read_ch4(file_name = "CH4.txt", verbose=False):
    '''
    # from https://www.esrl.noaa.gov/gmd/ccgg/trends/
    # CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    #
    #  (-99.99 missing data;  -1 no data for #daily means in month)
    #
    #            decimal     average   interpolated    trend    #days
    #             date                             (season corr)
    '''

    data = genfromtxt(file_name, comments='#')

    dates = data[:,2]
    averages = data[:,3]
    uncertainty = data[:,4]
    if verbose:
        print (dates)
        print(averages)
        print(uncertainty)
    return [dates, averages, uncertainty]