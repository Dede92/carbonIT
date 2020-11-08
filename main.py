
def read_input(filename):
    """
    Read input file
    """
    # Using readlines() 
    file1 = open(filename, 'r') 
    Lines = file1.readlines() 
    
    text = []
    # Strips the newline character 
    for line in Lines: 
        if not line.strip().startswith('#'):
            text.append(line.strip())
            # print("Line: {}".format(line.strip())) 
    return text

def parse_input(input):
    parsed = dict()
    for line in input:
        input_split = line.replace(' ', '').split('-')

        if input_split[0] == 'C':
            parsed['C'] = {
                'x': int(input_split[1]),
                'y': int(input_split[2]),
            }
        if input_split[0] == 'M':
            if 'M' in parsed:
                parsed['M'].append({
                    'x': int(input_split[1]),
                    'y': int(input_split[2]),
                })
            else:                
                parsed['M'] = [{
                    'x': int(input_split[1]),
                    'y': int(input_split[2]),
                }]
        if input_split[0] == 'T':
            if 'T' in parsed:
                parsed['T'].append({
                    'x': int(input_split[1]),
                    'y': int(input_split[2]),
                    'N': int(input_split[3]),
                })
            else:                
                parsed['T'] = [{
                    'x': int(input_split[1]),
                    'y': int(input_split[2]),
                    'N': int(input_split[3]),
                }]
        if input_split[0] == 'A':
            if 'A' in parsed:
                parsed['A'].append({
                    'name': input_split[1],
                    'x': int(input_split[2]),
                    'y': int(input_split[3]),
                    'D': input_split[4],
                    'S': input_split[5],
                })
            else:                
                parsed['A'] = [{
                    'name': input_split[1],
                    'x': int(input_split[2]),
                    'y': int(input_split[3]),
                    'D': input_split[4],
                    'S': input_split[5],
                }]
    return parsed



def init_mapping(input):
    x = input['C']['x']
    y = input['C']['y']
    map = []
    for i in range(y):
        map.append(['-' for i in range(x)])
    init_mountain(map, input)
    init_treasure(map, input)
    return map

def init_mountain(map, input):
    for ele in input['M']:
        map[ele['y']][ele['x']] = 'M'

def init_treasure(map, input):
    for ele in input['T']:
        map[ele['y']][ele['x']] = ele['N']



if __name__ == "__main__":

    pass