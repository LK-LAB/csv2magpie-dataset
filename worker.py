import pandas as pd
from tqdm import tqdm, tqdm_notebook
from tqdm._utils import _term_move_up
from copy import copy
from tempfile import mktemp
from platform import system

from function import func_split

# pandas 경고 무시
pd.options.mode.chained_assignment = None



#### 파일 ####
# 파일 경로
# sample
## file_directory = "/sample-dataset/sample.csv"
file_directory = input("Input file path(relative) : ")

# 파일 이름
## default
file_name = file_directory.split("/")[-1]
## for windows user(using '\' to seperate dir)
if('Windows' == system()):
    if(file_directory.count("\\") != 0):
        file_name = file_directory.split("\\")[-1]


#### 전역 변수 ####
# csv 파일 읽어오기
df_dataset = pd.read_csv(file_directory)

# 원본 데이터 보호를 위해 다른 객체로 복사
temp_set = copy(df_dataset)

# 화학식/분자식 열의 이름 객체 생성(첫 번재 열)
column_comp = temp_set.columns[0]

# 임시 파일 생성
file_temp = mktemp()




#### 문자열 수정 처리 함수 ####
def revise_func(f_temp):
    with open(f_temp, "rt") as file_in:
        file_output = file_name.replace(".csv", ".txt")
        with open("output/" + file_output, "wt") as file_out:
            lines = file_in.readlines()
            lines[0] = lines[0].replace(column_comp + ",", column_comp + " ")
            file_out.write(lines[0])
            i = 1
            while i < len(temp_set.index)+1 :
                lines[i] = lines[i].replace("\",", " ")
                lines[i] = lines[i].replace("\"", "")
                file_out.write(lines[i])
                i += 1
            file_out.close()
        file_in.close()
        print("\noutput/%s" %file_output)




#### 총 작업 함수 ####

# original
def work_func():
    print('')
    for i in range(len(temp_set.index)):
        print("%30s   =====>   %-60s   %6d/%-6d" %(df_dataset[column_comp][i], "", i+1, len(temp_set.index)), end='\r')
        temp_set[column_comp][i] = func_split.encoder(df_dataset[column_comp][i])
        print("%30s   =====>   %-60s" %(df_dataset[column_comp][i], temp_set[column_comp][i]), end='\r')
    temp_set.to_csv(file_temp, index=False)
    revise_func(file_temp)


### 진행률 표시가 포함된 총 작업 함수 ####

# cli - with tqdm progressbar
def work_func_cli():
    prefix = _term_move_up() + '\r'
    print('')
    for i in tqdm(range(len(temp_set.index))):
        tqdm.write(prefix + "%30s   =====>   %-60s" %(df_dataset[column_comp][i], ""))
        temp_set[column_comp][i] = func_split.encoder(df_dataset[column_comp][i])
        tqdm.write(prefix + "%30s   =====>   %-60s" %(df_dataset[column_comp][i], temp_set[column_comp][i]))
    temp_set.to_csv(file_temp, index=False)
    revise_func(file_temp)

# jupyter notebook
def work_func_jn():
    for i in tqdm_notebook(range(len(temp_set.index))):
        print("%30s   =====>   %-60s" %(df_dataset[column_comp][i], ""), end="\r")
        temp_set[column_comp][i] = func_split.encoder(df_dataset[column_comp][i])
        print("%30s   =====>   %-60s" %(df_dataset[column_comp][i],temp_set[column_comp][i]), end="\r")
    temp_set.to_csv(file_temp, index=False)
    revise_func(file_temp)



if('Windows'== system()):
    work_func_cli()
else:
    work_func()