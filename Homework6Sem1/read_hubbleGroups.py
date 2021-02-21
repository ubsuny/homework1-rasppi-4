from numpy import genfromtxt

def read_hubbleGroups(file_name = "HubbleGroups.txt", verbose=False):
    '''
    # from https://www.esrl.noaa.gov/gmd/ccgg/trends/
    # CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    #
    #  (-99.99 missing data;  -1 no data for #daily means in month)
    #
    #            decimal     average   interpolated    trend    #days
    #             date                             (season corr)
    '''

    data = genfromtxt(file_name, delimiter=",")

    distance = data[:,0]
    velocity = data[:,1]
    if verbose:
        print (dates)
        print(averages)
    return [distance, velocity]