import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

from pdfminer.layout import (
    LAParams,
    LTAnno,
    LTChar,
    LTTextLineHorizontal,
    LTTextLineVertical,
    LTImage,
)

def get_text_objects(layout, ltype="char", t=None):
    """Recursively parses pdf layout to get a list of
    PDFMiner text objects.

    Parameters
    ----------
    layout : object
        PDFMiner LTPage object.
    ltype : string
        Specify 'char', 'lh', 'lv' to get LTChar, LTTextLineHorizontal,
        and LTTextLineVertical objects respectively.
    t : list

    Returns
    -------
    t : list
        List of PDFMiner text objects.

    """
    if ltype == "char":
        LTObject = LTChar
    elif ltype == "image":
        LTObject = LTImage
    elif ltype == "horizontal_text":
        LTObject = LTTextLineHorizontal
    elif ltype == "vertical_text":
        LTObject = LTTextLineVertical
    if t is None:
        t = []
    try:
        for obj in layout._objs:
            if isinstance(obj, LTObject):
                t.append(obj)
            else:
                t += get_text_objects(obj, ltype=ltype)
    except AttributeError:
        pass
    return t




def get_rotation(chars, horizontal_text, vertical_text):
    rotation = ""
    hlen = len([t for t in horizontal_text if t.get_text().strip()])
    vlen = len([t for t in vertical_text if t.get_text().strip()])
    print(hlen,vlen)
    if hlen < vlen:
        clockwise = sum(t.matrix[1] < 0 and t.matrix[2] > 0 for t in chars)
        anticlockwise = sum(t.matrix[1] > 0 and t.matrix[2] < 0 for t in chars)
        rotation = "anticlockwise" if clockwise < anticlockwise else "clockwise"
    return rotation


def _nurminen_table_detection(textlines):
    # TODO: add support for arabic text #141
    # sort textlines in reading order
    textlines.sort(key=lambda x: (-x.y0, x.x0))
    print('entered the table detection algo')
    return "test"

def extract_tables(textlines):
    print('ex  tracting tables')
    _nurminen_table_detection(textlines)




filepath = "data.pdf"
infile = PdfFileReader(open(filepath, "rb"), strict=False)
print('Printing the number of pages',infile.getNumPages())

page_numbers = []
page_numbers.append({"start": 2, "end": 2})
temp = "temp"
print(page_numbers)
page = 2
with open(filepath, "rb") as fileobj:
    infile = PdfFileReader(fileobj, strict=False)
    fpath = os.path.join(temp, "page-{0}.pdf".format(page))
    print(fpath)
    froot, fext = os.path.splitext(fpath)
    p = infile.getPage(page - 1)
    outfile = PdfFileWriter()
    outfile.addPage(p)
    with open(fpath, "wb") as f:
        outfile.write(f)
        f.close()

    with open(fpath, "rb") as f:
        print('reading file now')
        parser = PDFParser(f)
        document = PDFDocument(parser)
        laparams = LAParams(
            char_margin=1.0,
            line_margin=0.5,
            word_margin=0.1,
            detect_vertical=True,
            all_texts=True,
        )
        rsrcmgr = PDFResourceManager()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            width = layout.bbox[2]
            height = layout.bbox[3]
            dim = (width, height)
            print(dim,layout)
            chars = get_text_objects(layout,ltype="char")

            horizontal_text = get_text_objects(layout, ltype="horizontal_text")
            vertical_text = get_text_objects(layout, ltype="vertical_text")
            for data in horizontal_text:
                print(data)
            #Tries to find rotation
            rotation = get_rotation(chars,horizontal_text,vertical_text)
            if rotation != "":
                print('rotation is needed for the page')
            else:
                print('No rotation is needed')
            extract_tables(horizontal_text)

