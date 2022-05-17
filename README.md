# slr-ltlm-mr
A Systematic Literature Review on Long-Term Localization and Mapping for Mobile Robots

## Methodology

### Identification

**Base string:**

`(robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)`

**Inquiries:**

- [ACM Digital Library](https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29+OR+Abstract%3A%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29+OR+Keyword%3A%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29)
  - 5 results
  - Title + abstract + author keywords
  - `Title:((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) OR Abstract:((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) OR Keyword:((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong))`
- [Dimensions](https://app.dimensions.ai/discover/publication?search_mode=content&search_text=(robot%20OR%20robots%20OR%20robotics%20OR%20vehicle%20OR%20vehicles)%20AND%20(((localize%20OR%20localization%20OR%20localizing%20OR%20localise%20OR%20localisation%20OR%20localising)%20AND%20(map%20OR%20maps%20OR%20mapping))%20OR%20%22slam%22)%20AND%20(%22long%20term%22%20OR%20%22life%20long%22%20OR%20lifelong)&search_type=kws&search_field=text_search)
  - 430 results
  - Title + abstract
  - `(robot OR robots OR robotics OR vehicle OR vehicles) AND (((localize OR localization OR localizing OR localise OR localisation OR localising) AND (map OR maps OR mapping)) OR "slam") AND ("long term" OR "life long" OR lifelong)`
- [IEEE](https://ieeexplore.ieee.org/search/advanced) ( results)
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
- [INSPEC](https://www.engineeringvillage.com/search/submitlink.url?sd=H4sIAAAAAAAAAN1VS28jRRBu57Gx814WkDggWTllI%2BHBXokFIQ7ZJAvWDjZ5ENjk1O5p273bMz3b3eMHixD8Hzhw508sHLhxRQghceRIVc%2F0xHH2gMRtW0o7X1V1dz2%2Bqvn%2BL7JsNPmIqbjBk4FIONciGYyElHTAGyCOVdIwnGo2bDzLuJ42Th3g5iixwk4fcJo8r0dLv4pf%2FlkgZPK%2F7qKG%2F%2FTnj3%2B%2FqP729QLptMmtbr9vuL0gb%2BaGnwhjlZ6ecKZ0BFdfkM0%2Bt2zYoSMxoKC6IHeGYjCU8GdBf5TQnuTRBbktEiaziHczm2b2EZ%2BaC7IuzL7k2nbHCddtsp7Q0SG19EBliW2Tago%2Bn4qvOBhq3odgchfA0EBYVHayuIfntjPAeLAH3sfUPA3JKmWMGxNRyy3ZDp%2FQEQ0yK2QAZvzDkNQovrv%2FefvQktdytaTJIDi1mC8w2HAGh8I495%2BRb8hiSNacMIQrjC1Ey1TKqFeAKs2sMpbHHveUklCd5hxuOXxZYmPJncuXebHmDUBS3PF6L5OSQ2oPNKdWqAQjQt1CSLa9LlTM6YoztxgLRenybaZGXH8GyZ0zW4V00YdKx9R6B6Miq4iXQrLlMSQmlXRaHFyPZpLvExPxKEsLsOnAgRYWC2eulwRdg1hXnE2Zy81IGCZSCWW305SXLxUPI3dLmWJZzBN7Lvh4XjZzdjNS40QqGs2ECLmBR4HgPgUQgpCuzP7UlWTMuY9uhSfRY2CjT6lIILKYRwKLMeNbFeuZQaoLvJEOp0YwKo9njLbciRNHceczaYfQqsHNDg7yDg7yDg408DBgUsCZIFYRl0H7%2BPpVyKG8d4ylzHsP7WQyaQ3DRpuTgZ313tZ0X0%2BYktL4oho6Kruh6sAV%2B6q5V22vX81xh8b%2BvrVc8gWMjuZNUeum6F7BwxmRKai4kYvSoQbemetPzhQdnGJI8eYcbs3he1c3OOwb7rK08A%2FX4DkDuIxzyaiSLav4fzdFe0vu%2F7cquuoHp%2BVB7AW8JhKeXjUoirYzfKuZrOeK5wPfsDgNsOJnV7HXoJ1wVnVUKYBBeYR89uRHgfCBrIyEETDuvHIyS9LaFJ7XwGavXkWB4RKy4ySTlMCqVCrk5oLv2yY2fAMbvoETa%2Fjku8qjx%2FatRfhgpeMqHPz2RfPL%2B5MUliULmL6F7onb0nzHlWk%2FKBvYWI1iUP7w8%2Fnvf7z9%2FGP8%2BqEXFUsqrdRteFu1030nbH%2FaPrsBFuHrBj9LrXdbres6XBjWGy7DtWseWhLtatVTdq%2FePamP%2BFAwyffu1vc7h%2FXdXQlDVYo9h2KaghyMdoyk8U5hsiNVMqjjwNhxOin6vI4yBxEhuPtqPZNhHrfy4rxKcVmyfJwJ9hRIetaGbf8BbAfnsD0MkSo1DS0yognjyONoDGxrvv%2FBe3NsQ4on8Psvb0fzlQ0KAAA%3D)
  (272 results) (_link maybe be broken due to its length, restart your INSPEC
  session if needed_)
  - Query: `((((((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) WN TI) OR (((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) WN AB)) OR (((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) WN CV) ) OR (((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong)) WN FL))`
- [Scopus](https://www.scopus.com/results/results.uri?sort=plf-f&src=s&st1=%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29&sid=ab05b8cb41e4e85b9b1f90ec80501dac&sot=b&sdt=b&sl=115&s=TITLE-ABS-KEY%28%28robot*+OR+vehicle*%29+AND+%28%28locali*+AND+map*%29+OR+%22slam%22%29+AND+%28%22long+term%22+OR+%22life+long%22+OR+lifelong%29%29&origin=searchbasic&editSaveSearch=&yearFrom=Before+1960&yearTo=Present)
  (530 results)
  - Query: `TITLE-ABS-KEY((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong))`
- [Web of Science](https://www.webofscience.com/wos/woscc/summary/08d9d511-f688-4cb4-bee0-195db4f123b4-388d46fe/relevance/1)
  (387 results)
  - Query: `TS=((robot* OR vehicle*) AND ((locali* AND map*) OR "slam") AND ("long term" OR "life long" OR lifelong))`
