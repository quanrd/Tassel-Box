# slin63@illinois.edu
import os
import datetime
import csv


class RemlFile(object):
    def __init__(self, name, trait_dict):
        self.name = name
        self.trait_dict = trait_dict

    def get_header(self):
        trait_headers = self.trait_dict.keys()
        return ['Trait'] + sorted(trait_headers)

    def combine(self, other):
        self.trait_dict.update(other.trait_dict)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name + ' - {}'.format(self.trait_dict)


def merge_duplicate_remls(remls):
    merged = []
    for i in remls:
        for j in remls:
            if i == j:
                i.combine(j)
                merged.append(i)
                del j

    return merged


def write_to_csv(remls):
    output_list = []
    header = []
    file_name = RESULTS_DIR + 'summary/Her_K_results:{}.csv'.format(datetime.datetime.now())
    with open(file_name, 'w') as csvfile:
        for reml in remls:
            if header:
                if reml.get_header()[-1] not in header:
                    header.append(reml.get_header()[-1])
            else:
                header = reml.get_header()

            output_dict = {'Trait': reml.name}
            for i in xrange(len(reml.trait_dict)):
                current_her = reml.trait_dict.keys()[i]
                output_dict[current_her] = reml.trait_dict[current_her]

            output_list.append(output_dict)
        writer = csv.DictWriter(csvfile, fieldnames=header)
        # http://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
        # Remove dup. values (this is disgusting):
        output_list = [i for n, i in enumerate(output_list) if i not in output_list[n + 1:]]

        writer.writeheader()
        [writer.writerow(row) for row in output_list]
        writer.writerow({'Trait': "Generated: {}".format(datetime.datetime.now())})

    return 0


def load_remls(bins):
    reml_list = []
    for bin in bins:
        with open(bin, "r") as remlfile:
            reml_list.append(
                RemlFile(
                    name=get_hypo_name(get_base_name(bin)), trait_dict=access_reml_member(remlfile, "Her_", get_base_name(strip_extensions(bin))
                )))

    return reml_list


def access_reml_member(rfile, member, name):
    reml_info = rfile.readlines()
    trait_dict = {}
    is_rest_file = False
    for value in reml_info:
        if member in value:
            if is_rest_file:
                name += "_rest"
            split_value = value.split(' ')
            trait_dict[name] = split_value[1]
            is_rest_file = True

    return trait_dict


def get_base_name(file_name):
    while file_name.find('/') != -1:
        slash_index = file_name.find('/')
        file_name = file_name[slash_index + 1:]
    return file_name


def strip_extensions(file_name):
    results = file_name.find('_results')
    return file_name[:results]


def get_hypo_name(file_name):
    hyp_start = file_name.find('results_')
    return file_name[hyp_start + 8:] # +8: Gets rid of _results from the string


if __name__ == '__main__':
    RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../results/'
    KINSHIP_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../kinship/'
    if 'summary' not in os.listdir(RESULTS_DIR):
        os.system('mkdir {}/summary'.format(RESULTS_DIR))
    bins = set([RESULTS_DIR + bin for bin in os.listdir(RESULTS_DIR) if ".reml" in bin])
    remls = merge_duplicate_remls(load_remls(bins))

    write_to_csv(remls)

    print "-" * 30
    print "Outputting {} remls to CSV \n~~~~~~~~~~>{}Done!".format(len(bins), os.popen("cd {} && pwd".format(RESULTS_DIR)).read())

