
import os
import pandas as pd
import bibtexparser as bib



# Check if record from excel file exists in the bibtex database
def check_if_record_exists_in_bib_db(db,xlsx,row):
  for entry in db.entries:
    # - title
    if entry['title'] == str(xlsx.title[row]):
      return entry
    # - doi
    if 'doi' in entry:
      if entry['doi'] == str(xlsx.doi[row]):
        return entry

  return None

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

bib_inspec_db = load_bibtex_db(bib_directory + "inspec_proc.bib")
bib_scopus_db = load_bibtex_db(bib_directory + "scopus_proc.bib")
bib_wos_db    = load_bibtex_db(bib_directory + "wos_proc.bib")

# Init export database
bib_db = bib.bibdatabase.BibDatabase()

# Customization of the default writer
bibtex_writer = bib.bwriter.BibTexWriter()
bibtex_writer.add_trailing_comma = True
bibtex_writer.contents      = ['entries']
bibtex_writer.display_order = [
    'author','journal','booktitle','title', 'volume','number','pages','doi',
    'note','ISBN','ISSN','publisher','address','year','month']
bibtex_writer.indent           = '  '
bibtex_writer.order_entries_by = ('author','year','ID')



# Check from which databases appear the included records in the reviews
print("Total entries: " + str(len(results_xlsx.title)))
output = "missing references report\ntitle;year;doi\n"

for i in range(len(results_xlsx.title)):
  entry = check_if_record_exists_in_bib_db(bib_scopus_db,results_xlsx,i)
  if entry is not None:
    bib_db.entries.append(entry)
    continue

  entry = check_if_record_exists_in_bib_db(bib_inspec_db,results_xlsx,i)
  if entry is not None:
    bib_db.entries.append(entry)
    continue

  entry = check_if_record_exists_in_bib_db(bib_wos_db,results_xlsx,i)
  if entry is not None:
    bib_db.entries.append(entry)
    continue

  output += str(results_xlsx.title[i]) + ";" + str(results_xlsx.year[i]) + ";" + str(results_xlsx.doi[i])



# Save database analysis overview results
with open("../../data/results/included_all.bib","w",encoding="utf8") as bibtex_file:
  bib.dump(bib_db,bibtex_file,writer=bibtex_writer)

with open(os.path.splitext(results_str)[0]+"_get-bib_report.txt","w",encoding="utf8") as report_file:
  report_file.write(output)
