# slin63@illinois.edu
# Not in use
import datetime
import os


def get_base_name(file_name):
    while file_name.find('/') != -1:
        slash_index = file_name.find('/')
        file_name = file_name[slash_index + 1:]
    return file_name


def read_bins_to_string(bins):
    bin_list = []
    debug = 0

    for bin in bins:
        if debug > 1:
            break
        else:
            with open(bin, "r") as remlfile:
                lines = remlfile.readlines()
                print lines
                bin_dict = {}
                for line in lines:
                    line_s = line.split(' ')
                    bin_dict[line_s[0]] = line_s[1:]
                    print line_s

                    debug +=1

                print bin_dict

    return 0


def output_cat(bin_str):
    file_name = RESULTS_DIR + 'summary/LDAK_results:{}.txt'.format(datetime.datetime.now())
    with open(file_name, "w") as outfile:
        outfile.write(bin_str)

if __name__ == '__main__':
    RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../phenotypes/results/'
    if 'summary' not in os.listdir(RESULTS_DIR):
        os.system('mkdir {}/summary'.format(RESULTS_DIR))
    bins = set([RESULTS_DIR + bin for bin in os.listdir(RESULTS_DIR) if ".reml" in bin])

    print read_bins_to_string(bins)
