DATE=$(date +'%m/%d/%Y')
ldak=~/tassel/Annotations/unified
project_dir=~/tassel/Annotations/unified/Tassel-Box
py_dir=$project_dir/pyscripts
pheno_dir=$project_dir/phenotypes
hyp_dir=$project_dir/hyps

# Make hypothesis files for LDAK
python $py_dir/make_hype.py

# ldak.4.9.fast
for c in $pheno_dir/*.txt
do
  for hyp in matrices/*.txt
      do
        FILENAME=$(basename "$c")
        HYPNAME=$(basename "$hyp")
        HYPNAME_CLEAN=${HYPNAME:0:${#HYPNAME}-4}
        # echo $HYPNAME \
        $ldak/ldak.4.9.fast --reml ./results/$HYPNAME_CLEAN\_results_$DATE_$FILENAME \
        --mgrm $hyp \
        --pheno $c --kinship-details NO
      done
done

# Combine outputs and compile CSV with her_K data
python $py_dir/merge_results.py
python $py_dir/her_csv.py
