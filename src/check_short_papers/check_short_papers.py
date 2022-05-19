import pandas
import os
import re

# Load Excel file
file_str   = "../../data/methodology/identification/parsifal_identification.xlsx"
file_sheet = "Articles"

parsifal_xlsx = pandas.read_excel(file_str,sheet_name=file_sheet,header=0,dtype=str)

print(parsifal_xlsx)



# Identify short papers from the ones that have an Unclassified status
report = "i,title,doi,pages,#pages,\n"
num_pages_short_paper = 4

for i in range(len(parsifal_xlsx.pages)):
	if str(parsifal_xlsx.status[i]) == "Unclassified":
		tmp = str(parsifal_xlsx.pages[i])

		if re.search(r"[0-9]--[0-9]",tmp):
			pages = tmp.split("--")
			try:
				if int(pages[1]) - int(pages[0])+1 <= num_pages_short_paper and int(pages[1]) - int(pages[0])+1 > 0:
					report += str(i) + ',' + str(parsifal_xlsx.title[i]).rstrip().replace(",","") + ',' + str(parsifal_xlsx.doi[i]) + ',' + tmp + ',' + str(int(pages[1]) - int(pages[0])+1) + ',\n'

			except ValueError:
				continue



# Print and report relative to identifying short papers
print(report)

with open(os.path.splitext(file_str)[0]+"_short-papers_report.csv","w",encoding="utf8") as report_file:
  report_file.write(report);
