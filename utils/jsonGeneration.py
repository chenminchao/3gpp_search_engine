import json
import re

def get_title_info(catelog):
    title_level = catelog.count('.')
    title_pre = catelog.split()[0]
    key = re.sub(r'\d+', '', catelog)
    key = re.sub('\.', '', key).strip()
    print(title_level, title_pre, key)
    return (key, title_pre, title_level)

def get_desc_info(title_infos, content):
    desc_infos = []
    for i, title_info in enumerate(title_infos):
        title_cur = title_info
        title_next = ()
        start_num = 0
        end_num = 0
        if(i != len(title_infos)-1):
            title_next = title_infos[i+1]
        else:
            # this is hard-coded, check if it is ok
            title_next = ("Annex A (informative)", "", 0)
    
        # get the start desc line num
        for j, line in enumerate(content):
            if(line.find(title_cur[0]) != -1 and line.find(title_cur[1]) != -1 and not line.split()[-1].isdigit()):
                start_num = j            
       
        # get the end desc line num
        for j, line in enumerate(content):
            if(line.find(title_next[0]) != -1 and line.find(title_next[1]) != -1 and not line.split()[-1].isdigit()):
                end_num = j            
   
        desc_infos.append(''.join(content[start_num : end_num]))
    return desc_infos
  
def create_spec_dict_list(title_infos, desc_infos):
    spec_dict_list = []
    print(len(title_infos), len(desc_infos))
    for i, title_info in enumerate(title_infos):
        spec_dict = {}
        spec_dict['key'] = title_info[0] 
        spec_dict['numbering'] = title_info[1]
        spec_dict['title_levle'] = title_info[2]
        spec_dict['desc'] = desc_infos[i]
        spec_dict_list.append(spec_dict)
    return spec_dict_list

def save_json_file(file_name, dict_list):
    with open(file_name, 'w') as f:
        json.dump(dict_list, f)

def main():
    spec_dict_list = []
    title_infos = []
    desc_infos = []
    title_index = []
    content = {}

    with open('/media/minchao/3gpp_search_engine/doc/23401.txt', 'r') as f:
        content = f.readlines()
    
    for line in content:
        if(line.find('Foreword') != -1 and not line[-2].isdigit()):
            break
        
        if(len(line) > 1 and line[0].isdigit() and line[-2].isdigit()):
            title_info = get_title_info(line)
            title_infos.append(title_info)
            title_index.append(title_info[1])
            print(line)

    desc_infos = get_desc_info(title_infos, content)
    spec_dict_list = create_spec_dict_list(title_infos, desc_infos)
       
    save_json_file("/media/minchao/3gpp_search_engine/doc/f23401.json", spec_dict_list)

if __name__ == "__main__":
    main()
