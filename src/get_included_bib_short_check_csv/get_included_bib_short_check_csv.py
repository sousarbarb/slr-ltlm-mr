
import os
import bibtexparser as bib



# Load bibtex database
def load_bibtex_db(bib_file_str):
  bib_parser = bib.bparser.BibTexParser()
  bib_parser.common_strings           = False
  bib_parser.ignore_nonstandard_types = False
  bib_parser.homogenize_fields        = False

  return bib.load(open(bib_file_str, encoding="utf8"), parser=bib_parser)


bib_all_db = load_bibtex_db("../../data/results/bibtex/included_all_short_check.bib")



# Init CSV file
bib_all_db_csv = "type;id;title;author;year;doi;url;venue\n"



# Short the references for only the intended entries for each reference
for entry in bib_all_db.entries:
  if entry['ENTRYTYPE'] == "article":
    bib_all_db_csv += "journal;"
  else:
    bib_all_db_csv += "conference;"

  bib_all_db_csv += entry['ID'] + ";"
  bib_all_db_csv += entry['title'] + ";"
  bib_all_db_csv += entry['author'] + ";"
  bib_all_db_csv += entry['year'] + ";"

  if 'doi' in entry:
    bib_all_db_csv += entry['doi'] + ";"
  else:
    bib_all_db_csv += ";"

  if 'url' in entry:
    bib_all_db_csv += entry['url'] + ";"
  else:
    bib_all_db_csv += ";"

  if 'journal' in entry:
    bib_all_db_csv += entry['journal'] + "\n"
  elif 'booktitle' in entry:
    bib_all_db_csv += entry['booktitle'] + "\n"
  else:
    bib_all_db_csv += "\n"



# Save database analysis overview results
with open("../../data/results/bibtex/included_all_short_check.csv","w",encoding="utf8") as report_file:
  report_file.write(bib_all_db_csv)
