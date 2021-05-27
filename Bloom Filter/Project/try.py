

import pdfkit
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_url('https://medium.com/swlh/chatbots-were-the-next-big-thing-what-happened-5fc49dd6fa61',r'.\PDFs\test1.pdf',configuration=config)

