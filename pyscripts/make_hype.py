# slin63@illiois.edu
# Cases: Multiple kinship files, accompanied by a single _rest file
# hyp$ need files \n _rest
# hyp file names should just be based on the kinship prefix
import os


def strip_extensions(file_name):
    dot_index = file_name.find('.')
    return file_name[:dot_index]


def populate_hype_list(bins):
    count = 1
    hype_list = []
    for bin in bins:
        name = "{}_matrix.txt".format(bin)
        dirs = MATRIX_DIR + bin
        hype_list.append(HypeFile(name=name, dirs=dirs))
        count += 1

    return hype_list


def output_hype_file(hype_list):
    print "Generating hype-lists:"
    for hyp in hype_list:
        print "~~~~~~~~~~>{}".format(hyp.name)
        text = open(hyp.name, "w")
        text.write(hyp.dirs + '\n{}'.format(REST_FILE))
        text.close()
    print "Done!"


class HypeFile(object):
    def __init__(self, name, dirs):
        self.name = KINSHIP_DIR + name
        self.dirs = dirs

    def __repr__(self):
        return self.name + ' ' + self.dirs


if __name__ == '__main__':
    KINSHIP_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../matrices/' # Reads from here
    MATRIX_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../matrices/' # Outputs to here
    REST_FILE = ''
    try:
        REST_FILE = KINSHIP_DIR + list(set([strip_extensions(bin) for bin in os.listdir(KINSHIP_DIR) if "_rest" in bin]))[0] + ".json.gzs"
    except IndexError:
        pass
    bins = set([strip_extensions(bin) for bin in os.listdir(KINSHIP_DIR) if "_PositionList" in bin and "_matrix" not in bin])

    hype_list = populate_hype_list(bins)

    output_hype_file(hype_list)
