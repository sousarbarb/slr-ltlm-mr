from fileinput import close
import os
import bibtexparser

# Utilities
# - month definition
def month2num(month):
  if month[0] == "j" and month[1] == "a":
    return "1"
  if month[0] == "f":
    return "2"
  if month[0] == "m" and month[1] == "a" and month[2] == "r":
    return "3"
  if month[0] == "a" and month[1] == "p":
    return "4"
  if month[0] == "m" and month[1] == "a" and month[2] == "y":
    return "5"
  if month[0] == "j" and month[1] == "u" and month[2] == "n":
    return "6"
  if month[0] == "j" and month[1] == "u" and month[2] == "l":
    return "7"
  if month[0] == "a" and month[1] == "u":
    return "8"
  if month[0] == "s":
    return "9"
  if month[0] == "o":
    return "10"
  if month[0] == "n":
    return "11"
  if month[0] == "d":
    return "12"

# - unify references format to the desired one
def custom_unify_reference(record):
  global report

  # - missing fields
  missing_str = ""

  # - type (output: type with upper cases)
  if 'ENTRYTYPE' in record:
    record['ENTRYTYPE'] = record['ENTRYTYPE'].upper()

  # - volume
  if 'volume' in record:
    record['volume'] = record['volume'].replace(" ","")
    if len(record['volume']) == 0 and record['ENTRYTYPE'] == "ARTICLE":
      missing_str += "volume "
  else:
    if record['ENTRYTYPE'] == "ARTICLE":
      missing_str += "volume "

  # - issue
  if 'number' in record:
    record['number'] = record['number'].replace(" ","")
    if len(record['number']) == 0 and record['ENTRYTYPE'] == "ARTICLE":
      missing_str += "number "
  else:
    if record['ENTRYTYPE'] == "ARTICLE":
      missing_str += "number "

  # - pages (output: double hyphen + no spaces)
  if 'pages' in record:
    record['pages'] = record['pages'].replace(" ","")
    if len(record['pages']) == 0:
      missing_str += "pages "
    else:
      record = bibtexparser.customization.page_double_hyphen(record)
  else:
    missing_str += "pages "

  # - link (output: mantain link, copy to doi if it has the DOI link)
  if 'url' in record:
    record['url'] = record['url'].replace(" ","")
    if "doi.org/" in record['url']:
      record['doi'] = record['url'].split("doi.org/")[1]

  # - doi (output: only the DOI number, not the link)
  if 'doi' in record:
    record['doi'] = record['doi'].replace(" ","")
    if len(record['doi']) == 0:
      missing_str += "DOI "
    elif "doi.org/" in record['doi']:
      record['doi'] = record['doi'].split("doi.org/")[1]
  else:
    missing_str += "DOI "

  # - year (output: YYYY)
  if 'year' in record:
    record['year'] = record['year'].replace(" ","")
    if "/" in record['year']:
      date_array = record['year'].split("/")
      record['year'] = ""
      
      for date_field in date_array:
        if len(date_field) == 4:
          record['year'] = date_field

    if len(record['year']) == 0:
      missing_str += "year "
  else:
    missing_str += "year "

  # - month (output: 1-12)
  if 'month' in record:
    record['month'] = record['month'].replace(" ","")
    if any(c.isalpha() for c in record['month']):
      record['month'] = month2num(record['month'].lower())

  # - print missing fields
  if len(missing_str) > 0:
    report += "[" + record['ID'] + "] " + missing_str + "\n"

  return record



# Customize the default parser
bibtex_parser = bibtexparser.bparser.BibTexParser()
bibtex_parser.common_strings           = False
bibtex_parser.customization            = custom_unify_reference
bibtex_parser.ignore_nonstandard_types = False
bibtex_parser.homogenize_fields        = False

# Customization of the default writer
bibtex_writer = bibtexparser.bwriter.BibTexWriter()
bibtex_writer.add_trailing_comma = True
bibtex_writer.contents      = ['entries']
bibtex_writer.display_order = [
    'author','journal','booktitle','title', 'volume','number','pages','doi',
    'note','ISBN','ISSN','publisher','address','year','month']
bibtex_writer.indent           = '  '
bibtex_writer.order_entries_by = ('author','year','ID')



# File processing
file_str = "../../data/search/example.bib"
report = ""

with open(file_str,encoding="utf8") as bibtex_file:
	bibtex_db = bibtexparser.load(bibtex_file,parser=bibtex_parser)

print(report)

with open(os.path.splitext(file_str)[0]+"_proc.bib","w",encoding="utf8") as bibtex_file:
  bibtexparser.dump(bibtex_db,bibtex_file,writer=bibtex_writer)


with open(os.path.splitext(file_str)[0]+"_proc_report.txt","w",encoding="utf8") as report_file:
  report_file.write(report);
