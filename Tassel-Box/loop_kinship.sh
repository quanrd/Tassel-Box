# Work flow: SQL queries -> Position lists -> Kinship matrices (???) -> Hypothese Generation -> LDAK Analysis ->

genotype_lib=namrils_projected_hmp31_MAF02mnCnt2500.hmp.txt.gz.lix
conn_config=genomeAnnosConnectionConfig.txt

for query in ./queries/*.sql
do
    q=$(basename "$query")
    /home/slin63/tassel/tassel-5-standalone/run_pipeline.pl -Xmx55g \
    -GenomeAnnosDBQueryToPositionListPlugin \
    -cf genomeAnnosConnectionConfig.txt \
    -qf $query -endPlugin -export pos_lists/${q%.*}_PositionList.json.gz
done

for pos_list in ./pos_lists/*.json.gz
do
    p=$(basename "$pos_list")
    /home/slin63/tassel/tassel-5-standalone/run_pipeline.pl -Xmx55g \
    -importGuess $genotype_lib \
    -FilterSiteBuilderPlugin \
    -positionList $pos_list \
    -endPlugin -KinshipPlugin -method Scaled_IBS -endPlugin \
    -export matrices/${p%%.*} \
    -exportType SqrMatrixBin
done

