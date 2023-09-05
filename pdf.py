import yaml

class Translate:
    def __init__(self, word):
        self.word = word

    def translate(self):
        with open('dictionary.yaml', 'r') as file:
            dictionary = yaml.safe_load(file)
        if self.word in dictionary:
            return dictionary[self.word]
        else:
            return "Không tìm thấy từ này trong từ điển"

while True:
    try:
        word = input("Nhập từ bạn cần dịch: ")
        if word.isalnum():
            break
        else:
            print("Vui lòng nhập lại")
    except:
        print("Vui lòng nhập lại")

print(f"Nghĩa của từ này là {Translate(word).translate()}")

while True:
    hoi = input("Bạn có muốn tiếp tục hay không? (C/K) ")
    if hoi == "K" or hoi == "k":
        break