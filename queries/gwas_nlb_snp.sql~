SELECT 
  DISTINCT gwas_hits.chr_number as chr, position
FROM
  gwas_hits, -- Has chr and position
  feature
WHERE
  gwas_hits.position >= lower(feature.feature_range) - 5000 AND
  gwas_hits.position < upper(feature.feature_range) + 5000 AND
  gwas_hits.trait_name = 'Days to anthesis' AND
  gwas_hits.variant_type = 'SNP'
ORDER BY
  chr, position
;
