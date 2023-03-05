import string


# task_6.1_pdf_git
class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop == None:
            self.start += 1
            return self.start
        elif self.start < self.stop:
            self.start += 1
            return self.start
        elif self.start == self.stop:
            return "Maximal value is reached"

    def get(self):
        return self.start


c = Counter(1, 2)
print(c.increment())
print(c.get())
print(c.increment())


# task_6.2_pdf_git
class Dict:
    dict_keys = []

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.dictionary = dict.fromkeys(self.key, self.value)
        Dict.dict_keys.append(self.key)

    @staticmethod
    def get_history():
        return Dict.dict_keys[-10:]

    def set_value(self, new_key, new_value):
        self.key = new_key
        self.value = new_value
        Dict.dict_keys.append(self.key)


d = Dict("test", 1)
print(d.get_history())
d.set_value("bar", 2)
print((d.get_history()))
d.set_value("zar", 2)
d.set_value("sar", 2)
d.set_value("mar", 2)
d.set_value("nar", 2)
d.set_value("lar", 2)
d.set_value("buar", 2)
d.set_value("bfar", 2)
d.set_value("bgar", 2)
d.set_value("lar", 2)
d.set_value("kar", 2)
d.set_value("car", 2)
print(d.get_history())


# task_6.3_pdf_git
class Cipher:
    alphabet = string.ascii_uppercase

    def __init__(self, string: str):
        self.string = string.upper()

    def encode(self, encode_str):
        append_alphabet = self.string + Cipher.alphabet
        l_ = [append_alphabet[0]]
        for i in append_alphabet[1:]:
            if i not in l_:
                l_.append(i)
        new_alphabet = "".join(l_)
        encode_list = []
        encode_str = encode_str.upper()
        cipher_string = []
        m = 0
        n = 0
        for j in new_alphabet:
            if m < len(encode_list):
                j = new_alphabet[encode_list[m]]
                if j == new_alphabet[-1]:
                    j = ' '
                cipher_string.append(j)
                m += 1
            for c in Cipher.alphabet:
                if n < len(encode_str):
                    c = Cipher.alphabet.find(encode_str[n])
                    encode_list.append(c)
                    n += 1
        cipher_string = "".join(cipher_string)
        return cipher_string.capitalize()

    def decode(self, decode_str):
        append_alphabet = self.string + Cipher.alphabet
        l_ = [append_alphabet[0]]
        for i in append_alphabet[1:]:
            if i not in l_:
                l_.append(i)
        new_alphabet = "".join(l_)
        encode_list = []
        encode_str = decode_str.upper()
        cipher_string = []
        m = 0
        n = 0
        for j in Cipher.alphabet:
            if m < len(encode_list):
                j = Cipher.alphabet[encode_list[m]]
                if j == Cipher.alphabet[-1]:
                    j = ' '
                cipher_string.append(j)
                m += 1
            for c in new_alphabet:
                if n < len(encode_str):
                    c = new_alphabet.find(encode_str[n])
                    encode_list.append(c)
                    n += 1
        cipher_string = "".join(cipher_string)
        return cipher_string.capitalize()


c = Cipher("crypto")
print(c.encode("Hello world"))
print(c.decode("Btggj vjmgp"))

# task_6.4_pdf_git
class Birds:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name} может летать')

    def walk(self):
        print(f'{self.name} может ходить')

    def __str__(self):
        method_list = [method for method in dir(Birds) if method.startswith('__') is False]
        method_list = " ".join(method_list)
        return f'{self.name} имеет методы: {method_list}'


class FlyingBird(Birds):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f'{self.name} ест насекомых')

    def __str__(self):
        method_list = [method for method in dir(FlyingBird) if method.startswith('__') is False]
        method_list = " ".join(method_list)
        return f'{self.name} имеет методы: {method_list}'


class NonflyingBird(Birds):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        raise AttributeError(f'{self.name} не умеет летать')
        # exit()

    def eat(self):
        print(f'{self.name} ест семена и червей')

    def __str__(self):
        method_list = [method for method in dir(NonflyingBird) if method.startswith('__') is False]
        method_list = " ".join(method_list)
        return f'{self.name} имеет методы: {method_list}'


class SwimmingBird(Birds):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f'{self.name} ест рыбу')

    def swim(self):
        print(f'{self.name} плавает')

    def __str__(self):
        method_list = [method for method in dir(SwimmingBird) if method.startswith('__') is False]
        method_list = " ".join(method_list)
        return f'{self.name} имеет методы: {method_list}'


class Penguin(SwimmingBird, NonflyingBird):
    def __init__(self, name):
        super().__init__(name)


class Duck(FlyingBird, SwimmingBird):
    def __init__(self, name):
        super().__init__(name)


b = Birds('Any')
p = Penguin("Penguin")
p.eat()
d = Duck("Утка")
# p.fly()
d.fly()
d.eat()
d.swim()
print(p)
print(d)
# с str вообще не уверен, что нужно было так делать. И почему-то не показывает у утки метод swim, хотя он есть
# и с пингвином, не знаю, как убрать из видимости fly
