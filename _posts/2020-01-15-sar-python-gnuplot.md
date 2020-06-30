---
layout: post
title:  "sar python gnuplot"
---

Основная задача всего этого (single script, pure python and console output) вот такие графики в консоли:

![SAR-PY-PLOT](https://joingig.github.io/images/sar-py-00.jpg)

Подготовка:

1. Устанавливаем sar, в составе пакета sysstat
1. Устанавливаем gnuplot

> yum install sysstat
>
> yum install gnuplot
        

First of, get sar data (CPU utilisation) and push it to python app sar00.py:

    LC_TIME="POSIX"  /usr/bin/sar -C | egrep -i -v Linux\|Average\|CPU  | /usr/bin/python sar00.py

Python для фильтрации данных sar [sar00.py](https://github.com/joingig/joingig.github.io/blob/master/sar00.py) ( **attention! spaghetti code ahead!** )


```python
import fileinput as fi
import pprint as pp

def main():
    kk = [line.split() for line in fi.input()]

    iline, hr_nxt, hr_cur, sum_util, sum_h, hr_cnt = 0, 0, 0, 0, 0, 1;
    sar_sum = [(h,0) for h in range(0,24)]

    f_sarfiltered = '/tmp/sar_data.txt'

    while iline < len(kk):
        if len(kk[iline]) < 2:
            iline+=1
            continue

        hr_nxt = kk[iline][0].split(':')[0]

        if hr_nxt!=hr_cur:
            #old fashion
            sum_h = sum_util / hr_cnt
            sar_sum[int(hr_cur)] = (int(hr_cur),sum_h)
            sum_util = 100 - float(kk[iline][7])
            hr_cur=hr_nxt
            hr_cnt = 1
        else:
            sum_util += 100 - float(kk[iline][7])
            hr_cnt += 1

        iline += 1

    pp.pprint (sar_sum)

    print '{} writing'.format(f_sarfiltered)

    with open(f_sarfiltered, 'w') as f:
        for item in sar_sum:
            print >> f, item[0],item[1]

if __name__ == "__main__":
    main()
```

Python выдаёт файл *sar_data.txt* (это прописано внутри *sar00.py* в переменной *f__sarfiltered*)

Конфигурация gnuplot, файл *sar.gnuplot*

    set term dumb
    set yrange [0:100]
    set ylabel "%"
    set xlabel "Hour"
    set style data histogram
    set style fill solid border -1
    plot for [i=2:3] "/dev/stdin" using i:xtic(1) title "CPU usage"

Основной pipeline который "нарисует" график в файл sar.graph00:

    gnuplot -p sar.gnuplot < sar_data.txt > sar.graph00
