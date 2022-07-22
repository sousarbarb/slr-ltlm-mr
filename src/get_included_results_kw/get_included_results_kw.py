import os
import re
import bibtexparser as bib



# Load bibtex database
def load_bibtex_db(bib_file_str):
  bib_parser = bib.bparser.BibTexParser()
  bib_parser.common_strings           = False
  bib_parser.ignore_nonstandard_types = False
  bib_parser.homogenize_fields        = False

  return bib.load(open(bib_file_str, encoding="utf8"), parser=bib_parser)

# Add if unique
list_kw = []
list_unique_kw = []

def add_if_unique(kw2add):
  add = True

  for kw in list_kw:
    if kw == kw2add:
      add = False
      break

  if add:
    list_kw.append(kw2add)

def extend_add_if_unique(list_kw2add):
  for kw in list_kw2add:
    add_if_unique(kw)

def unique_add_if_unique(kw2add):
  add = True

  for kw in list_unique_kw:
    if kw == kw2add:
      add = False
      break

  if add:
    list_unique_kw.append(kw2add)


def unique_extend_add_if_unique(list_kw2add):
  for kw in list_kw2add:
    unique_add_if_unique(kw)




bib_all_db = load_bibtex_db("../../data/results/bibtex/included_all.bib")



# Init export database
bib_all_kw_db = bib.bibdatabase.BibDatabase()

# Customization of the default writer
bibtex_writer = bib.bwriter.BibTexWriter()
bibtex_writer.add_trailing_comma = True
bibtex_writer.contents      = ['entries']
bibtex_writer.display_order = [
    'author','journal','booktitle','title', 'volume','number','pages','doi',
    'note','ISBN','ISSN','publisher','address','year','month']
bibtex_writer.indent           = '  '
bibtex_writer.order_entries_by = ('author','year','ID')



# Init CSV file
bib_all_kw_csv = "title;year;doi;url;kw1;kw2;kw3;kw4;kw5;kw6;kw7;kw8;kw9;kw10;kw11;kw12;kw13;kw14;kw15;kw16;kw17;kw18;kw19;kw20;kw21;kw22;kw23;kw24;kw25;kw26;kw27;kw28;kw29;kw30;kw31;kw32;kw33;kw34;kw35;kw36;kw37;kw38;kw39;kw40;kw41;kw42;kw43;kw44;kw45;kw46;kw47;kw48;kw49;kw50\n"



# Check keywords from the original entries
for entry in bib_all_db.entries:
  mod_entry = entry
  kw = []
  list_kw.clear()

  # - get all available keywords: keywords
  if 'author_keywords' in entry:
    list_aux = re.split(r"[,;]\s*",entry['author_keywords'].replace('\n',' ').lower())
    extend_add_if_unique(list_aux)
    

  # - get all available keywords: author
  if 'keywords' in entry:
    list_aux = re.split(r"[,;]\s*",entry['keywords'].replace('\n',' ').lower())
    extend_add_if_unique(list_aux)

  # - get all available keywords: wos
  if 'keywords-plus' in entry:
    list_aux = re.split(r"[,;]\s*",entry['keywords-plus'].replace('\n',' ').lower())
    extend_add_if_unique(list_aux)

  # - update keywords
  mod_entry['keywords'] = "; ".join(list_kw)

  # - add entry to CSV
  bib_all_kw_csv += entry['title'].replace('\n',' ') + ";"
  bib_all_kw_csv += entry['year'] + ";"
  if 'doi' in entry:
    bib_all_kw_csv += entry['doi'].replace('\n','') + ";;"
  else:
    bib_all_kw_csv += ";"
    if 'url' in entry:
      bib_all_kw_csv += entry['url'].replace('\n','') + ";"
    else:
      bib_all_kw_csv += ";"
  bib_all_kw_csv += mod_entry['keywords'] + "\n"

  bib_all_kw_db.entries.append(mod_entry)
  unique_extend_add_if_unique(list_kw)



# Save database analysis overview results
with open("../../data/results/bibtex/included_all_kw.bib","w",encoding="utf8") as bibtex_file:
  bib.dump(bib_all_kw_db,bibtex_file,writer=bibtex_writer)



# Save database analysis overview results
with open("../../data/results/bibtex/included_all_kw.csv","w",encoding="utf8") as report_file:
  report_file.write(bib_all_kw_csv)
with open("../../data/results/bibtex/included_all_kw_unique.txt","w",encoding="utf8") as report_file:
  report_file.write("\n".join(list_unique_kw))
