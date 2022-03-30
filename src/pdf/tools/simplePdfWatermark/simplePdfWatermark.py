# pdf水印
from io import BytesIO
from re import match

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from webcolors import hex_to_rgb
import click


@click.command()
@click.argument('filename')
# watermark 水印文字
@click.option('-w', '--watermark', default='TEST')
# font-name 水印字体
@click.option('-f', '--font-name', default='Helvetica-Bold',
              help='Font name')
# font-size 水印字体大小
@click.option('-s', '--font-size', default=85, type=int,
              help='Font size')
# color 水印颜色
@click.option('-c', '--color', default='#000000',
              help='Font colour')
# opacity 水印透明度
@click.option('-o', '--opacity', default=1.0,
              help='Opacity from 0 (transparent) to 1 (solid)')
# x y 水印坐标
@click.option('-x', default=250,
              help='X coordinate')
@click.option('-y', default=250,
              help='Y coordinate')
# destination-file-name 水印文件输出地址
@click.option('-d', '--destination-file-name', default='',
              help='Destination file, by default files are modified in place')
# water-page-number 单独打水印页
@click.option('-wpn', '--water-page-number', default=0, type=int,
              help='page number')
# mark-count 每页 每列水印个数
@click.option('-mc', '--mark-count', default=1,
              help='water count')
# columns 每页水印列数 单列 或 三列
@click.option('-col', '--columns', default='single',
              help='multi or single')
def annotate(filename, watermark, font_name, font_size, color, opacity,
             x, y, destination_file_name, water_page_number, mark_count, columns):
    print ("page number:", water_page_number)
    print ("mark_count:", mark_count)
    print ("columns:", columns)
    mask_stream = BytesIO()
    watermark_canvas = canvas.Canvas(mask_stream, pagesize=A4)
    watermark_canvas.setFont(font_name, font_size)
    r, g, b = hex_to_rgb(color)
    c = Color(r, g, b, alpha=opacity)
    watermark_canvas.setFillColor(c)
    print('filename', filename)
    
    watermark_canvas.rotate(10)
    for index in range(0, mark_count):
        x1 = x + index * 40
        watermark_canvas.drawString(x1, y + index * 100, watermark)
        if columns == 'multi':
            x0 = x1 - 300
            x2 = x1 + 300
            watermark_canvas.drawString(x0, y + index * 100, watermark)
            watermark_canvas.drawString(x2, y + index * 100, watermark)
        

   
    watermark_canvas.save()

    mask_stream.seek(0)

    mask = PdfFileReader(mask_stream)
    src = PdfFileReader(filename)
    output = PdfFileWriter()
    # water_page_number参数大于0时单独某页打水印
    if water_page_number > 0:
        for index in range(0, src.getNumPages()):
            page = src.getPage(index)
            if (index + 1 == water_page_number):
                page.mergePage(mask.getPage(0))
                page.compressContentStreams()
            output.addPage(src.getPage(index))
    else:
        # 所有页面打水印
        for index in range(0, src.getNumPages()):
            page = src.getPage(index)
            page.mergePage(mask.getPage(0))
            page.compressContentStreams()
            output.addPage(src.getPage(index))

    if not destination_file_name:
        destination_file_name = filename

    with open(destination_file_name, "wb") as output_stream:
        output.write(output_stream)


if __name__ == '__main__':
    annotate()
