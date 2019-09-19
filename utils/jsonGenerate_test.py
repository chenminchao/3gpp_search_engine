import json

abbr_dict = [
            {"name":"ADC", "desc":"Application Detection and Control"},
            {"name":"BAR", "desc":"Buffering Action Rule"},  
            {"name":"CP", "desc":"Control Plane"} 
            ]

with open("C:\\3gpp_search_engine\\3gpp_search_engine\\doc\\test.json", "w") as f:
    json.dump(abbr_dict, f) 
