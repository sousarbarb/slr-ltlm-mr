
import os
import bibtexparser as bib



# Load bibtex database
def load_bibtex_db(bib_file_str):
  bib_parser = bib.bparser.BibTexParser()
  bib_parser.common_strings           = False
  bib_parser.ignore_nonstandard_types = False
  bib_parser.homogenize_fields        = False

  return bib.load(open(bib_file_str, encoding="utf8"), parser=bib_parser)


bib_all_db = load_bibtex_db("../../data/results/bibtex/included_all.bib")



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



# Short the references for only the intended entries for each reference
for entry in bib_all_db.entries:
  short_entry = {}
  
  short_entry['ENTRYTYPE'] = entry['ENTRYTYPE']
  short_entry['ID']        = entry['ID']
  short_entry['author']    = entry['author']
  short_entry['title']     = entry['title']
  short_entry['year']      = entry['year']

  if 'journal' in entry:
    short_entry['journal'] = entry['journal']

  if 'booktitle' in entry:
    short_entry['booktitle'] = entry['booktitle']

  if 'doi' in entry:
    short_entry['doi'] = entry['doi']
  else:
    if 'url' in entry:
      short_entry['url'] = entry['url']

  if 'volume' in entry:
    short_entry['volume'] = entry['volume']

  if 'number' in entry:
    short_entry['number'] = entry['number']

  if 'pages' in entry:
    short_entry['pages'] = entry['pages']

  bib_db.entries.append(short_entry)



# Save database analysis overview results
with open("../../data/results/bibtex/included_all_short.bib","w",encoding="utf8") as bibtex_file:
  bib.dump(bib_db,bibtex_file,writer=bibtex_writer)
