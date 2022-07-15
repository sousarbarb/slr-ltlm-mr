import os
import pandas as pd
import bibtexparser as bib



# Check if record from excel file exists in the bibtex database
def check_if_record_exists_in_bib_db(db,xlsx,row):
  for entry in db.entries:
    # - title
    if entry['title'] == str(xlsx.title[row]):
      return True
    # - doi
    if 'doi' in entry:
      if entry['doi'] == str(xlsx.doi[row]):
        return True

  return False

# Load bibtex database
def load_bibtex_db(bib_file_str):
  bib_parser = bib.bparser.BibTexParser()
  bib_parser.common_strings           = False
  bib_parser.ignore_nonstandard_types = False
  bib_parser.homogenize_fields        = False

  return bib.load(open(bib_file_str, encoding="utf8"), parser=bib_parser)



# Load excel file with the records included in the review
results_str   = "../../data/results/analysis.xlsx"
results_sheet = "included"

results_xlsx = pd.read_excel(results_str,sheet_name=results_sheet,header=0,dtype=str)

print(results_xlsx)

# Load bibtex from each database
bib_directory  = "../../data/methodology/identification/"

bib_acm_db    = load_bibtex_db(bib_directory + "acm_proc.bib")
bib_dim_db    = load_bibtex_db(bib_directory + "dimensions_proc.bib")
bib_ieee_db   = [ load_bibtex_db(bib_directory + "ieee_abstract_proc.bib") ,
                  load_bibtex_db(bib_directory + "ieee_author-kw_proc.bib") ,
                  load_bibtex_db(bib_directory + "ieee_index-terms_proc.bib") ,
                  load_bibtex_db(bib_directory + "ieee_inspec-ctrl_proc.bib") ,
                  load_bibtex_db(bib_directory + "ieee_inspec-non-ctrl_proc.bib") ,
                  load_bibtex_db(bib_directory + "ieee_title_proc.bib") ]
bib_inspec_db = load_bibtex_db(bib_directory + "inspec_proc.bib")
bib_scopus_db = load_bibtex_db(bib_directory + "scopus_proc.bib")
bib_wos_db    = load_bibtex_db(bib_directory + "wos_proc.bib")



# Check from which databases appear the included records in the reviews
print("Total entries: " + str(len(results_xlsx.title)))
output = "title;year;doi;acm;dim;ieee;inspec;scopus;wos\n"

for i in range(len(results_xlsx.title)):
  output += str(results_xlsx.title[i]) + ";" + str(results_xlsx.year[i]) + ";" + str(results_xlsx.doi[i]) + ";"

  if check_if_record_exists_in_bib_db(bib_acm_db,results_xlsx,i):
    output += "1"
  else:
    output += "0"
  output += ";"

  if check_if_record_exists_in_bib_db(bib_dim_db,results_xlsx,i):
    output += "1"
  else:
    output += "0"
  output += ";"

  check_ieee = False
  for j in range(6):
    if check_if_record_exists_in_bib_db(bib_ieee_db[j],results_xlsx,i):
      output += "1"
      check_ieee = True
      break
  if not check_ieee:
    output += "0"
  output += ";"

  if check_if_record_exists_in_bib_db(bib_inspec_db,results_xlsx,i):
    output += "1"
  else:
    output += "0"
  output += ";"

  if check_if_record_exists_in_bib_db(bib_scopus_db,results_xlsx,i):
    output += "1"
  else:
    output += "0"
  output += ";"

  if check_if_record_exists_in_bib_db(bib_wos_db,results_xlsx,i):
    output += "1"
  else:
    output += "0"
  output += "\n"



# Save database analysis overview results
with open(os.path.splitext(results_str)[0]+"_db.txt","w",encoding="utf8") as report_file:
  report_file.write(output)