# slr-ltlm-mr
A Systematic Literature Review on Long-Term Localization and Mapping for Mobile Robots

## Methodology

### Identification

**Base string:**

`(robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)`

**Inquiries:** 2040 records

- [ACM Digital Library](https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29+OR+Abstract%3A%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29+OR+Keyword%3A%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29)
  - 5 results
  - Title + abstract + author keywords
  - `Title:((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) OR Abstract:((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) OR Keyword:((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong))`
- [Dimensions](https://app.dimensions.ai/discover/publication?search_mode=content&search_text=(robot%20OR%20robots%20OR%20robotics%20OR%20vehicle%20OR%20vehicles)%20AND%20(((localize%20OR%20localization%20OR%20localizing%20OR%20localise%20OR%20localisation%20OR%20localising)%20AND%20(map%20OR%20maps%20OR%20mapping))%20OR%20%22slam%22)%20AND%20(%22long%20term%22%20OR%20%22life%20long%22%20OR%20lifelong)&search_type=kws&search_field=text_search)
  - 430 results
  - Title + abstract
  - `(robot OR robots OR robotics OR vehicle OR vehicles) AND (((localize OR localization OR localizing OR localise OR localisation OR localising) AND (map OR maps OR mapping)) OR "slam") AND ("long term" OR "life long" OR lifelong)`
- [IEEE](https://ieeexplore.ieee.org/search/advanced)
  - 260 results (after removing 173 duplicate records of the inquiries using a
    single field)
  - IEEE limits the maximum number of wildcards (e.g., `*`) in a query to 7
  - Search results obtained using single queries for each search field wanted
  - [Title](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22Document%20Title%22:robot*%20OR%20%22Document%20Title%22:vehicle*)%20AND%20((%22Document%20Title%22:locali*%20AND%20%22Document%20Title%22:map*)%20OR%20%22Document%20Title%22:%22slam%22)%20AND%20(%22Document%20Title%22:%22long%20term%22%20OR%20%22Document%20Title%22:%22life%20long%22%20OR%20%22Document%20Title%22:lifelong)))
    - 6 results
    - `("Document Title":robot* OR "Document Title":vehicle*) AND (("Document Title":locali* AND "Document Title":map*) OR "Document Title":"slam") AND ("Document Title":"long term" OR "Document Title":"life long" OR "Document Title":lifelong)`
  - [Abstract](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22Abstract%22:robot*%20OR%20%22Abstract%22:vehicle*)%20AND%20((%22Abstract%22:locali*%20AND%20%22Abstract%22:map*)%20OR%20%22Abstract%22:%22slam%22)%20AND%20(%22Abstract%22:%22long%20term%22%20OR%20%22Abstract%22:%22life%20long%22%20OR%20%22Abstract%22:lifelong))&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&rowsPerPage=100&pageNumber=1)
    - 193 results
    - `("Abstract":robot* OR "Abstract":vehicle*) AND (("Abstract":locali* AND "Abstract":map*) OR "Abstract":"slam") AND ("Abstract":"long term" OR "Abstract":"life long" OR "Abstract":lifelong)`
  - [Index terms](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22Index%20Terms%22:robot*%20OR%20%22Index%20Terms%22:vehicle*)%20AND%20((%22Index%20Terms%22:locali*%20AND%20%22Index%20Terms%22:map*)%20OR%20%22Index%20Terms%22:%22slam%22)%20AND%20(%22Index%20Terms%22:%22long%20term%22%20OR%20%22Index%20Terms%22:%22life%20long%22%20OR%20%22Index%20Terms%22:lifelong))&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&rowsPerPage=100&pageNumber=1)
    - 158 results
    - `("Index Terms":robot* OR "Index Terms":vehicle*) AND (("Index Terms":locali* AND "Index Terms":map*) OR "Index Terms":"slam") AND ("Index Terms":"long term" OR "Index Terms":"life long" OR "Index Terms":lifelong)`
  - [Author keywords](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22Author%20Keywords%22:robot*%20OR%20%22Author%20Keywords%22:vehicle*)%20AND%20((%22Author%20Keywords%22:locali*%20AND%20%22Author%20Keywords%22:map*)%20OR%20%22Author%20Keywords%22:%22slam%22)%20AND%20(%22Author%20Keywords%22:%22long%20term%22%20OR%20%22Author%20Keywords%22:%22life%20long%22%20OR%20%22Author%20Keywords%22:lifelong)))
    - 2 results
    - `("Author Keywords":robot* OR "Author Keywords":vehicle*) AND (("Author Keywords":locali* AND "Author Keywords":map*) OR "Author Keywords":"slam") AND ("Author Keywords":"long term" OR "Author Keywords":"life long" OR "Author Keywords":lifelong)`
  - [IEEE terms](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22IEEE%20Terms%22:robot*%20OR%20%22IEEE%20Terms%22:vehicle*)%20AND%20((%22IEEE%20Terms%22:locali*%20AND%20%22IEEE%20Terms%22:map*)%20OR%20%22IEEE%20Terms%22:%22slam%22)%20AND%20(%22IEEE%20Terms%22:%22long%20term%22%20OR%20%22IEEE%20Terms%22:%22life%20long%22%20OR%20%22IEEE%20Terms%22:lifelong)))
    - 0 results
    - Query: `("IEEE Terms":robot* OR "IEEE Terms":vehicle*) AND (("IEEE Terms":locali* AND "IEEE Terms":map*) OR "IEEE Terms":"slam") AND ("IEEE Terms":"long term" OR "IEEE Terms":"life long" OR "IEEE Terms":lifelong)`
  - [INSPEC controlled terms](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22INSPEC%20Controlled%20Terms%22:robot*%20OR%20%22INSPEC%20Controlled%20Terms%22:vehicle*)%20AND%20((%22INSPEC%20Controlled%20Terms%22:locali*%20AND%20%22INSPEC%20Controlled%20Terms%22:map*)%20OR%20%22INSPEC%20Controlled%20Terms%22:%22slam%22)%20AND%20(%22INSPEC%20Controlled%20Terms%22:%22long%20term%22%20OR%20%22INSPEC%20Controlled%20Terms%22:%22life%20long%22%20OR%20%22INSPEC%20Controlled%20Terms%22:lifelong)))
    - 1 result
    - `("INSPEC Controlled Terms":robot* OR "INSPEC Controlled Terms":vehicle*) AND (("INSPEC Controlled Terms":locali* AND "INSPEC Controlled Terms":map*) OR "INSPEC Controlled Terms":"slam") AND ("INSPEC Controlled Terms":"long term" OR "INSPEC Controlled Terms":"life long" OR "INSPEC Controlled Terms":lifelong)`
  - [INSPEC non-controlled terms](https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText=((%22INSPEC%20Non-Controlled%20Terms%22:robot*%20OR%20%22INSPEC%20Non-Controlled%20Terms%22:vehicle*)%20AND%20((%22INSPEC%20Non-Controlled%20Terms%22:locali*%20AND%20%22INSPEC%20Non-Controlled%20Terms%22:map*)%20OR%20%22INSPEC%20Non-Controlled%20Terms%22:%22slam%22)%20AND%20(%22INSPEC%20Non-Controlled%20Terms%22:%22long%20term%22%20OR%20%22INSPEC%20Non-Controlled%20Terms%22:%22life%20long%22%20OR%20%22INSPEC%20Non-Controlled%20Terms%22:lifelong))&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&rowsPerPage=75&pageNumber=1)
    - 73 results
    - `("INSPEC Non-Controlled Terms":robot* OR "INSPEC Non-Controlled Terms":vehicle*) AND (("INSPEC Non-Controlled Terms":locali* AND "INSPEC Non-Controlled Terms":map*) OR "INSPEC Non-Controlled Terms":"slam") AND ("INSPEC Non-Controlled Terms":"long term" OR "INSPEC Non-Controlled Terms":"life long" OR "INSPEC Non-Controlled Terms":lifelong)`
