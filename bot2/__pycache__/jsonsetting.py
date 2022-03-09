import json
from collections import OrderedDict
import subject as sbj  # subject.py 가져오기

file_data = OrderedDict()

# 시간표를 json 에 작성 (이 부분만 수정하세요)
file_data["Mon"] = {"1": sbj.korean(), "2": sbj.Programming(), "3": sbj.Social(), "4": sbj.physics(), "5": sbj.Exercise(), "6": sbj.English(), "7": sbj.information()}
file_data["Tue"] = {"1": sbj.art(), "2": sbj.art(), "3": sbj.Exercise(), "4": sbj.Music(), "5": sbj.korean(), "6": sbj.Math(), "7": sbj.dataprocessing()}
file_data["Wed"] = {"1": sbj.Programming(), "2": sbj.Biology(), "3": sbj.English(), "4": sbj.Social(), "5": sbj.CreativeActivities(), "6": sbj.CreativeActivities()}
file_data["Thu"] = {"1": sbj.CareerAndJob(), "2": sbj.circuit(), "3": sbj.datapocessing(), "4": sbj.Social(), "5": sbj.korean(), "6": sbj.Math(), "7": sbj.information()}
file_data["Fri"] = {"1": sbj.chemistry(), "2": sbj.Programming(), "3": sbj.circuit(), "4": sbj.Math(), "5": sbj.Engglish(), "6": sbj.CreativeActivities(), "7": sbj.CreativeActivities}

# Print JSON
print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('timetable.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")