import arxiv
import PyPDF2
search = arxiv.Search(
    query="IEE 2021",
    max_results=30
)
i=0
# for result in search.results():
#     result.download_pdf(dirpath="D:\PDFY", filename="paper{}.pdf".format(i))
#     i+=1
# print("Success")

for x in range(30):
    words = 1
    filepath="D:\PDFY\paper{}.pdf".format(x)
    f=open(filepath,"rb")
    pdfReader = PyPDF2.PdfReader(f)
    t = pdfReader.extractText()
    e = len(t)
    for y in t:
        if y.isspace():
            words+=1
            e-=1
    print("Znaki ze spacjami",len(t),
    "\nZnaki bez spacji",e,
    "\nWyrazy",words
    )