
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
        temp = dict()

        if input_split[0] in parsed:
            for idx in range(1, len(input_split)):
                temp[idx] = input_split[idx]
            parsed[input_split[0]].append(temp)
        else:         
            for idx in range(1, len(input_split)):
                temp[idx] = input_split[idx]
            parsed[input_split[0]] = [temp]

    return parsed

def init_map(input):
    x = int(input['C'][0][1])
    y = int(input['C'][0][2])
    map = []
    for i in range(y):
        map.append(['-' for i in range(x)])

    for field in ['M', 'T', 'A']:
        for ele in input[field]:
            if field == 'M':
                map[int(ele[2])][int(ele[1])] = 'M'
            elif field == 'T':
                map[int(ele[2])][int(ele[1])] = ele[3]
            elif field == 'A':
                map[int(ele[3])][int(ele[2])] = 'A-{}'.format(ele[1])
    return map

def move_adventurers(map, input):
    adventurers = input['A']
    final_adventurers = dict()
    for adven in adventurers:
        print(adven)
        pos_x = int(adven[2])
        pos_y = int(adven[3])
        compass = ['N', 'E', 'S', 'W']
        direc = compass.index(adven[4])
        num_tre = 0
        sequences = [char for char in adven[5]]

        for mvt in sequences:
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
                pos_map = ''
                try:
                    pos_map = map[futur_y][futur_x]
                except IndexError:
                    pass

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
        final_adventurers[adven[1]] = {
            'pos_x': pos_x,
            'pos_y': pos_y,
            'num_tre': num_tre,
            'D': compass[direc],
        }
    display_map(map)
    print(final_adventurers)
    pass

def display_map(map):
    for y in map:
        print(y)

if __name__ == "__main__":
    text = read_input('input.txt')
    parsed = parse_input(text)
    print(parsed)
    map = init_map(parsed)
    display_map(map)
    move_adventurers(map, parsed)

    pass