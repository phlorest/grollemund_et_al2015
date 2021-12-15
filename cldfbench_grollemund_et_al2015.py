import pathlib

import phlorest

def preprocess_nexus(s):
    for t in self.taxa:
        if t['taxon'] != t['Original_Name']:
            s = s.replace(t['Original_Name'], t['taxon'])
    return s


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "grollemund_et_al2015"

    def cmd_makecldf(self, args):
        self.init(args)

        args.writer.add_summary(
            self.raw_dir.read_tree('grollemund.mcct.trees', detranslate=True),
            self.metadata,
            args.log)
        posterior = self.sample(
            self.raw_dir.read('BP425_M1P_100_cv2_relaxed_YP_runs_1_2_4_5_thinned-fixed.trees.gz'),
            detranslate=True,
            n=100,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus(
                'Grollemund-et-al_Bantu-database_2015.nex',
                preprocessor=preprocess_nexus,
                encoding='latin1'),
            self.characters,
            args.log)
