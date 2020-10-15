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
