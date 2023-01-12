import json
from json import JSONDecodeError


def load_files(path):
    try:
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError:
        print('Файл не найден')
    except JSONDecodeError:
        print('Файл не удается преобразовать')
    else:
        return data


def search_posts_by_key(search_key):
    data = load_files('posts.json')

    posts_by_key = []

    for item in data:
        if search_key.lower() in item['content'].lower():
            posts_by_key.append(item)

    return posts_by_key


def add_post_in_file(pic, content):
    data = load_files('posts.json')
    data.append({
                    "pic": pic,
                    "content": content
    })

    with open('posts.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)

    for item in data:
        if item['pic'] == pic:
            return item