- [INSPEC](https://www.engineeringvillage.com/search/submitlink.url?sd=H4sIAAAAAAAAAKVVzW8bRRQf56Ox8%2BGmLULigGTllEbCS1yJFiEOIQlgZbFJUoqSnMazY3va2Z3tzKw%2FKELw%2F8CBO1f%2BAMqBG1eEEBJHjrw3u7OxnR4qMVI%2Bfr%2F33sz73u%2F%2FJqtGkw%2BZips8GYiEcy2SwUhISQe8CXSskqbhVLNh83nG9bR57gA3x4kVdvoRp8mLRrTym%2Fj13yVCJv%2FrLmr4T3%2F9%2BM8v1d%2B%2FXiKdNrnV7fcNt5fkzVzxU2Gs0tMzzpSO4OpLUu9zy4YdOhIDCqJLcm8oBkMJPxbkxwntSR5dkjsiYTKLeDezaWZP%2BNRckk1hDiTXtjtOuG6TzYSOjqilhypLbJtUU%2FD5XHzFQVHzPgSTuwCKBsKispPFPbTbzgCjYQ%2B8j6l5FpJ1yhg3JqKWW7IdPqUjGmRWyADU%2BAchqVF89%2BCL9pEld3OxpMkgOLeYL1DYcgpHwjj3n5NvyHJINhwZwhXGFtQqlTLqFaBKM6uM5bHHPaUkVGd%2FAbccviqxseTe1au82PAKwBR3vNHLpOSQ2kPNqRUqwYhQthSSbS8LFXOywuYWY6EoXb7D1IjrzyG5C2rrkC76sdIxtd7BqMgq4pWQ3PYYEpNKOi0MN6OZ5PvERDzK0gLUHTjUwmLhzHxJ0DWIdc3plLmsR8IwkUoou52mvHypeBh7t%2BQUy2Ke2CeCjxe5Gdt6pMaJVDSaCRFyA49Cg%2FsUQAhCujJ7q2tmzLmPbo0n0QV0o0%2BpSCCymEcCizHjWxXrmUGqC7yVDqdGMCpPZ5RuO4sz1%2BLOZ9IOYVSDmxMc5BMc5BMcaOjDgEkBNkGsIi6D9un8VdhD%2BewYS5n3HsbJZNIahoO2wIGe9d7WdF9PmJLS%2BKIaOiqnoerAdfdVc6%2FaXr6e4w6N%2FX0bOfMlrI79m1TrJvWg6MMZyhStuJVT6VBD35n5J2eKDk4xbPH9BdxawA%2Bub3DYD9xVqeEfrsFzBnAZ54pRZbes4%2F%2FdFPUtefh6VXTVD85LQ5wFvCYSvr1qUBRtZ%2FqtZrKeK54PfMviNsCKP76OvQbjhLuqo0oCFuUx9rNvfiSED2RtJIyAdeeFk9kmrU3heQ3d7MXrSBguITuOmaQETqVCXnHg%2B1bHgW%2FiwDdxYw2fflc5ubBvLcMHKx1XwfDbl7s%2FdycpHEuWVJL6k2m%2FHJs4TM1iOf7w8skff7794hP84uHLFUsqrdT9whuqne47Yfuz9uMbYBm%2BaPBnpfVuqzUvw4Oh3HVZrc15ZUm0q1VP2b1G96wx4kPBJN%2B73zjoHDV2dyUsUin2HIppCjwo7RhJ451CZUeqZNDAJbHjZFL0eQM5BxEhuJ%2BHv3qaCfYM0nBykeZMTUOiRzRhHLMTjcH%2F%2FUfvv7fgP4i6mLj%2FAHhEW31TCAAA)
  (_link maybe be broken due to its length, restart your INSPEC
  session if needed_)
  - 428 results
  - Subject/Title/Abstract: equivalent to retrieving results from any of the
    fields abstract, title, controlled term, or uncontrolled term
    ([link](https://service.elsevier.com/app/answers/detail/a_id/25647/supporthub/engineering-village/#panel10))
  - `(((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) WN KY)`
- [Scopus](https://www.scopus.com/results/results.uri?sort=plf-f&src=s&st1=%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29&sid=ab05b8cb41e4e85b9b1f90ec80501dac&sot=b&sdt=b&sl=115&s=TITLE-ABS-KEY%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29&origin=searchbasic&editSaveSearch=&yearFrom=Before+1960&yearTo=Present)
  - 530 results
  - TITLE-ABS-KEY: equivalent to retrieving results from any of the fields
    abstract, title, and keywords
    ([link](https://service.elsevier.com/app/answers/detail/a_id/11236/supporthub/scopus/kw/TITLE-ABS-KEY/)
  - `TITLE-ABS-KEY((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong))`
- [Web of Science](https://www.webofscience.com/wos/woscc/summary/08d9d511-f688-4cb4-bee0-195db4f123b4-388d46fe/relevance/1)
  - 387 results
  - Topic: equivalent to retrieving results from any of the fields title,
    abstract, author keywords, and Keywords Plus
  - Query: `TS=((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong))`

**Records removed before screening:**

- Duplicates: 1250 records
- Exclusion criteria: 214 records

**Records identified from the search results:** 576 records

### Screening

**Records screened:** 576 records

**Records removed after screening:**

- Duplicates: 13 records
- Exclusion criteria: 153 records

**Records accepted for quality assessment:** 410 records

### Quality Evaluation

**Records assessed for eligibility:** 410 records

## Contacts

If you have any questions or you want to know more about the work developed by
us, please contact one of the contributors of this project:

- Ricardo B. Sousa ([gitlab](https://gitlab.com/sousarbarb/),
  [github](https://github.com/sousarbarb/),
  [personal](mailto:sousa.ricardob@outlook.com),
  [feup:professor](mailto:rbs@fe.up.pt),
  [feup:student](mailto:up201503004@edu.fe.up.pt),
  [inesctec](mailto:ricardo.b.sousa@inesctec.pt))
  _(corresponding author)_
- Héber Miguel Sobreira ([gitlab](https://gitlab.inesctec.pt/heber.m.sobreira),
  [inesctec](mailto:heber.m.sobreira@inesctec.pt))
- António Paulo Moreira ([feup](mailto:amoreira@fe.up.pt))

Project Link:
[https://github.com/sousarbarb/slr-ltlm-mr](https://github.com/sousarbarb/slr-ltlm-mr)

## Acknowledgements

- [CRIIS - Centre for Robotics in Industry and Intelligent Systems](https://www.inesctec.pt/en/centres/criis)
  from
  [INESC TEC - Institute for Systems and Computer Engineering, Technology and Science](https://www.inesctec.pt/en)
- [Faculty of Engineering, University of Porto (FEUP)](https://sigarra.up.pt/feup/en/WEB_PAGE.INICIAL)

## Funding

This work is financed by National Funds through the Portuguese funding agency,
[FCT - Fundação para a Ciência e a Tecnologia](https://www.fct.pt/index.phtml.en),
within scholarship 2021.04591.BD.
