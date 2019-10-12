import os
import subprocess
import doc_x_to_html
from docx2html import convert
import HTMLParser

def call_soffice(args):
    p = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr = p.communicate()
    if p.returncode != 0 or stderr[:7] == b'Error: ':
        return 1
    return 0

def convert_doc_to_html(input,outdir): # LibreOffice
    print(input,'-->',outdir)
    #subprocess.call(['soffice', '--headless', '--convert-to','html:XHTML Writer File:UTF8','--outdir', outdir, input])
    #args = ['soffice', '--headless', '--convert-to', 'html:XHTML Writer File:UTF8', '--outdir', outdir, input]
    #call_soffice(args)
    html_parser = HTMLParser.HTMLParser()

    html = convert(input) #使用docx2html模块将docx文件转成html串，随后你想干嘛都行

    html_parser.unescape(html) #这句非常关键，docx2html模块将中文进行了转义，所以要将生成的字符串重新转义回来！
    #该片段来自于http://outofmemory.cn



def main(in_path, out_path):
    input_files = [f for f in os.listdir(in_path) if os.path.isfile(os.path.join(in_path, f)) and f.endswith(".docx")]
    for input_file in input_files:
        convert_doc_to_html(os.path.join(in_path, input_file), out_path)


if __name__ == "__main__":

    # abspath = os.getcwd()             # 获取当前路径
    rootpath = os.path.abspath('..')  # 获取上级路径

    in_Path = rootpath + "\\doc"
    out_Path = rootpath + "\\htm"

    main(in_Path, out_Path)