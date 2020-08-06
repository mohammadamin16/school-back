from persiantools.jdatetime import JalaliDate
import datetime


def main():
    date = datetime.datetime.now()
    print(date)
    p = JalaliDate(date)
    print(p)


def get_today():
    date = datetime.datetime.now()
    return JalaliDate(date).strftime('%y-%m-%d')


if __name__ == '__main__':
    main()
