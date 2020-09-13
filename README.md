# 2020SummerResearch_ChineseResDatabase

DO NOT MODIFY THE ORIGINAL EXCEL FILE
In file new_data.csv, each column has the following meaning

1. Number: the unique identifier that correspond to the excel file 'NARA NY CECF DB check list 2020 Summer'
2. ENTRYDATE_YEAR: correspond to column 'ENTRYDATE', this shows what year it is
3. ENTRYDATE_MONTH: correspond to column 'ENTRYDATE', this shows what month it is
4. ENTRYDATE_DAY: correspond to column 'ENTRYDATE', this shows what day it is
5. ENTRYDATE2_YEAR: correspond to column 'ENTRYDAT2', this shows what year it is
6. ENTRYDATE2_MONTH: correspond to column 'ENTRYDATE2', this shows what month it is
7. ENTRYDATE2_DAY: correspond to column 'ENTRYDATE2', this shows what day it is
8. DOCDATE1: correspond to column 'DOCDATE', this shows the first year it appears
9. DOCDATE1: correspond to column 'DOCDATE', this shows the second year it appears
10. BIRTHPLACE_COUNTRY/REGION: correspond to column 'BIRTHPLACE', this shows the country or region of the birthplace
11. BIRTHPLACE_STATE/CITY: correspond to column 'BIRTHPLACE', this shows the state (in U.S.) or city (province) of the birthplace
12. BIRTHPLACE_CITY/COUNTY: correspond to column 'BIRTHPLACE', this shows the city or county (town) of the birthplace, which is comparatively a more specific location than the other two
13. STREET2_NUMBER: correspond to column 'STREET2', this shows the street number, should be integers
14. STREET2_STREET: correspond to column 'STREET2', this shows the street name; some may also be the specific location name, like university
15. STREET2_TYPE: correspond to column 'STREET2', this shows whether it is street ,road, or avenue, etc.
16. STREET2_ROOM: correspond to column 'STREET2', this shows room number or flat number
17. HOMETOWN_NEW: correspond to column 'HOMETOWN', this correct the misspelling and organizes the string format. Some error may still exist since manual check hasn't finished yet
18. SEX: correspond to column 'SEX', this shows the gender.
19. PORT2: correspond to column 'PORT2'.
20. STREET2: correspond to column 'STREET2'.
21. STATE2: correspond to column 'STATE2'.
22. CITY2: correspond to column 'CITY2'.
23. GEO_MARKER: correspond to the geo location in column 'SPONSOR'.
24. SPONSOR_NAME1: correspond to the first sponsor name in column 'SPONSOR' if there is any.
25. SPONSOR_NAME2: correspond to the second sponsor name in column 'SPONSOR' if there is any.
26. SPONSOR_NAME3: correspond to the third sponsor name in column 'SPONSOR' if there is any.

In file you_xu.py, each function deal with one column, as following:

1. 'clean_entry_date(sheet)': clean the column 'ENTRYDATE'; output column 'ENTRYDATE_YEAR', 'ENTRYDATE_MONTH', 'ENTRYDATE_DAY' in csv file
2. 'clean_entry_date2(sheet)': clean the column 'ENTRYDATE2'; output column 'ENTRYDATE2_YEAR', 'ENTRYDATE2_MONTH', 'ENTRYDATE2_DAY' in csv file
3. 'clean_docdate(sheet)': clean the column 'DOCDATE'; output column 'DOCDATE1' and 'DOCDATE2' in csv file
4. 'clean_birthplace(sheet)': clean the column 'BIRTHPLACE'; output column 'BIRTHPLACE_COUNTRY/REGION', 'BIRTHPLACE_STATE/CITY', 'BIRTHPLACE_CITY/COUNTY' in csv file
   a. before the program, the excel file has been manually checked for correction and reformat
   b. even though all data has been manually checked, some data may still inaccurate
5. 'clean_street2(sheet_street)': clean the column 'STREET2'; output column 'STREET2_NUMBER', 'STREET2_STREET', 'STREET2_TYPE', 'STREET2_ROOM' in csv file
6. 'clean_hometown(sheet_street)': correct the misspelling and organizes the string format of column 'HOMETOWN'; it applies Levenshtein module and combines items with more than 93% similarities by replacing them with the meidian string; output column 'HOMETOWN_NEW' in csv file

In the directory Alison_code, you can find detailed implementation of data cleaning. Each ipynb file deals with one column (see file name). Here, STREET2 column did not have any code because there was only about 20-30 misspellings, so I corrected them by hand.
