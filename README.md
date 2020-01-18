# lsd
LED Scrolling Data - python app to display scrolling messages on LED dot matrix connected to RPi.

![Demo](README.gif)

## Description

LSD queries and displays notifications from [github.com/pruh/api](https://github.com/pruh/api). The app expects the following parameters:
```
  -u URL, --url URL     API base URL
  -a USERNAME, --username USERNAME
                        HTTP basic auth username
  -p PASSWORD, --password PASSWORD
                        HTTP basic auth password
```

type `lsd.py --help` for more info.

## LED Dot Matrix Connection

LSD requires LED Dot Matrix to be connected to RPi using the following scheme:

| Matrix PIN | RPi GPIO PIN |
|-|-|
|OE|18|
|CLK|17|
|LAT|4|
|A|22|
|B|23|
|C|24|
|RED1|11|
|GREEN1|27|
|BLUE1|7|
|RED2|8|
|GREEN2|9|
|BLUE2|10|

More info on how matrix works can be found [here](https://www.bigmessowires.com/2018/05/24/64-x-32-led-matrix-programming/)