When you download a full reference and citation data set from Web of Science (WoS), the resulting plain text file typically contains several structured fields that describe the articles. Each field has a specific code that indicates the type of information contained within it. Below is a list of common fields you might encounter in such a file, along with their descriptions:

### Common Fields in WoS Plain Text Files

1. **VR** - Version
   - Indicates the version of the data format (e.g., `VR 1.0`).

2. **PT** - Publication Type
   - Describes the type of publication (e.g., `PT S` for a journal article).

3. **AU** - Author
   - The authors of the article (e.g., `AU Ruiz, M`).

4. **AF** - Author Full Name
   - Full names of the authors (e.g., `AF Ruiz, Marco`).

5. **BE** - Book Editor
   - Editors of the book (if applicable).

6. **TI** - Title
   - The title of the article (e.g., `TI Processes Parallel Execution Using Grid Wizard Enterprise`).

7. **SO** - Source
   - The source or journal where the article is published (e.g., `SO BIOMEDICAL INFORMATICS`).

8. **SE** - Series Title
   - The title of the series if the publication is part of a series.

9. **LA** - Language
   - The language of the publication (e.g., `LA English`).

10. **DT** - Document Type
    - The type of document (e.g., `DT Article; Book Chapter`).

11. **DE** - Keywords
    - Keywords associated with the article (e.g., `DE Cluster computing; Grid computing; ...`).

12. **AB** - Abstract
    - The abstract of the article summarizing its content.

13. **C1** - Address
    - The address of the authors or the institution (e.g., `C1 Biomed Informat Res Network, San Diego, CA USA`).

14. **RP** - Corresponding Author
    - Information on the corresponding author (e.g., `RP Ruiz, M (corresponding author)`).

15. **CR** - Cited References
    - The references cited within the article (e.g., `CR Epema DHJ, 1996, FUTURE GENER COMP SY, V12, P53, DOI ...`).

16. **NR** - Number of References
    - The total number of references cited in the article.

17. **TC** - Total Citations
    - The number of times this article has been cited by other articles.

18. **Z9** - Not Used
    - Usually reserved for future use or not applicable.

19. **U1** - Not Used
    - Usually reserved for future use or not applicable.

20. **U2** - Not Used
    - Usually reserved for future use or not applicable.

21. **PU** - Publisher
    - The name of the publisher (e.g., `PU HUMANA PRESS INC`).

22. **PI** - Place of Publication
    - The location of the publisher (e.g., `PI TOTOWA`).

23. **PA** - Publisher Address
    - The full address of the publisher.

24. **SN** - ISSN
    - The International Standard Serial Number (ISSN) of the journal.

25. **EI** - e-ISSN
    - The electronic ISSN of the journal.

26. **BN** - ISBN
    - The International Standard Book Number (ISBN) for books.

27. **J9** - Journal Abbreviation
    - An abbreviation of the journal name.

28. **JI** - Journal Title
    - Full journal title.

29. **PY** - Publication Year
    - The year the article was published (e.g., `PY 2009`).

30. **VL** - Volume
    - The volume number of the journal (e.g., `VL 569`).

31. **BP** - Beginning Page
    - The first page of the article (e.g., `BP 219`).

32. **EP** - Ending Page
    - The last page of the article (e.g., `EP 238`).

33. **DI** - Digital Object Identifier
    - The DOI for the article (e.g., `DI 10.1007/978-1-59745-524-4_11`).

34. **D2** - Alternative DOI
    - Another identifier for the article (if applicable).

35. **PG** - Page Count
    - Total number of pages in the article.

36. **WC** - Web of Science Categories
    - Categories under which the article is classified (e.g., `WC Biochemical Research Methods`).

37. **WE** - Indexing Source
    - The indexing source for the article (e.g., `WE Book Citation Index – Science`).

38. **SC** - Research Areas
    - Scientific categories related to the article (e.g., `SC Biochemistry & Molecular Biology`).

39. **GA** - Accession Number
    - A unique identifier assigned to the record (e.g., `GA BLU18`).

40. **UT** - Unique WOS ID
    - The unique identifier for the article within the WoS database (e.g., `UT WOS:000271018800011`).

41. **PM** - PubMed ID
    - The identifier used in PubMed (if applicable).

42. **DA** - Date of Addition to WoS
    - The date when the article was added to the WoS database (e.g., `DA 2024-09-30`).

43. **ER** - End of Record
    - Marks the end of the record for a specific article.

### Example Structure
Here’s an example of how these fields might look in a plain text file:

```
VR 1.0
PT S
AU Ruiz, M
AF Ruiz, Marco
BE Astakhov, V
TI Processes Parallel Execution Using Grid Wizard Enterprise
SO BIOMEDICAL INFORMATICS
SE Methods in Molecular Biology
LA English
DT Article; Book Chapter
DE Cluster computing; Grid computing; gwe; High performance computing;
   Parallel computing; Resource manager; Job scheduler; Globus; Java; Open
   source
AB The field of high-performance computing (HPC) ...
C1 Biomed Informat Res Network, San Diego, CA USA.
RP Ruiz, M (corresponding author), Biomed Informat Res Network, San Diego, CA USA.
CR Epema DHJ, 1996, FUTURE GENER COMP SY, V12, P53, DOI ...
NR 4
TC 0
Z9 0
U1 0
U2 1
PU HUMANA PRESS INC
PI TOTOWA
PA 999 RIVERVIEW DR, STE 208, TOTOWA, NJ 07512-1165 USA
SN 1064-3745
EI 1940-6029
BN 978-1-934115-63-3
J9 METHODS MOL BIOL
JI Methods Mol. Biol.
PY 2009
VL 569
BP 219
EP 238
DI 10.1007/978-1-59745-524-4_11
D2 10.1007/978-1-59745-524-4
PG 20
WC Biochemical Research Methods; Biotechnology & Applied Microbiology;
   Medical Informatics
WE Book Citation Index – Science (BKCI-S)
SC Biochemistry & Molecular Biology; Biotechnology & Applied Microbiology;
   Medical Informatics
GA BLU18
UT WOS:000271018800011
PM 19623493
DA 2024-09-30
ER
```

### Conclusion
This structure will help you understand how to navigate and process the data when you read the plain text files for your bibliometric analysis or citation graph creation. If you have further questions about specific fields or how to utilize this data, feel free to ask!