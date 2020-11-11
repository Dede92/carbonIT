import re
from datetime import datetime

def read_input(filename):
    """
    Read input file
    """
    # Using readlines() 
    file1 = open(filename, 'r') 
    Lines = file1.readlines() 
    file1.close()
    
    text = []
    # Strips the newline character 
    for line in Lines: 
        if not line.strip().startswith('#'):
            text.append(line.strip())
    return text

def parse_input(input):
    """
    Parse the text into a dict
    """
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

def write_output(treasure_map, adventurers):
    """
    Write the and adventurers to an txt file
    """
    with open('output_{}.txt'.format(datetime.now()), 'a') as f:
        f.write('C - {} - {}\n'.format(len(treasure_map[0]), len(treasure_map)))
        for y in range(len(treasure_map)):
            for x in range(len(treasure_map[y])):
                if treasure_map[y][x] == 'M':
                    f.write('M - {} - {}\n'.format(x,y))
                elif re.search(r'T\(\d+\)', treasure_map[y][x]):
                    pattern = re.compile(r'\((\d+)\)')
                    num = int(pattern.findall(treasure_map[y][x])[0])
                    f.write('T - {} - {} - {}\n'.format(x, y, num))
        # Write adventurers to file
        for name in adventurers:
            adven = adventurers[name]
            f.write('A - {} - {} - {} - {} - {}\n'.format(name, adven['x'], adven['y'], adven['direc'], adven['treasure']))

def init_map(input):
    """
    Create a map based on the dictionnay in input
    """
    x = int(input['C'][0][1])
    y = int(input['C'][0][2])
    treasure_map = []
    for i in range(y):
        treasure_map.append(['' for i in range(x)])

    for field in ['M', 'T', 'A']:
        for ele in input[field]:
            if field == 'M':
                treasure_map[int(ele[2])][int(ele[1])] = 'M'
            elif field == 'T':
                treasure_map[int(ele[2])][int(ele[1])] = 'T({})'.format(ele[3])
            elif field == 'A':
                treasure_map[int(ele[3])][int(ele[2])] = 'A-{}'.format(ele[1])
    return treasure_map

def parse_adventurers(input):
    """
    Extract adventurers from the input and create the mvt sequence
    """
    adven_pos = {}
    adven_seq = []
    for adven in input['A']:
        seq = [adven[1]+'-'+x for x in adven[5]]
        adven_pos[adven[1]] = {
            'x': adven[2],
            'y': adven[3],
            'direc': adven[4],
            'seq': seq,
            'len_seq': len(seq),
            'treasure': 0,
        }
        adven_seq.append(seq)
    
    sequence = []
    max_seq_len = max(map(len, adven_seq))
    for x in range(max_seq_len):    
        for y in range(len(adven_seq)):
            try:
                sequence.append(adven_seq[y][x])
            except IndexError:
                pass

    return adven_pos, sequence

def move_adventurers(treasure_map, positions, sequence):
    """
    Apply the sequence mvt
    """
    for seq in sequence:
        name, mvt = seq.split('-')
        pos_x = int(positions[name]['x'])
        pos_y = int(positions[name]['y'])
        compass = ['N', 'E', 'S', 'W']
        direc = compass.index(positions[name]['direc'])
        # Si y a un changement de direction
        if mvt == 'D':
            direc += 1
            if direc > 3:
                direc = 0
            positions[name]['direc'] = compass[direc]
        if mvt == 'G':
            direc -= 1
            if direc < 0:
                direc = 3
            positions[name]['direc'] = compass[direc]
        # Lorsque l'on avance d'une case
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

            if futur_x < 0 or futur_y < 0 or futur_y > (len(treasure_map)-1) or futur_x > (len(treasure_map[0])-1)\
                or treasure_map[futur_y][futur_x] == 'M' or re.search('A-', treasure_map[futur_y][futur_x]):
                continue

            pos_map = treasure_map[futur_y][futur_x]

            if re.search(r'T\(\d+\)', pos_map):
                pattern = re.compile(r'\((\d+)\)')
                num = int(pattern.findall(pos_map)[0])
                if num > 0:
                    treasure_map[futur_y][futur_x] = 'T({})'.format(num - 1)
                    positions[name]['treasure'] += 1
            positions[name]['x'] = futur_x
            positions[name]['y'] = futur_y
            treasure_map[pos_y][pos_x] = str(treasure_map[pos_y][pos_x]).replace('A-{}'.format(name), '').strip()
            treasure_map[futur_y][futur_x] = (str(treasure_map[futur_y][futur_x]) + ' A-{}'.format(name)).strip()

def display_map(treasure_map):
    """
    Display the map
    """
    for y in treasure_map:
        print(y)

if __name__ == "__main__":
    text = read_input('input.txt')
    parsed = parse_input(text)
    treasure_map = init_map(parsed)
    positions, sequence = parse_adventurers(parsed)
    print('BEGINNING')
    display_map(treasure_map)
    move_adventurers(treasure_map, positions, sequence)
    print('END')
    display_map(treasure_map)
    write_output(treasure_map, positions)
