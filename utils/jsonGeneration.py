import json
import re
import argparse

def get_title_info(catelog):
    title_level = catelog.count('.')
    title_pre = catelog.split()[0]
    key = re.sub(title_pre, '', catelog)
    key = re.sub(r'\d+', '', key).strip()
    print(title_level, title_pre, key)
    return (key, title_pre, title_level)

def get_desc_info(title_infos, content):
    desc_infos = []
    start_num = 0
    end_num = 0
    for i, title_info in enumerate(title_infos):
        title_cur = title_info
        title_next = ()
        if(i != len(title_infos)-1):
            title_next = title_infos[i+1]
        else:
            # this is hard-coded, check if it is ok
            title_next = ("Annex A (informative)", "", 0)
    
        # get the start desc line num
        for j, line in enumerate(content[end_num:]):
            if (line.find(title_cur[0]) != -1 and line.find(title_cur[1]) != -1 and not line.split()[-1].isdigit()):
                print(line.split(title_cur[1])[1].strip())
                print(title_cur[0])
            if(line.find(title_cur[0]) != -1 and line.find(title_cur[1]) != -1
                    and line.split(title_cur[1])[1].strip() == title_cur[0] and not line.split()[-1].isdigit()):
                start_num = end_num + j
                break;
       
        # get the end desc line num
        for j, line in enumerate(content[start_num:]):
            if (line.find(title_next[0]) != -1 and line.find(title_next[1]) != -1
                    and title_next[0] != "Annex A (informative)"
                    and not line.split()[-1].isdigit()):
                print(line.split(title_next[1])[1].strip())
                print(title_next[0])
            if(line.find(title_next[0]) != -1 and line.find(title_next[1]) != -1
                    and title_next[0] != "Annex A (informative)" and line.split(title_next[1])[1].strip() == title_next[0]
                    and not line.split()[-1].isdigit()):
                end_num = start_num + j
                break;

        print(title_cur[1], start_num, end_num)
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

def main(input, output):
    spec_dict_list = []
    title_infos = []
    desc_infos = []
    title_index = []
    content = {}

    with open(input, 'r') as f:
        content = f.readlines()
    
    for i, line in enumerate(content):
        if(line.find('Foreword') != -1 and not line[-2].isdigit()):
            break
        
        if((len(line) > 1 and line[0].isdigit() and line[-2].isdigit()) or
            (len(line) > 1 and line[0].isdigit() and content[i+1][-2].isdigit())):
            title_info = get_title_info(line)
            title_infos.append(title_info)
            title_index.append(title_info[1])
            print(line)

    desc_infos = get_desc_info(title_infos, content)
    spec_dict_list = create_spec_dict_list(title_infos, desc_infos)
       
    save_json_file(output, spec_dict_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="convert txt file to json file")
    parser.add_argument("--input", required="true")
    parser.add_argument("--output", required="true")
    args = parser.parse_args()
    main(args.input, args.output)
