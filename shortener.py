import random

def rand_first():
    x = random.randint(65,90)
    return x
def rand_second():
    y = random.randint(97,122)
    return y
def rand_third():
    z = random.randint(0,9)
    return z


def rand_String():
    rand_str = ''
    while len(rand_str) != 6:
        random_call = random.randint(1,3)
        if random_call == 1:
            letter = chr(rand_first())
        elif random_call == 2:
            letter = chr(rand_second())
        else:
            letter = str(rand_third())
        rand_str += letter
        letter = ''
        
    return rand_str


def shortener():
    main_str = 'https://yk.py/' + rand_String()

    return main_str

def store(url, shortened_url):
    urls = {}
    urls[url] = shortened_url


if __name__ == '__main__':
    url = input("\nEnter the url\n")
    shortened_url = shortener()
    store(url, shortened_url)
    print(shortened_url)
