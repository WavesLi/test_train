import json

ip = {}
app = {}
device = {}
os = {}
channel = {}
day = {}
hour = {}
MM = {}
ip_app = {}
ip_device = {}
ip_channel = {}
app_channel = {}
ip_app_channel = {}

with open('Data/train.csv', 'r', encoding='utf-8') as f:
    f.readline()
    while True:
        Line = f.readline()
        if Line.strip():
            line = Line.split(',')
            if line[0] in ip.keys():
                ip[line[0]] += 1
            else:
                ip[line[0]] = 1
            if line[1] in app.keys():
                app[line[1]] += 1
            else:
                app[line[1]] = 1
            if line[2] in device.keys():
                device[line[2]] += 1
            else:
                device[line[2]] = 1
            if line[3] in os.keys():
                os[line[3]] += 1
            else:
                os[line[3]] = 1
            if line[4] in channel.keys():
                channel[line[4]] += 1
            else:
                channel[line[4]] = 1
            if str(line[0])+'-'+str(line[1]) in ip_app.keys():
                ip_app[str(line[0])+'-'+str(line[1])] += 1
            else:
                ip_app[str(line[0])+'-'+str(line[1])] = 1
            if str(line[0])+'-'+str(line[2]) in ip_device.keys():
                ip_device[str(line[0])+'-'+str(line[2])] += 1
            else:
                ip_device[str(line[0])+'-'+str(line[2])] = 1
            if str(line[0])+'-'+str(line[4]) in ip_channel.keys():
                ip_channel[str(line[0])+'-'+str(line[4])] += 1
            else:
                ip_channel[str(line[0])+'-'+str(line[4])] = 1

            if str(line[1])+'-' + str(line[4]) in app_channel.keys():
                app_channel[str(line[1])+'-' + str(line[4])] += 1
            else:
                app_channel[str(line[1])+'-' + str(line[4])] = 1
            if str(line[0])+'-'+str(line[1])+'-' + str(line[4]) in ip_app_channel.keys():
                ip_app_channel[str(line[0])+'-'+str(line[1])+'-' + str(line[4])] += 1
            else:
                ip_app_channel[str(line[0])+'-'+str(line[1])+'-' + str(line[4])] = 1
            if line[5].split(' ')[0] in day.keys():
                day[line[5].split(' ')[0]] += 1
            else:
                day[line[5].split(' ')[0]] =1
            if line[5].split(' ')[1].split(':')[0] in hour.keys():
                hour[line[5].split(' ')[1].split(':')[0]] += 1
            else:
                hour[line[5].split(' ')[1].split(':')[0]] =1

            if line[5].split(' ')[1].split(':')[1] in MM.keys():
                MM[line[5].split(' ')[1].split(':')[1]] += 1
            else:
                MM[line[5].split(' ')[1].split(':')[1]] =1
        else:
            break


with open('Data/test.csv', 'r', encoding='utf-8') as f:
    f.readline()
    while True:
        Line = f.readline()
        if Line.strip():
            line = Line.split(',')
            if line[1] in ip.keys():
                ip[line[1]] += 1
            else:
                ip[line[1]] = 1
            if line[2] in app.keys():
                app[line[2]] += 1
            else:
                app[line[2]] = 1
            if line[3] in device.keys():
                device[line[3]] += 1
            else:
                device[line[3]] = 1
            if line[4] in os.keys():
                os[line[4]] += 1
            else:
                os[line[4]] = 1
            if line[5] in channel.keys():
                channel[line[5]] += 1
            else:
                channel[line[5]] = 1
            if str(line[1])+'-'+str(line[2]) in ip_app.keys():
                ip_app[str(line[1])+'-'+str(line[2])] += 1
            else:
                ip_app[str(line[1])+'-'+str(line[2])] = 1
            if str(line[1])+'-'+str(line[3]) in ip_device.keys():
                ip_device[str(line[1])+'-'+str(line[3])] += 1
            else:
                ip_device[str(line[1])+'-'+str(line[3])] = 1
            if str(line[1])+'-'+str(line[5]) in ip_channel.keys():
                ip_channel[str(line[1])+'-'+str(line[5])] += 1
            else:
                ip_channel[str(line[1])+'-'+str(line[5])] = 1

            if str(line[2])+'-' + str(line[5]) in app_channel.keys():
                app_channel[str(line[2])+'-' + str(line[5])] += 1
            else:
                app_channel[str(line[2])+'-' + str(line[5])] = 1
            if str(line[1])+'-'+str(line[2])+'-' + str(line[5]) in ip_app_channel.keys():
                ip_app_channel[str(line[1])+'-'+str(line[2])+'-' + str(line[5])] += 1
            else:
                ip_app_channel[str(line[1])+'-'+str(line[2])+'-' + str(line[5])] = 1
            if line[6].split(' ')[0] in day.keys():
                day[line[6].split(' ')[0]] += 1
            else:
                day[line[6].split(' ')[0]] =1
            if line[6].split(' ')[1].split(':')[0] in hour.keys():
                hour[line[6].split(' ')[1].split(':')[0]] += 1
            else:
                hour[line[6].split(' ')[1].split(':')[0]] =1

            if line[6].split(' ')[1].split(':')[1] in MM.keys():
                MM[line[6].split(' ')[1].split(':')[1]] += 1
            else:
                MM[line[6].split(' ')[1].split(':')[1]] =1
        else:
            break

with open('Mid_deal/test.count.json','w',encoding='utf-8') as f:
    print(ip)
    f.write(json.dumps(ip,ensure_ascii=False)+'\n')
    print(app)
    f.write(json.dumps(app, ensure_ascii=False) + '\n')
    print(device)
    f.write(json.dumps(device, ensure_ascii=False) + '\n')
    print(os)
    f.write(json.dumps(os, ensure_ascii=False) + '\n')
    print(channel)
    f.write(json.dumps(channel, ensure_ascii=False) + '\n')
    print(ip_app)
    f.write(json.dumps(ip_app, ensure_ascii=False) + '\n')
    print(ip_device)
    f.write(json.dumps(ip_device, ensure_ascii=False) + '\n')
    print(ip_channel)
    f.write(json.dumps(ip_channel, ensure_ascii=False) + '\n')
    print(app_channel)
    f.write(json.dumps(app_channel, ensure_ascii=False) + '\n')
    print(ip_app_channel)
    f.write(json.dumps(ip_app_channel, ensure_ascii=False) + '\n')
    print(day)
    f.write(json.dumps(day, ensure_ascii=False) + '\n')
    print(hour)
    f.write(json.dumps(hour, ensure_ascii=False) + '\n')
    print(MM)
    f.write(json.dumps(MM, ensure_ascii=False) + '\n')
