for c in *.txt; do   /media/sf_Annotations/programs/ldak.4.9.fast --reml results/hyp1_results_2_Dec_$c --mgrm /media/sf_Annotations/workdir2/hyp_all_kinlist.txt --pheno $c --kinship-details NO; done
#for c in *.txt; do   /media/sf_Annotations/programs/ldak.4.9.fast --reml results/hyp2_results_30_Nov_$c --mgrm /media/sf_Annotations/workdir2/hyp_2_kinlist.txt --pheno $c --kinship-details NO; done
#for c in *.txt; do   /media/sf_Annotations/programs/ldak.4.9.fast --reml results/hyp3_results_30_Nov_$c --mgrm /media/sf_Annotations/workdir2/hyp_3_kinlist.txt --pheno $c --kinship-details NO; done
#for c in *.txt; do   /media/sf_Annotations/programs/ldak.4.9.fast --reml results/hyp4_results_30_Nov_$c --mgrm /media/sf_Annotations/workdir2/hyp_4_kinlist.txt --pheno $c --kinship-details NO; done
#for c in *.txt; do   /media/sf_Annotations/programs/ldak.4.9.fast --reml results/hyp5_results_30_Nov_$c --mgrm /media/sf_Annotations/workdir2/hyp_5_kinlist.txt --pheno $c --kinship-details NO; done
#cd results/
#cat *reml > combinedreml.txt