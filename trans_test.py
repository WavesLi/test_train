import time
import csv
import gc
import json
json_file = open('Mid_deal/test.count.json','r',encoding='utf-8')
ip_dict,app_dict,device_dict,os_dict,channel_dict,ip_app_dict,ip_device_dict,ip_channel_dict,app_channel_dict,ip_app_channel_dict,day_dict,hour_dict,MM_dict=[json.loads(i) for i in json_file.readlines()]
json_file.close()
gc.collect()
with open('Data/trans_test.csv','w',encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(
        ['ip', 'ip_freq', 'app', 'app_freq', 'device', 'device_freq', 'os', 'os_freq', 'channel', 'channel_freq', 'ip_app', 'ip_app_freq',
         'ip_device', 'ip_device_freq', 'ip_channel', 'ip_channel_freq', 'app_channel', 'app_channel_freq', 'ip_app_channel',
         'ip_app_channel_freq', 'day', 'day_freq', 'hour', 'hour_freq', 'MM', 'MM_freq'])
    with open('Data/test.csv','r',encoding='utf-8') as f:
        f.readline()
        i = 1
        while True:
            # gc.collect()
            # list = []
            line = f.readline()
            if line:
                Line = line.strip().split(',')
                ip = Line[1]
                ip_freq = ip_dict[ip]
                app = Line[2]
                app_freq = app_dict[app]
                device = Line[3]
                device_freq = device_dict[device]
                os = Line[4]
                os_freq = os_dict[os]
                channel = Line[5]
                channel_freq = channel_dict[channel]
                ip_app = Line[1]+'-'+Line[2]
                ip_app_freq = ip_app_dict[ip_app]
                ip_device = Line[1]+'-'+Line[3]
                ip_device_freq = ip_device_dict[ip_device]
                ip_channel = Line[1]+'-'+Line[5]
                ip_channel_freq = ip_channel_dict[ip_channel]
                app_channel = Line[2]+'-'+Line[5]
                app_channel_freq = app_channel_dict[app_channel]
                ip_app_channel = Line[1]+'-'+Line[2]+'-'+Line[5]
                ip_app_channel_freq = ip_app_channel_dict[ip_app_channel]
                day = Line[6].split(' ')[0]
                day_freq = day_dict[day]
                hour = Line[6].split(' ')[1].split(':')[0]
                hour_freq = hour_dict[hour]
                MM = Line[6].split(' ')[1].split(':')[1]
                MM_freq = MM_dict[MM]
                # list.append([ip,ip_freq,app,app_freq,device,device_freq,os,os_freq,channel,channel_freq,ip_app,ip_app_freq,
                #              ip_device,ip_device_freq,ip_channel,ip_channel_freq,app_channel,app_channel_freq,ip_app_channel,
                #             ip_app_channel_freq,day,day_freq,hour,hour_freq,MM,MM_freq])
                writer.writerow([ip,ip_freq,app,app_freq,device,device_freq,os,os_freq,channel,channel_freq,ip_app,ip_app_freq,
                             ip_device,ip_device_freq,ip_channel,ip_channel_freq,app_channel,app_channel_freq,ip_app_channel,
                            ip_app_channel_freq,day,day_freq,hour,hour_freq,MM,MM_freq])
                i+=1
                print(i)
            else:
                break
            # i+=1
            # print(i)
            # if i == 100:
            #     writer.writerows(list)
            #     print(list)
            #     time.sleep(5)
            #     gc.collect()
            #     # csv_file.flush()
            #     i = 1
