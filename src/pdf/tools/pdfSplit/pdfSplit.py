# pdf 拆分
from PyPDF2 import PdfFileWriter, PdfFileReader
import click

@click.command()
# 输出文件名
@click.argument('filename')
# 起始页
@click.option('-s', '--start', default=0, type=int, help='start page')
# 结束页
@click.option('-e', '--end', type=int, help='end page')
# 目标文件
@click.option('-t', '--target-file', help='target file')
def annotate(filename, start, end, target_file):
    print ("filename:", filename)
    print ("start:", start)
    print ("end:", end)
    print ("target_file:", target_file)

    src = PdfFileReader(target_file)
    output = PdfFileWriter()
    try:
        # 页码从0开始
        for index in range(start, end + 1):
            print(index - 1)
            output.addPage(src.getPage(index -1 ))
        
        with open(filename, "wb") as output_stream:
                output.write(output_stream)
    except Exception as e:
        print ('pdf split err', repr(e))
if __name__ == '__main__':
    annotate()
