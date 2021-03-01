from numpy import genfromtxt

def read_ch4(file_name = "ch4_mm_gl.txt", verbose=False):
    '''
    # from https://www.esrl.noaa.gov/gmd/ccgg/trends/
    # CH4 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    #
    #  (-99.99 missing data;  -1 no data for #daily means in month)
    #
    #            decimal     average   interpolated    trend    #days
    #             date                             (season corr)
    '''

    data = genfromtxt(file_name, comments='#')

    dates = data[:,2]
    averages = data[:,3]
    if verbose:
        print (dates)
        print(averages)
    return [dates, averages]
