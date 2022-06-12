import os
import shutil
import pathlib
import fileinput


file_path = os.path.dirname(os.path.abspath(__file__))
file_names = os.listdir(file_path)

null_path = ""
asin = "asin"
metadata_name = "metadata.jsonp"

pathlib.Path('zip').mkdir(parents=True, exist_ok=True)
zip_path = os.path.abspath("zip")

for book_name in file_names:
    pathlib.Path('temp').mkdir(parents=True, exist_ok=True)
    if ".azw3" in book_name:
        book_full_path = os.path.abspath(book_name)
        over2 = os.path.abspath("temp")
        os.system('azkcreator --source %s --target %s' %(book_full_path,over2))
        zip_temp_path = os.path.join(over2,asin,null_path)
        metadata_path = os.path.join(over2,asin,metadata_name)
        re_num1 = '"asin" : "%s",'%(book_name[:-5])
        re_num2 = '"title" : "%s",' % (book_name[:-5])
        for line in fileinput.input(metadata_path, inplace=1):
            line = line.replace('"asin" : "asin",', re_num1)
            line = line.replace('"title" : "title",', re_num2)
            print(line, end="")

        zip_name =  book_name[:-4] + "zip"
        full_zip_path = os.path.join(zip_path,zip_name)
        os.system('rar a -r -ep1 %s %s'%(full_zip_path,zip_temp_path))
        azk_name = book_name[:-4] + "azk"
        azk_path = os.path.join(zip_path,azk_name)
        os.rename(full_zip_path,azk_path)
        shutil.rmtree(over2)

    elif ".mobi" in book_name:
        book_full_path = os.path.abspath(book_name)
        over2 = os.path.abspath("temp")
        os.system('azkcreator --source %s --target %s' %(book_full_path,over2))

        zip_temp_path = os.path.join(over2,asin,null_path)
        metadata_path = os.path.join(over2,asin,metadata_name)
        re_num1 = '"asin" : "%s",'%(book_name[:-5])
        re_num2 = '"title" : "%s",' % (book_name[:-5])
        for line in fileinput.input(metadata_path, inplace=1):
            line = line.replace('"asin" : "asin",', re_num1)
            line = line.replace('"title" : "title",', re_num2)
            print(line, end="")

        zip_name =  book_name[:-4] + "zip"
        full_zip_path = os.path.join(zip_path,zip_name)
        os.system('rar a -r -ep1 %s %s'%(full_zip_path,zip_temp_path))
        azk_name = book_name[:-4] + "azk"
        azk_path = os.path.join(zip_path,azk_name)
        os.rename(full_zip_path,azk_path)
        shutil.rmtree(over2)