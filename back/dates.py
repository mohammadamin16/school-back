from persiantools.jdatetime import JalaliDate
import datetime


def main():
    date = datetime.datetime.now()
    print(date)
    p = JalaliDate(date)
    print(p)


if __name__ == '__main__':
    main()