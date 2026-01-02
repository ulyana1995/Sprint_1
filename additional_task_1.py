from copy import deepcopy 

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(tickets):
    start_index = 1
    for current_index in range(len(tickets.keys())):
        for current_ticket in list(tickets.values())[current_index]:
            for next_level_index in range(start_index, len(tickets.keys())):
                for lower_ticket in list(tickets.values())[next_level_index]:
                    if current_ticket == lower_ticket:
                        tickets[next_level_index + 1].remove(lower_ticket)
        start_index+= 1
    return tickets

def assign_tickets_to_types(types, tickets):
    copied_tickets = deepcopy(tickets)
    tickets_by_type = {}
    unique_tickets = remove_duplicates(copied_tickets)
    for key, value in types.items():
        tickets_by_type[value] = unique_tickets.get(key)     
    return tickets_by_type

grouped_tickets = assign_tickets_to_types(types, tickets)
print(grouped_tickets)