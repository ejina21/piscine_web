import antigravity
import sys

def get_hash():
    if (len(sys.argv) == 4):
        try:
            latitude = float(sys.argv[1])
        except:
            return print("Широта должна быть типа float")
        try:
            longitude = float(sys.argv[2])
        except:
            return print("Долгота должна быть типа float")
        try:
            datedow = sys.argv[3].encode('utf-8')
        except:
            return print("Дата должна быть типа string")
        antigravity.geohash(latitude, longitude, datedow)
    else:
        print("Введите широту, долготу и дату(пример: 110.0 90.9 2005-05-26-10458.68)")

if __name__ == '__main__':
    get_hash()