class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):

        try:
            self.text = text

            keyi = 0
            n = len(self.alphabet)
            newkey = list()

            for a in self.text:
                newkey.append(self.key[keyi])
                keyi = (keyi + 1) % len(self.key)

            res1 = []
            for i in range(len(self.text)):
                for j in range(len(self.alphabet)):
                    if self.text[i] == self.alphabet[j]:
                        res1.append(j)

            res2 = []
            for i in range(len(newkey)):
                for j in range(len(self.alphabet)):
                    if newkey[i] == self.alphabet[j]:
                        res2.append(j)

            mod = []
            for i in range(len(self.text)):
                mod.append((res1[i] + res2[i]) % n)

            res = []
            for i in mod:
                res.append(self.alphabet[i])

            res = ''.join(res)

            return res
        
        except:
            print("ERROR")
            return self.text
    
    def decode(self, text):

        try:
            self.text = text

            keyi = 0
            n = len(self.alphabet)
            newkey = list()

            for a in self.text:
                newkey.append(self.key[keyi])
                keyi = (keyi + 1) % len(self.key)

            res1 = []
            for i in range(len(self.text)):
                for j in range(len(self.alphabet)):
                    if self.text[i] == self.alphabet[j]:
                        res1.append(j)

            res2 = []
            for i in range(len(newkey)):
                for j in range(len(self.alphabet)):
                    if newkey[i] == self.alphabet[j]:
                        res2.append(j)

            mod = []
            for i in range(len(self.text)):
                mod.append((res1[i] - res2[i]) % n)

            res = []
            for i in mod:
                res.append(self.alphabet[i])

            res = ''.join(res)

            return res
        
        except:
            print("ERROR")
            return self.text

conf = VigenereCipher("key", 'abcdefghijklmnopqrstuvwxyz')
e = conf.encode("hello")
d = conf.decode(e)
print(e, d)