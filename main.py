
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
    init_adventurers(map, input)
    return map

def init_mountain(map, input):
    for ele in input['M']:
        map[ele['y']][ele['x']] = 'M'

def init_treasure(map, input):
    for ele in input['T']:
        map[ele['y']][ele['x']] = ele['N']

def init_adventurers(map, input):
    for ele in input['A']:
        map[ele['y']][ele['x']] = 'A-{}'.format(ele['name'])

def move_adventurers(map, input):
    adventurers = input['A']
    final_adventurers = dict()
    for adven in adventurers:
        print(adven)
        pos_x = adven['x']
        pos_y = adven['y']
        compass = ['N', 'E', 'S', 'W']
        direc = compass.index(adven['D'])
        num_tre = 0
        sequences = [char for char in adven['S']]

        for mvt in sequences:
            # print('MVT: ', mvt)
            # print('DIREC: ', direc)
            # print('POS_X: {}, POS_Y:{}'.format(pos_x, pos_y))
            if mvt == 'A':
                futur_y = pos_y
                futur_x = pos_x
                if direc == 0:
                    futur_y -= 1
                if direc == 1:
                    futur_x += 1
                if direc == 2:
                    futur_y += 1
                if direc == 3:
                    futur_x -= 1
                
                #  Check map
                pos_map = map[futur_y][futur_x]
                # print('F_X: {}, F_Y:{}'.format(futur_x, futur_y))
                # print('POS_MAP: ', pos_map)
                if pos_map == 'M' or str(pos_map).startswith('A-'):
                    pass
                elif isinstance(pos_map, int):
                    if pos_map > 0:
                        num_tre += 1
                        map[futur_y][futur_x] = map[futur_y][futur_x] - 1
                    pos_x = futur_x
                    pos_y = futur_y
                else: 
                    pos_x = futur_x
                    pos_y = futur_y
            if mvt == 'D':
                direc += 1
                if direc > 3:
                    direc = 0
            if mvt == 'G':
                direc -= 1
                if direc < 0:
                    direc = 3
        final_adventurers[adven['name']] = {
            'pos_x': pos_x,
            'pos_y': pos_y,
            'num_tre': num_tre,
            'D': compass[direc],
        }
    print(map)
    print(final_adventurers)
    pass


if __name__ == "__main__":
    text = read_input('input.txt')
    parsed = parse_input(text)
    print(parsed)
    map = init_mapping(parsed)
    print(map)
    move_adventurers(map, parsed)

    pass