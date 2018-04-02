with open('Data/test.csv','r',encoding='utf-8') as f1:
    with open('Data/trans_test.csv','r',encoding='utf-8') as f2:
        with open('Data/freq_test.csv','w',encoding='utf-8') as f3:
            f1.readline()
            f2.readline()
            f3.write('ip_freq,app_freq,device_freq,os_freq,channel_freq,ip_app_freq,ip_device_freq,ip_channel_freq,app_channel_freq,ip_app_channel_freq,hour_freq,MM_freq,lable'+'\n')
            print(f1.readline())
            print(f2.readline())
            number = 0
            while True:
                number+=1
                Line1 = f1.readline().strip()
                Line2 = f2.readline().strip()
                if Line1 and Line2:
                    line1 = Line1.split(',')
                    line2 = Line2.split(',')
                    line = []
                    for i,item in enumerate(line2):
                        if i%2==1:
                            line.append(item)
                    if number == 5:
                        f3.write(','.join(line)+'\n')
                        number = 0
