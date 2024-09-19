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
    'tttt': 2,
    'vvvvv': 'ssss'
}

# print(site)


def find_key(target_key, input_dict):
    result = None

    for key in input_dict:
        if key == target_key:
            return input_dict[key]
        else:
            if isinstance(input_dict[key], dict):
                result = find_key(target_key, input_dict[key])
                if result:
                    break
    return result


res = find_key("div", site)
print(res)
