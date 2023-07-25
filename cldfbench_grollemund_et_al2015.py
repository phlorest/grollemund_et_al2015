import pathlib

import phlorest


def fix_nexus(nex_string):
    # Remove asterisks in some names (nexus has them, trees don't)
    fix = [
        'D20B_Vamba_1919',
        'D304_Homa_1919',
        'D305_Nyanga-li',
        'D308_Bodo2',
        'D308_Ebodo',
    ]
    for f in fix:
        nex_string = nex_string.replace("*%s" % f, f)
    # MATRIX command doesn't end with ";":
    nex_string = nex_string.replace('end;', ';\nend;')
    # DATATYPE=binary is not in the NEXUS spec.
    nex_string = nex_string.replace('datatype=binary', 'datatype=standard')
    return '\n'.join(line for line in nex_string.split('\n') if not line.startswith('# ')).strip()


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "grollemund_et_al2015"

    def cmd_makecldf(self, args):
        self.init(args)

        args.writer.add_summary(
            self.raw_dir.read_tree('grollemund.mcct.trees', detranslate=True),
            self.metadata,
            args.log)

        # note only 100 tree, burn-in pre-removed so just take what we have.
        posterior = self.raw_dir.read_trees(
            'BP425_M1P_100_cv2_relaxed_YP_runs_1_2_4_5_thinned-fixed.trees.gz',
            detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)
        
        nex = self.raw_dir.read_nexus(
            'Grollemund-et-al_Bantu-database_2015.nex',
            preprocessor=fix_nexus,
            encoding='latin1')
        args.writer.add_data(nex, self.characters, args.log)
