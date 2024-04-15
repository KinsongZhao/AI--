import json
import pandas as pd
import os
import shutil

path_dir = 'files'
tran_flie_name = 'train.json'
dev_flie_name = 'dev.json'
if os.path.exists(path_dir):
    pass
else:
    os.mkdir(path_dir)


df = pd.read_excel("train_.xls")
i = 0
write_type = "w"
for clm in df.iloc:
    if i>0:
        write_type = "a"
    print(clm["content"])
    print(clm["summary"])

    test_dict = {
    "content": clm["content"],
    "summary": clm["summary"]
    }
    with open(path_dir+"/"+tran_flie_name,write_type,encoding="utf8") as f:
        json.dump(test_dict,f,ensure_ascii=False)
        f.write('\n')
        print("加载入文件完成...")
    i+=1

    shutil.copyfile(path_dir+"/"+tran_flie_name,path_dir+"/"+dev_flie_name)