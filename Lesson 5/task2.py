import copy
site = {
    'html': {
        'head': {
            'title': "куплю/продам телефон недорого"
        },
        'body': {
            'h1': "тут самая низкая цена на айфон",
            'div': "купить",
            'p': "продать"
        }
    },
    'aaa': 3
}


def change_value(struct, key, value):
    if key in struct:
        struct[key] = value
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                change_value(sub_struct, key, value)
    return struct


sites = []

site1 = copy.deepcopy(site)
# site1 = site
change_value(site1, 'title', 'куплю вишню')
change_value(site1, 'h1', 'вишня')
sites.append(site1)

site2 = copy.deepcopy(site)
# site2 = site
change_value(site2, 'title', 'куплю мороженое')
change_value(site2, 'h1', 'мороженое')
sites.append(site2)

print(sites)
