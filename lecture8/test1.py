'''
def html_bold(func):
    def inner(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return inner

@html_bold
def get_name(user: str):
    return user.upper()


@html_bold
def greetings(user: str):
    return f'Hello, {user}'

name = input('name=')
print(get_name(name))
print(greetings(name))
'''
#Якщо треба, щоб був декоратор з параметрами
def tags(tag):
    def decorator(func):
        def inner(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return inner
    return decorator


@tags('b')
def get_name(user: str):
    return user.upper()


@tags('i')
def greetings(user: str):
    return f'Hello, {user}'


name = input('name=')
print(get_name(name))
print(greetings(name))
'''
def tags(tag):
    def decorator(func):
        def inner(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return inner
    return decorator

@tags('p')
@tags('b')
def get_name(user: str):
    return user.upper()


@tags('i')
def greetings(user: str):
    return f'Hello, {user}'


name = input('name=')
print(get_name(name))
print(greetings(name))
'''