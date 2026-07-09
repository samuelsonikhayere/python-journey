genes = ["BRCA1","TP53","EGFR","MYC","ALK","KRAS","PTEN","BRAF","HER2","CDH1"]
healthy   = [4.2, 6.1, 2.3, 1.8, 3.5, 2.9, 5.1, 1.2, 3.8, 4.9]
diseased  = [1.1, 2.0, 8.7, 9.2, 3.6, 7.8, 0.8, 6.5, 9.1, 1.2]

#len (diseased)
#genes_comb = dict(zip(genes, zip(healthy, diseased)))
#print (genes_comb)
regulation_status = []
up_count = 0
down_count = 0
unchanged_count = 0

for i,j,k in zip (genes, healthy, diseased):
  fold_change =k/j

  if fold_change > 2.0:
    regulation_status = "Upregulated"
    up_count += 1
  elif fold_change < 0.5:
    regulation_status = "Downregulated"
    down_count += 1
  else:
    regulation_status = "Unchanged"
    unchanged_count += 1
  print (i,j,k, f"{fold_change:.2f}", regulation_status)
  
print(f"\nUpregulated: {up_count}")
print(f"Downregulated: {down_count}")
print(f"Unchanged: {unchanged_count}")
