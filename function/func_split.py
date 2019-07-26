# function_split.py

#### 분리를 위한 함수 ####

# is_int(var) - 문자열의 원소가 숫자인지 검사하는 함수
def is_int(var):
    try:
        temp_var = int(var) # 정수형으로 변환 시도
        return True # 에러가 발생하지 않으면 True 반환(정수임을 의미)
    except:
        return False # 에러가 발생하면 False 반환(알파벳임을 의미)

# element_position_finder(compound) - 문자열(화학식)에서 알파벳들의 위치를 파악하는 함수
def element_position_finder(compound):
    position = []
    for i in range(0, len(compound)):
        if compound[i]=='.': 
            continue
        if is_int(compound[i])!= True:
            position.append(i)
        else: 
            continue
    # print(compound)
    # print(position)
    return position
            
# constant_split(compound, position) - 화학식에서 상수를 분리해내는 함수
def constant_split(comp, pos):
    constant = []
    constant.clear()
    for i in range(0, len(pos)):
        if i != (len(pos)-1):
            if (pos[i+1] - pos[i])!= 1:
                constant.append(comp[pos[i]+1:pos[i+1]])
        else:
            try:
                constant.append(comp[pos[i]+1:])
            except:
                break
    # print(constant)
    return constant

        
# compound_split(compound, pos) - 화학식에서 원소를 분리해내는 함수
def element_split(comp, pos):
    elements = []
    elements.clear()
    i=0
    while i < len(pos):
        if i != (len(pos)-1):
            if (pos[i+1] - pos[i])== 1:
                elements.append(comp[pos[i]:pos[i]+2])
                i += 2
            else:
                elements.append(comp[pos[i]])
                i += 1
        else:
            elements.append(comp[pos[i]])
            i+=1
        
        # print(elements)
    return elements


# joiner(elements, constant) - 분리해낸 원소들 리스트와 상수들 리스트를 결합해내는 함수
# 최종 출력 element1, const1, element2, const2, ...
def joiner(elements, constant):
    encoded = []
    encoded.clear()
    for i in range(0, len(elements)):
        encoded.append(elements[i])
        encoded.append(constant[i])
    
    # print(encoded)
    fin = ','.join(encoded)
    
    
    # print(fin)
    return fin

def encoder(comp):
    el_pos = element_position_finder(comp)
    el_const_list = constant_split(comp, el_pos)
    el_list = element_split(comp, el_pos)
    return joiner(el_list, el_const_list)