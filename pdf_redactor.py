import fitz
 
class Redactor:
 
    # constructor
    def __init__(self, path,outpath,redact_coords):
        self.path = path
        self.outpath = outpath
        self.redact_coords = redact_coords
 
    def redaction(self,page_nums):
         
        # PDF開封
        doc = fitz.open(self.path)
         
        # 各ページをiterate
        for i,page in enumerate(doc):
            if i in page_nums:
                areas = [fitz.Rect(coord) for coord in self.redact_coords]
                [page.add_redact_annot(area, fill = (0, 0, 0)) for area in areas]
                
                # 黒塗りする
                page.apply_redactions()
             
        # 新しいPDFとして保存
        doc.save(self.outpath)
        print("Successfully redacted")

path = 'test.pdf'
outpath = 'test_redacted.pdf'
redact_coords = [(37,80,550,219),(37,220,289,242)]
pages_to_redact = [0,1]

redactor = Redactor(path,outpath,redact_coords)
redactor.redaction(pages_to_redact)

# import os
# import glob

# # 黒塗り座標
# redact_coords = [(37,80,550,219),(37,220,289,242)]
# # 黒塗りページ
# pages_to_redact = [0,1]

# # 黒塗りしたいpdfが入ってるフォルダの指定
# directory = '<pdfファイルが置かれたフォルダへのパス>'
# pdf_files = glob.glob(os.path.join(directory, '*.pdf'))
# for path in pdf_files:
#     outpath = f"{path[:-4]}_redacted.pdf"
#     redactor = Redactor(path,outpath,redact_coords)
#     redactor.redaction(pages_to_redact)
